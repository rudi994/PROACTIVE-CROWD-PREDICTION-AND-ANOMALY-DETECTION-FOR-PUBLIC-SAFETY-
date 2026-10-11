import React from 'react';

const StatsDisplay = ({ stats, loading }) => {
  const {
    crowdCount = 0,
    violationCount = 0,
    restrictedEntry = false,
    abnormalActivity = false,
    timestamp = new Date().toLocaleTimeString()
  } = stats;

  if (loading) {
    return (
      <div className="stats-container">
        <h3>📈 Real-time Statistics</h3>
        <div className="stats-loading">
          <div className="loading-spinner"></div>
          <p>Loading statistics...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="stats-container">
      <div className="stats-header">
        <h3>📈 Real-time Statistics</h3>
        <div className="timestamp">
          Last updated: {timestamp}
        </div>
      </div>
      
      <div className="stats-grid">
        <div className="stat-card crowd">
          <div className="stat-icon">👥</div>
          <div className="stat-content">
            <div className="stat-value">{crowdCount.toLocaleString()}</div>
            <div className="stat-label">Crowd Count</div>
            <div className="stat-trend">Real-time detection</div>
          </div>
        </div>

        <div className="stat-card violation">
          <div className="stat-icon">⚠️</div>
          <div className="stat-content">
            <div className="stat-value">{violationCount}</div>
            <div className="stat-label">Violation Count</div>
            <div className="stat-trend">Safety breaches detected</div>
          </div>
        </div>

        <div className={`stat-card ${restrictedEntry ? 'warning' : 'safe'}`}>
          <div className="stat-icon">{restrictedEntry ? '🚫' : '✅'}</div>
          <div className="stat-content">
            <div className="stat-value">{restrictedEntry ? 'Yes' : 'No'}</div>
            <div className="stat-label">Restricted Entry</div>
            <div className="stat-trend">
              {restrictedEntry ? 'Unauthorized access' : 'No violations'}
            </div>
          </div>
        </div>

        <div className={`stat-card ${abnormalActivity ? 'alert' : 'normal'}`}>
          <div className="stat-icon">{abnormalActivity ? '🚨' : '👍'}</div>
          <div className="stat-content">
            <div className="stat-value">{abnormalActivity ? 'Detected' : 'Normal'}</div>
            <div className="stat-label">Crowd Activity</div>
            <div className="stat-trend">
              {abnormalActivity ? 'Abnormal pattern' : 'Normal behavior'}
            </div>
          </div>
        </div>
      </div>

      <div className="stats-summary">
        <div className="summary-item">
          <span className="summary-label">Total Detections:</span>
          <span className="summary-value">{crowdCount}</span>
        </div>
        <div className="summary-item">
          <span className="summary-label">Violation Rate:</span>
          <span className="summary-value">
            {crowdCount > 0 ? ((violationCount / crowdCount) * 100).toFixed(1) : 0}%
          </span>
        </div>
        <div className="summary-item">
          <span className="summary-label">Safety Score:</span>
          <span className="summary-value">
            {crowdCount > 0 ? (100 - (violationCount / crowdCount) * 100).toFixed(0) : 100}/100
          </span>
        </div>
      </div>
    </div>
  );
};

export default StatsDisplay;