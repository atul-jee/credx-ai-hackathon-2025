# ⚡ CredX AI Job Recommendation

An AI-powered job recommendation system that suggests jobs based on user preferences and provides AI-generated explanations. Built for **CredX Hackathon 2025**.

---

## 🛠 Tech Stack

**Frontend:** React (Vite, TailwindCSS, Axios)
**Backend:** Flask (Python, Flask-CORS)
**AI Models:** Google Gemini API (embeddings + explanations)
**ML Components:** Fuzzy Logic + Cosine Similarity (Hybrid Model)

---

## 📂 Project Structure

```
credx-job-recommendation/
│── backend/
│   ├── app.py                # Flask backend
│   ├── jobs/jobs.json        # Job dataset
│   └── requirements.txt      # Python dependencies
│
│── frontend/
│   ├── src/
│   │   ├── App.jsx           # Main React app
│   │   ├── Components/       # PreferenceForm, JobCard, etc.
│   │   └── services/api.js   # API calls
│   ├── package.json          # Frontend dependencies
│   └── vite.config.js        # Vite config
│
└── README.md
```

---

## 🔧 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/atul-jee/credx-ai-hackathon-2025.git
cd credx-job-recommendation
```

### 2️⃣ Setup Backend (Flask)

```bash
cd backend
python -m venv venv
# Activate virtual environment
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
```

Create a `.env` file in `backend/` and add your Gemini API key:

```
GEMINI_API_KEY=your_api_key_here
```

Run Flask server:

```bash
python app.py
```

Backend runs at 👉 `http://127.0.0.1:5000`

### 3️⃣ Setup Frontend (React + Vite)

```bash
cd ../frontend
npm install
npm run dev
```

Frontend runs at 👉 `http://localhost:5173`

---

## 🚀 Usage

1. Start backend: `python app.py`
2. Start frontend: `npm run dev`
3. Open browser at `http://localhost:5173`
4. Fill the **Preference Form** → Click **Recommend**
5. View job recommendations along with AI explanations

---

## 📌 Future Improvements

* ✅ Resume parsing (PDF/DOCX upload)


---
# Algo:
## 1️⃣ Fuzzy Logic (Structured Match)

### Matches user preferences against structured job fields like skills, titles, location, industry, company size, values, and salary.Calculates a score between 0 and 1 for each field based on partial or exact matches.Helps provide interpretable recommendations.

##2️⃣ Embedding Similarity (Semantic Match)

### Uses Google Gemini API to convert user preferences and job descriptions into vector embeddings.Computes cosine similarity between embeddings to measure semantic closeness.Captures matches even when keywords differ (e.g., “Frontend Developer” vs “React Engineer”).

## 3️⃣ Hybrid Recommendation

### Combines fuzzy logic and embedding similarity for a robust scoring system: final_score = 0.6 * fuzzy_score + 0.4 * embedding_score Ensures recommendations consider both exact matches and semantic meaning.

## 4️⃣ AI Explanations Uses Gemini generative model to provide short, human-readable explanations for each recommended job.Helps users understand why a job is suggested, improving trust in the system.
This hybrid approach ensures accurate, explainable, and intelligent job recommendations.
## 👨‍💻 Contributors
**Team Name:2100060018eee**
**Atul Jee**

✨ Built for **CredX Hackathon 2025** 🚀
