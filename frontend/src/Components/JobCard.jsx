import { useState } from "react";

function JobCard({ job }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div
      className="job-card border border-gray-300 rounded-xl p-4 shadow-md bg-white hover:shadow-lg transition cursor-pointer w-full mb-4"
      onClick={() => setExpanded(!expanded)}
    >
      {/* Job title & company */}
      <h2 className="job-title font-bold text-xl text-gray-800">{job.job_title}</h2>
      <p className="job-company text-gray-600">
        {job.company} — {job.location}
      </p>

      {/* Match Score */}
      <p className="job-score text-blue-600 font-medium mt-2">
        Match: {job.match_score}%
      </p>

      {/* Expandable breakdown */}
      {expanded && (
        <div className="breakdown mt-4 border-t pt-3">
          <h3 className="font-semibold text-gray-700 mb-2">Breakdown:</h3>
          <ul className="list-disc ml-5 space-y-1 text-gray-600">
            {Object.entries(job.breakdown).map(([k, v]) => (
              <li key={k}>
                {k}: {(v * 100).toFixed(0)}%
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default JobCard;
