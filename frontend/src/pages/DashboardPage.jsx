import { useQuery } from '@tanstack/react-query'
import { fetchHotspots, fetchSummary } from '../api/client'

export function DashboardPage() {
  const summaryQuery = useQuery({ queryKey: ['summary'], queryFn: fetchSummary })
  const hotspotsQuery = useQuery({ queryKey: ['hotspots'], queryFn: fetchHotspots })

  return (
    <main style={{ maxWidth: 900, margin: '2rem auto', fontFamily: 'sans-serif' }}>
      <h1>India Corruption Transparency Dashboard</h1>
      <p>Aggregated statistics only. No raw accusations or personal evidence are shown.</p>

      <section>
        <h2>Summary</h2>
        {summaryQuery.isLoading ? <p>Loading...</p> : <pre>{JSON.stringify(summaryQuery.data, null, 2)}</pre>}
      </section>

      <section>
        <h2>Hotspots</h2>
        {hotspotsQuery.isLoading ? <p>Loading...</p> : <pre>{JSON.stringify(hotspotsQuery.data, null, 2)}</pre>}
      </section>
    </main>
  )
}
