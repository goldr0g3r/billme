import axios from "axios";

const baseURL =
  process.env.REACT_APP_BACKEND_BASE_URL || "http://localhost:8000";

axios.defaults.baseURL = baseURL;
const api = axios.create({
  baseURL: baseURL, // Replace with your API base URL
  timeout: 1000,
  headers: { "Content-Type": "application/json" },
});

export default api;
