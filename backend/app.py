from flask import Flask, request, jsonify
from flask_cors import CORS
import json, os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# Load job data
JOBS_PATH = os.path.join(os.path.dirname(__file__), "jobs", "jobs.json")
with open(JOBS_PATH) as f:
    JOBS = json.load(f)

# Configure Gemini
genai.configure(api_key='')# Put your Gemini API key in the environment variable GEMINI_API_KEY

# ----------- Fuzzy Logic Weights -----------
WEIGHTS = {
    "skills": 0.30,
    "title": 0.20,
    "location": 0.15,
    "industry": 0.10,
    "company_size": 0.10,
    "values": 0.10,
    "salary": 0.05,
}

# ----------- Embedding Helper (Gemini) -----------
def get_embedding(text):
    if not text:
        return np.zeros(768)  # Gemini embedding dim is 768
    response = genai.embed_content(
        model="models/embedding-001",
        content=text
    )
    return np.array(response["embedding"])

# Precompute embeddings for all jobs
for job in JOBS:
    job["embedding"] = get_embedding(
        f"{job['title']} {job['company']} {job['location']} {job['industry']} {' '.join(job['required_skills'])}"
    )

# ----------- Fuzzy Logic Scoring -----------
def fuzzy_score(prefs, job):
    breakdown = {}

    skills = prefs.get("skills", [])
    if skills:
        matched = len(set(skills) & set(job.get("required_skills", [])))
        breakdown["skills"] = matched / len(skills)
    else:
        breakdown["skills"] = 0

    titles = prefs.get("titles", [])
    breakdown["title"] = 1 if any(t.lower() in job["title"].lower() for t in titles) else 0

    breakdown["location"] = 1 if job["location"] in prefs.get("locations", []) else 0
    breakdown["industry"] = 1 if job["industry"] in prefs.get("industries", []) else 0
    breakdown["company_size"] = 1 if job["company_size"] in prefs.get("company_size", []) else 0

    values = prefs.get("values", [])
    promoted = job.get("values_promoted", [])
    breakdown["values"] = len(set(values) & set(promoted)) / len(values) if values else 0

    min_salary = prefs.get("min_salary", 0)
    salary_range = job.get("salary_range", [0, 0])
    breakdown["salary"] = 1 if salary_range[1] >= min_salary else 0

    score = sum(breakdown[k] * WEIGHTS[k] for k in WEIGHTS) * 100
    return score, breakdown

# ----------- Gemini Explanation -----------
def explain_recommendation(job, prefs):
    prompt = f"""
    User preferences: {prefs}
    Job: {job}
    Explain in 2-3 sentences why this job is a good match for the user.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Explanation unavailable: {str(e)}"

# ----------- API Endpoint -----------
@app.route("/api/recommend", methods=["POST"])
def recommend():
    prefs = request.json
    print("✅ Received preferences:", prefs)

    pref_text = f"Titles: {prefs.get('titles', [])}, Skills: {prefs.get('skills', [])}, Industry: {prefs.get('industries', [])}, Location: {prefs.get('locations', [])}, Values: {prefs.get('values', [])}, Salary: {prefs.get('min_salary', 0)}"
    pref_embedding = get_embedding(pref_text)

    results = []
    for job in JOBS:
        # Fuzzy score
        fuzzy, breakdown = fuzzy_score(prefs, job)

        # Embedding similarity
        sim = cosine_similarity([pref_embedding], [job["embedding"]])[0][0]
        embedding_score = sim * 100

        # Hybrid score
        final_score = round(0.6 * fuzzy + 0.4 * embedding_score, 2)

        results.append({
            "job_id": job["job_id"],
            "job_title": job["title"],
            "company": job["company"],
            "location": job["location"],
            "match_score": final_score,
            "breakdown": {
                "fuzzy_score": fuzzy,
                "embedding_score": embedding_score,
                **breakdown
            },
            "explanation": explain_recommendation(job, prefs)
        })

    results.sort(key=lambda x: x["match_score"], reverse=True)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
