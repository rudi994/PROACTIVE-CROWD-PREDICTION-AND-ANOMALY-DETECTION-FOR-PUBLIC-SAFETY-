CrowdSense — Command & Control Dashboard
=========================================

CORRECT FOLDER STRUCTURE (this is what went wrong before):

  CrowdSense_Dashboard/          <-- your working folder
  ├── app.py                     <-- run this
  ├── README.txt
  ├── templates/
  │   └── index.html
  ├── static/
  │   ├── data.js
  │   └── events.js
  └── crowd_model_output/
      ├── processed_features.csv
      ├── future_forecast.csv
      ├── alert_log.csv
      ├── surge_periods.csv
      └── model_config.json

COMMON MISTAKE:
  Do NOT put app.py inside crowd_model_output/
  app.py must be at the TOP level next to the folders

HOW TO RUN:
  1. Open terminal / command prompt
  2. cd into CrowdSense_Dashboard folder
  3. pip install flask
  4. python app.py
  5. Open http://localhost:5000

ACCURACY (honest numbers from your run):
  Realtime display (1s):  R² = 0.9996
  5s ahead prediction:    R² = 0.3639  MAE = 4.83 people
  Rule-based alerts:      100% reliable (no ML needed)
