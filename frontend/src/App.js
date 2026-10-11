import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import VideoPlayer from './components/VideoPlayer';
import StatsDisplay from './components/StatsDisplay';
import Charts from './components/Charts';
import './styles/App.css';

function App() {
  const [stats, setStats] = useState({
    crowdCount: 0,
    violationCount: 0,
    restrictedEntry: false,
    abnormalActivity: false,
    timestamp: new Date().toLocaleTimeString()
  });
  
  const [backendConnected, setBackendConnected] = useState(false);
  const [isProcessing, setIsProcessing] = useState(false);
  const [loading, setLoading] = useState(true);

  // Check backend connection and fetch initial stats
  useEffect(() => {
    const checkBackend = async () => {
      try {
        const response = await fetch('http://localhost:5000/');
        if (response.ok) {
          setBackendConnected(true);
          fetchStats();
        }
      } catch (error) {
        console.log('Backend connection failed:', error);
        setBackendConnected(false);
      } finally {
        setLoading(false);
      }
    };

    checkBackend();
    const interval = setInterval(checkBackend, 5000);
    return () => clearInterval(interval);
  }, []);

  // Fetch statistics from backend
  const fetchStats = async () => {
    try {
      const response = await fetch('http://localhost:5000/stats');
      if (response.ok) {
        const data = await response.json();
        setStats({
          crowdCount: data.crowd_count || 0,
          violationCount: data.violation_count || 0,
          restrictedEntry: data.restricted_entry || false,
          abnormalActivity: data.abnormal_activity || false,
          timestamp: new Date().toLocaleTimeString()
        });
      }
    } catch (error) {
      console.log('Failed to fetch stats:', error);
    }
  };

  // Start video processing
  const startProcessing = async () => {
    try {
      setIsProcessing(true);
      const response = await fetch('http://localhost:5000/start_processing', {
        method: 'POST'
      });
      
      if (response.ok) {
        const result = await response.json();
        alert(`Processing started: ${result.message}`);
        // Start fetching stats more frequently when processing
        const statsInterval = setInterval(fetchStats, 1000);
        return () => clearInterval(statsInterval);
      }
    } catch (error) {
      alert('Failed to start processing. Make sure Python backend is running.');
      setIsProcessing(false);
    }
  };

  return (
    <div className="app">
      <Header />
      
      <div className="connection-banner">
        <div className={`connection-status ${backendConnected ? 'connected' : 'disconnected'}`}>
          <span className="status-indicator"></span>
          Backend: {backendConnected ? 'Connected ✅' : 'Disconnected ❌'}
          {!backendConnected && (
            <span className="help-text">
              - Run: <code>python backend.py</code>
              
            </span>
          )}
        </div>
      </div>

      <div className="main-container">
        <div className="left-panel">
          <VideoPlayer 
            videoSource={backendConnected ? "http://localhost:5000/video_feed" : ""}
            onProcessingStart={startProcessing}
            isProcessing={isProcessing}
          />
          <StatsDisplay stats={stats} loading={loading} />
        </div>
        
        <div className="right-panel">
          <Charts stats={stats} />
        </div>
      </div>
    </div>
  );
}

export default App;