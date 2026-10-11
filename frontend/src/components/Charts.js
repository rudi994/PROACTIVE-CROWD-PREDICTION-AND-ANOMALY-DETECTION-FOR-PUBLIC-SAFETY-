import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line, Bar, Doughnut } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend
);

const Charts = ({ stats }) => {
  // Sample data - replace with actual data from your backend
  const timeSeriesData = {
    labels: ['10:25', '10:26', '10:27', '10:28', '10:29', '10:30', '10:31'],
    datasets: [
      {
        label: 'Crowd Count',
        data: [1200, 1350, 1500, 1650, stats.crowdCount || 1761, 1700, 1620],
        borderColor: 'rgb(75, 192, 192)',
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        tension: 0.4,
        fill: true,
      },
      {
        label: 'Violation Count',
        data: [15, 18, 20, 22, stats.violationCount || 23, 21, 19],
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        tension: 0.4,
        fill: true,
      },
    ],
  };

  const violationTypeData = {
    labels: ['Social Distancing', 'Mask Violation', 'Restricted Area', 'Overcrowding'],
    datasets: [
      {
        label: 'Violation Types',
        data: [12, 5, 3, 3],
        backgroundColor: [
          'rgba(255, 99, 132, 0.8)',
          'rgba(54, 162, 235, 0.8)',
          'rgba(255, 206, 86, 0.8)',
          'rgba(75, 192, 192, 0.8)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
        ],
        borderWidth: 2,
      },
    ],
  };

  const densityData = {
    labels: ['Low Density', 'Medium Density', 'High Density', 'Critical Density'],
    datasets: [
      {
        label: 'Crowd Density Distribution',
        data: [15, 35, 40, 10],
        backgroundColor: [
          'rgba(75, 192, 192, 0.8)',
          'rgba(54, 162, 235, 0.8)',
          'rgba(255, 206, 86, 0.8)',
          'rgba(255, 99, 132, 0.8)',
        ],
        borderColor: [
          'rgba(75, 192, 192, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(255, 99, 132, 1)',
        ],
        borderWidth: 2,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Crowd Analytics',
      },
    },
    maintainAspectRatio: false,
  };

  return (
    <div className="charts-container">
      <div className="charts-header">
        <h3>📊 Analytics Dashboard</h3>
        <div className="charts-description">
          Real-time crowd behavior analysis and trend visualization
        </div>
      </div>

      <div className="charts-grid">
        <div className="chart-card">
          <div className="chart-title">Crowd & Violation Trends</div>
          <div className="chart-wrapper">
            <Line data={timeSeriesData} options={chartOptions} height={300} />
          </div>
          <div className="chart-footer">
            Tracking crowd density and safety violations over time
          </div>
        </div>

        <div className="chart-card">
          <div className="chart-title">Violation Type Distribution</div>
          <div className="chart-wrapper">
            <Doughnut data={violationTypeData} options={chartOptions} height={300} />
          </div>
          <div className="chart-footer">
            Breakdown of different types of safety violations
          </div>
        </div>

        <div className="chart-card">
          <div className="chart-title">Crowd Density Analysis</div>
          <div className="chart-wrapper">
            <Bar data={densityData} options={chartOptions} height={300} />
          </div>
          <div className="chart-footer">
            Current crowd density levels across monitored areas
          </div>
        </div>

        <div className="chart-card metrics">
          <div className="chart-title">Key Performance Indicators</div>
          <div className="metrics-grid">
            <div className="metric-item">
              <div className="metric-value">{stats.crowdCount || 0}</div>
              <div className="metric-label">Total Detections</div>
            </div>
            <div className="metric-item">
              <div className="metric-value">{stats.violationCount || 0}</div>
              <div className="metric-label">Active Violations</div>
            </div>
            <div className="metric-item">
              <div className="metric-value">
                {stats.crowdCount > 0 ? ((stats.violationCount / stats.crowdCount) * 100).toFixed(1) : 0}%
              </div>
              <div className="metric-label">Violation Rate</div>
            </div>
            <div className="metric-item">
              <div className="metric-value">
                {stats.restrictedEntry ? 'High' : 'Low'}
              </div>
              <div className="metric-label">Risk Level</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Charts;