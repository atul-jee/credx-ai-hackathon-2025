import { useState } from "react";

function PreferenceForm({ onRecommend }) {
  const [input, setInput] = useState(`{
  "values": ["Impactful Work", "Mentorship & Career Development", "Work-Life Balance"],
  "role_types": ["Full-Time", "Contract"],
  "titles": ["UI/UX Designer", "Senior Product Designer"],
  "locations": ["Remote in USA", "New York City"],
  "role_level": ["Senior (5 to 8 years)"],
  "leadership_preference": "Individual Contributor",
  "company_size": ["51-200 Employees", "201-500 Employees"],
  "industries": ["AI & Machine Learning", "Design"],
  "skills": ["Figma", "UI/UX Design", "Wireframing", "Prototyping"],
  "min_salary": 185000
}`);

  const handleSubmit = (e) => {
    e.preventDefault();
    try {
      const prefs = JSON.parse(input);
      onRecommend(prefs);
    } catch {
      alert("Invalid JSON!");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form">
      <textarea
        value={input}
        onChange={(e) => setInput(e.target.value)}
        rows={10}
        className="textarea"
      />
      <button type="submit" className="btn">
        Recommend
      </button>
    </form>
  );
}

export default PreferenceForm;
