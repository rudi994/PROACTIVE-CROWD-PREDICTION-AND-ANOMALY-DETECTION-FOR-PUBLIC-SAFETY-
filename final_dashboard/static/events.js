const ALERT_EVENTS = [
  {
    "id": "EVT-001",
    "time_min": 3.2,
    "time_sec": 193.0,
    "level": "WARNING",
    "peak": 65,
    "mean": 63.8,
    "duration_s": 5.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-002",
    "time_min": 5.5,
    "time_sec": 329.0,
    "level": "WARNING",
    "peak": 74,
    "mean": 73.3,
    "duration_s": 5.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-003",
    "time_min": 6.6,
    "time_sec": 399.0,
    "level": "CRITICAL",
    "peak": 75,
    "mean": 74.0,
    "duration_s": 7.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-004",
    "time_min": 9.1,
    "time_sec": 546.0,
    "level": "WARNING",
    "peak": 68,
    "mean": 66.3,
    "duration_s": 5.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-005",
    "time_min": 10.9,
    "time_sec": 655.0,
    "level": "WARNING",
    "peak": 63,
    "mean": 61.7,
    "duration_s": 5.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-006",
    "time_min": 12.5,
    "time_sec": 748.0,
    "level": "WATCH",
    "peak": 25,
    "mean": 15.3,
    "duration_s": 17.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-007",
    "time_min": 12.9,
    "time_sec": 775.0,
    "level": "WARNING",
    "peak": 70,
    "mean": 65.8,
    "duration_s": 25.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-008",
    "time_min": 17.0,
    "time_sec": 1022.0,
    "level": "WARNING",
    "peak": 74,
    "mean": 71.2,
    "duration_s": 7.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-009",
    "time_min": 20.7,
    "time_sec": 1243.0,
    "level": "WATCH",
    "peak": 23,
    "mean": 21.5,
    "duration_s": 5.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-010",
    "time_min": 21.6,
    "time_sec": 1297.0,
    "level": "WATCH",
    "peak": 27,
    "mean": 16.9,
    "duration_s": 6.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-011",
    "time_min": 21.9,
    "time_sec": 1313.0,
    "level": "WATCH",
    "peak": 23,
    "mean": 21.9,
    "duration_s": 7.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-012",
    "time_min": 22.7,
    "time_sec": 1360.0,
    "level": "WATCH",
    "peak": 24,
    "mean": 12.9,
    "duration_s": 17.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-013",
    "time_min": 23.3,
    "time_sec": 1397.0,
    "level": "WATCH",
    "peak": 24,
    "mean": 13.5,
    "duration_s": 12.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-014",
    "time_min": 23.6,
    "time_sec": 1415.0,
    "level": "WATCH",
    "peak": 21,
    "mean": 17.6,
    "duration_s": 7.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-015",
    "time_min": 23.9,
    "time_sec": 1434.0,
    "level": "WATCH",
    "peak": 23,
    "mean": 13.8,
    "duration_s": 7.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-016",
    "time_min": 26.5,
    "time_sec": 1589.0,
    "level": "WATCH",
    "peak": 45,
    "mean": 35.6,
    "duration_s": 8.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-017",
    "time_min": 27.5,
    "time_sec": 1649.0,
    "level": "WARNING",
    "peak": 74,
    "mean": 69.5,
    "duration_s": 14.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-018",
    "time_min": 29.2,
    "time_sec": 1752.0,
    "level": "WATCH",
    "peak": 24,
    "mean": 19.7,
    "duration_s": 8.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-019",
    "time_min": 31.9,
    "time_sec": 1913.0,
    "level": "CRITICAL",
    "peak": 76,
    "mean": 69.4,
    "duration_s": 8.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-020",
    "time_min": 32.5,
    "time_sec": 1952.0,
    "level": "CRITICAL",
    "peak": 83,
    "mean": 78.1,
    "duration_s": 15.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-021",
    "time_min": 32.8,
    "time_sec": 1969.0,
    "level": "CRITICAL",
    "peak": 76,
    "mean": 73.4,
    "duration_s": 15.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-022",
    "time_min": 33.1,
    "time_sec": 1988.0,
    "level": "CRITICAL",
    "peak": 82,
    "mean": 74.7,
    "duration_s": 9.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-023",
    "time_min": 33.3,
    "time_sec": 2000.0,
    "level": "CRITICAL",
    "peak": 76,
    "mean": 73.2,
    "duration_s": 12.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-024",
    "time_min": 34.5,
    "time_sec": 2072.0,
    "level": "WATCH",
    "peak": 32,
    "mean": 20.6,
    "duration_s": 9.0,
    "type": "SURGE_ONSET"
  },
  {
    "id": "EVT-025",
    "time_min": 43.9,
    "time_sec": 2633.0,
    "level": "WATCH",
    "peak": 23,
    "mean": 13.4,
    "duration_s": 22.0,
    "type": "SURGE_ONSET"
  }
];