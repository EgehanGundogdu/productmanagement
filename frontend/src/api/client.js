import axios from "axios";

const apiService = axios.create({
  baseURL: process.env.BASEURL,
  headers: {
    "Content-type": "application/json"
  }
});

export default apiService;
