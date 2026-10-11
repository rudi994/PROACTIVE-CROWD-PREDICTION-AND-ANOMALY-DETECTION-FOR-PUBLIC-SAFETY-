import React, { useState, useEffect } from 'react';

const VideoPlayer = ({ videoSource, onProcessingStart, isProcessing }) => {
  const [videoError, setVideoError] = useState('');
  const [currentVideo, setCurrentVideo] = useState('');

  useEffect(() => {
    if (videoSource) {
      setCurrentVideo(videoSource);
    }
  }, [videoSource]);

  const handleVideoError = () => {
    setVideoError('Failed to load video stream. Check backend connection.');
  };

  const handleVideoLoad = () => {
    setVideoError('');
  };

  return (
    <div className="video-container">
      <div className="video-header">
        <h3>📹 Live Video Feed with YOLOv8 Detection</h3>
        <div className="video-status">
          Status:{' '}
          <span className={isProcessing ? 'processing' : 'idle'}>
            {isProcessing ? 'Processing' : 'Ready'}
          </span>
        </div>
      </div>

      <div className="video-wrapper">
        {isProcessing ? (
          <>
            <img
              src="/placeholder-image.png"
              alt="Processing in progress..."
              className="w-full h-auto rounded-lg shadow-md"
            />
            <p className="text-gray-600 mt-3 text-center">
              Video is being processed in the backend. Live view is disabled.
            </p>
          </>
        ) : currentVideo ? (
          <img
            src={currentVideo}
            alt="YOLOv8 Processed Video Feed"
            className="video-stream"
            onError={handleVideoError}
            onLoad={handleVideoLoad}
          />
        ) : (
          <div className="video-placeholder">
            <div className="placeholder-content">
              <div className="placeholder-icon">📹</div>
              <h4>No Video Source</h4>
              <p>Configure video source in backend</p>
            </div>
          </div>
        )}
      </div>

      {videoError && (
        <div className="error-message">
          <strong>Error:</strong> {videoError}
        </div>
      )}

      <div className="video-info">
        <div className="info-item">
          <span className="info-label">Source:</span>
          <span className="info-value">{videoSource || 'Not specified'}</span>
        </div>
        <div className="info-item">
          <span className="info-label">Processing:</span>
          <span className="info-value">YOLOv8 Object Detection</span>
        </div>
      </div>

      <div className="video-controls">
        <button
          className={`control-btn primary ${isProcessing ? 'active' : ''}`}
          onClick={onProcessingStart}
          disabled={isProcessing}
        >
          {isProcessing ? '🔄 Processing...' : '🚀 Start YOLOv8 Processing'}
        </button>

        <button className="control-btn secondary">
          📊 Export Results
        </button>

        <button
          className="control-btn secondary"
          onClick={() => window.location.reload()}
        >
          🔄 Refresh
        </button>
      </div>
    </div>
  );
};

export default VideoPlayer;
