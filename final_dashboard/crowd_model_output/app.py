"""
CrowdSense — Command & Control Dashboard
Run: python app.py
Open: http://localhost:5000

Folder structure MUST be:
  your_folder/
  ├── app.py                  ← this file
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
"""

from flask import Flask, jsonify, render_template
import pandas as pd
import json
import os
from pathlib import Path

app = Flask(__name__)

DATA_DIR = Path("crowd_model_output")

def load_all():
    data = {}
    try:
        pf  = pd.read_csv(DATA_DIR / "processed_features.csv")
        fc  = pd.read_csv(DATA_DIR / "future_forecast.csv")
        al  = pd.read_csv(DATA_DIR / "alert_log.csv")
        sp  = pd.read_csv(DATA_DIR / "surge_periods.csv")

        pf_s = pf[::3].copy()
        data["history"] = [
            {"t":  round(float(r["elapsed_sec"]),1),
             "m":  round(float(r["elapsed_min"]),2),
             "c":  int(r["count"]),
             "sm": round(float(r["roll_mean_30"]),1),
             "v":  round(float(r["velocity"]),2),
             "sev":str(r["severity"]),
             "an": int(r["anomaly_ensemble"]),
             "av": int(r["anomaly_votes"])}
            for _, r in pf_s.iterrows()
        ]

        data["forecast"] = [
            {"t":    round(float(r["future_sec"]),1),
             "m":    round(float(r["future_min"]),2),
             "pred": round(float(r["predicted_count"]),1),
             "lo":   round(float(r["lower_95"]),1),
             "hi":   round(float(r["upper_95"]),1),
             "an":   int(r["predicted_count"] >= 60)}
            for _, r in fc.iterrows()
        ]

        data["surges"] = [
            {"start_m": round(float(r["start_min"]),2),
             "end_m":   round(float(r["end_min"]),2),
             "dur_s":   round(float(r["duration_sec"]),1),
             "peak":    int(r["peak_count"]),
             "mean":    float(r["mean_count"])}
            for _, r in sp.iterrows()
        ]

        notable = al[al["level"].isin(["WARNING","CRITICAL","SURGE"])].copy()
        data["alerts"] = [
            {"t":     round(float(r["time_sec"])/60,2),
             "c":     int(r["count"]),
             "lv":    str(r["level"]),
             "v":     round(float(r["velocity"]),2),
             "surge": bool(r["is_surge"])}
            for _, r in notable.iterrows()
        ]

        data["stats"] = {
            "total_frames":    int(len(pf)),
            "duration_min":    round(float(pf["elapsed_min"].max()),1),
            "max_count":       int(pf["count"].max()),
            "min_count":       int(pf["count"].min()),
            "mean_count":      round(float(pf["count"].mean()),1),
            "std_count":       round(float(pf["count"].std()),1),
            "anomaly_pct":     round(float(pf["anomaly_ensemble"].mean()*100),1),
            "anomaly_frames":  int(pf["anomaly_ensemble"].sum()),
            "surge_periods":   int(len(sp)),
            "critical_frames": int((pf["severity"]=="CRITICAL").sum()),
            "warning_frames":  int((pf["severity"]=="WARNING").sum()),
            "watch_frames":    int((pf["severity"]=="WATCH").sum()),
            "normal_frames":   int((pf["severity"]=="NORMAL").sum()),
            "threshold_anomaly":  60,
            "threshold_critical": 75,
            "forecast_final":  round(float(fc["predicted_count"].iloc[-1]),1),
            "forecast_lo":     round(float(fc["lower_95"].iloc[-1]),1),
            "forecast_hi":     round(float(fc["upper_95"].iloc[-1]),1),
            "data_start":      "2026-03-31 14:39:53",
            "data_end":        "2026-03-31 15:25:15",
            "best_model":      "Ridge Regression",
            "split_method":    "Strict Temporal 80/20 + 60-frame gap",
            "r2_realtime":     0.9996,
            "r2_5s":           0.3639,
            "mae_realtime":    0.224,
            "mae_5s":          4.83,
            "train_frames":    2178,
            "test_frames":     485,
            "gap_frames":      60,
        }

        data["models"] = {
            "Ridge (realtime)":    {"MAE":0.224, "RMSE":0.28,  "R2":0.9996},
            "Ridge (5s ahead)":    {"MAE":4.83,  "RMSE":6.10,  "R2":0.3639},
            "Random Forest (5s)":  {"MAE":5.84,  "RMSE":7.20,  "R2":0.1212},
            "Gradient Boost (5s)": {"MAE":6.01,  "RMSE":7.40,  "R2":0.0673},
            "Ensemble (5s)":       {"MAE":5.26,  "RMSE":6.50,  "R2":0.2650},
            "ARIMA":               {"MAE":15.38, "RMSE":17.04, "R2":0.4431},
            "Holt-Winters":        {"MAE":11.27, "RMSE":14.84, "R2":0.5867},
        }

        data["horizon_acc"] = {
            "1s":  {"r2":0.9631, "mae":1.13,  "quality":"STRONG",   "pct":96.3},
            "5s":  {"r2":0.3513, "mae":4.83,  "quality":"MODERATE", "pct":35.1},
            "15s": {"r2":-1.091, "mae":9.02,  "quality":"WEAK",     "pct":0},
            "30s": {"r2":-1.975, "mae":10.65, "quality":"WEAK",     "pct":0},
        }

        print("✅ Data loaded from CSV files")

    except Exception as e:
        print(f"⚠️  Could not load CSV files: {e}")
        print("   Using embedded data.js fallback")
        data = None

    return data


DATA = load_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/all")
def api_all():
    if DATA:
        return jsonify(DATA)
    return jsonify({"error": "No data loaded — check crowd_model_output folder"}), 500


@app.route("/api/history")
def api_history():
    return jsonify(DATA["history"] if DATA else [])


@app.route("/api/forecast")
def api_forecast():
    return jsonify(DATA["forecast"] if DATA else [])


@app.route("/api/surges")
def api_surges():
    return jsonify(DATA["surges"] if DATA else [])


@app.route("/api/alerts")
def api_alerts():
    return jsonify(DATA["alerts"] if DATA else [])


@app.route("/api/stats")
def api_stats():
    return jsonify(DATA["stats"] if DATA else {})


@app.route("/api/models")
def api_models():
    return jsonify(DATA["models"] if DATA else {})


if __name__ == "__main__":
    print("\n" + "="*50)
    print("  CrowdSense Dashboard")
    print("  Open: http://localhost:5000")
    print("="*50 + "\n")
    app.run(debug=True, port=5000)
