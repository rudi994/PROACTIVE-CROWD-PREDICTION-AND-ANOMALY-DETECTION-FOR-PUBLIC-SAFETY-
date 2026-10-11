// components/WebSocketVideoPlayer.js
import React, { useEffect, useRef, useState } from 'react';

const WebSocketVideoPlayer = () => {
  const videoRef = useRef(null);
  const [stats, setStats] = useState({});
  const [connected, setConnected] = useState(false);

  useEffect(() => {
    const ws = new WebSocket('ws://localhost:8765');
    
    ws.onopen = () => {
      console.log('WebSocket connected');
      setConnected(true);
    };
    
    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      
      // Update video frame
      if (videoRef.current) {
        videoRef.current.src = `data:image/jpeg;base64,${data.frame}`;
      }
      
      // Update stats
      setStats(data.stats);
    };
    
    ws.onclose = () => {
      console.log('WebSocket disconnected');
      setConnected(false);
    };
    
    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
      setConnected(false);
    };
    
    return () => {
      ws.close();
    };
  }, []);

  return (
    <div className="video-container">
      <h3>Live Video (WebSocket)</h3>
      <div className="connection-status">
        WebSocket: {connected ? 'Connected' : 'Disconnected'}
      </div>
      <div className="video-wrapper">
        <img 
          ref={videoRef}
          alt="WebSocket Video Stream"
          className="video-stream"
        />
      </div>
    </div>
  );
};

export default WebSocketVideoPlayer;

  // or use your custom weights file


// Use results to draw boxes and get stats