import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_BASE || 'http://127.0.0.1:8000';

export const api = {
  getLinks: () => axios.get(`${API_BASE}/api/links/`),
  createLink: (data) => axios.post(`${API_BASE}/api/links/`, data),
  getLinkStats: (code) => axios.get(`${API_BASE}/api/links/${code}/`),
  deleteLink: (code) => axios.delete(`${API_BASE}/api/links/${code}/`),
};