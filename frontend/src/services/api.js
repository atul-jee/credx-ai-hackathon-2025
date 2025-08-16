import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5000/api", // ✅ point only to /api
});

export const getRecommendations = (preferences) =>
  API.post("/recommend", preferences);
