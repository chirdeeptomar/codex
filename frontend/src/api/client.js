const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000/api'

export async function fetchSummary() {
  const response = await fetch(`${API_BASE}/public/analytics/summary`)
  return response.json()
}

export async function fetchHotspots() {
  const response = await fetch(`${API_BASE}/public/analytics/hotspots`)
  return response.json()
}
