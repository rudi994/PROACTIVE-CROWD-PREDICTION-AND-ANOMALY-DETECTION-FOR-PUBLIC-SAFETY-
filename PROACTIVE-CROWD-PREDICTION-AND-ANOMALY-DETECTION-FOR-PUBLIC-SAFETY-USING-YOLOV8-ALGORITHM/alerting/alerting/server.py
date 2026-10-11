from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

# Store alerts in memory (simple demo, you can later use DB)
alerts = []

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    alerts.append(data)
    print("⚠️ ALERT RECEIVED:", data)
    return jsonify({"status": "ok"}), 200

@app.route("/")
def index():
    # Show alerts on web page
    return render_template("alerts.html", alerts=alerts)

@app.route("/alerts", methods=["GET"])
def get_alerts():
    return jsonify({"alerts": alerts}), 200

@app.route("/video-metadata", methods=["GET"])
def video_metadata():
    # Compute project root relative to this file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.normpath(os.path.join(current_dir, "..", "..", ".."))
    metadata_path = os.path.join(project_root, "PROACTIVE-CROWD-PREDICTION-AND-ANOMALY-DETECTION-FOR-PUBLIC-SAFETY-USING-YOLOV8-ALGORITHM", "processed_data", "video_data.json")
    if not os.path.exists(metadata_path):
        return jsonify({"error": "video_data.json not found", "path": metadata_path}), 404
    try:
        with open(metadata_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
