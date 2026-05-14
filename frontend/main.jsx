import React, { useState } from 'react'
import ReactDOM from 'react-dom/client'

function App() {
  const [query, setQuery] = useState('')
  const [result, setResult] = useState(null)

  async function analyze() {
    const res = await fetch('http://localhost:8000/analyze', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ query })
    })

    const data = await res.json()
    setResult(data)
  }

  return (
    <div style={{padding: 24, fontFamily: 'Arial'}}>
      <h1>跨文档矛盾检测 Agent</h1>

      <input
        value={query}
        onChange={e => setQuery(e.target.value)}
        placeholder="输入问题"
        style={{width: 400, padding: 8}}
      />

      <button onClick={analyze} style={{marginLeft: 12}}>
        分析
      </button>

      {result && (
        <pre style={{marginTop: 24, background: '#eee', padding: 16}}>
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(<App />)