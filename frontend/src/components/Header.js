import './../styles/App.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header-content">
        <h1>🚦 Crowd Prediction & Anomaly Detection System</h1>
        <p>Using YOLOv8 Algorithm for Public Safety</p>
        <div className="header-badge">
          Real-time Monitoring Active
        </div>
      </div>
    </header>
  );
};

export default Header;