import { useState } from "react";
import PreferenceForm from "./Components/PreferenceForm";
import JobCard from "./Components/JobCard";
import { getRecommendations } from "./services/api";
import "./App.css";

function App() {
  const [jobs, setJobs] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // ---- Handle preference form submit ----
  const handleRecommend = async (prefs) => {
    setLoading(true);
    setError("");
    try {
      const response = await getRecommendations(prefs);
      setJobs(response.data);
    } catch (err) {
      console.error("Error fetching recommendations:", err);
      setError("Failed to fetch recommendations. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container flex flex-col items-center p-6">
      <h1 className="title text-3xl font-bold mb-6 text-gray-800">
        CredX Job Recommender
      </h1>

      {/* Only preference form now */}
      <PreferenceForm onRecommend={handleRecommend} />

      {loading && <p className="text-blue-600 mt-4">Loading recommendations...</p>}
      {error && <p className="text-red-500 mt-4">{error}</p>}

      <div className="jobs-grid mt-6 w-full max-w-3xl">
        {jobs.length > 0 ? (
          jobs.map((job) => <JobCard key={job.job_id} job={job} />)
        ) : (
          !loading && (
            <p className="placeholder text-gray-500 mt-4">
              No recommendations yet. Fill preferences above and submit.
            </p>
          )
        )}
      </div>
    </div>
  );
}

export default App;
