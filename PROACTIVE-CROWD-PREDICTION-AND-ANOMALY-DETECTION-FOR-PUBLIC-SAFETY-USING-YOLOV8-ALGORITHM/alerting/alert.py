import time
import requests
import logging
from config import ALERT_COUNT_THRESHOLD, ALERT_ANOMALY_THRESHOLD, ALERT_COOLDOWN, TSI_ENDPOINT

last_alert_time = 0

def send_alert_if_needed(crowd_count, anomaly_score, frame_id=None):
    """Check thresholds and send alert to web app if needed."""
    global last_alert_time
    now = time.time()

    if now - last_alert_time < ALERT_COOLDOWN:
        return  # prevent spamming

    if crowd_count > ALERT_COUNT_THRESHOLD or anomaly_score > ALERT_ANOMALY_THRESHOLD:
        payload = {
            "crowd_count": crowd_count,
            "anomaly_score": anomaly_score,
            "frame_id": frame_id,
            "timestamp": now
        }
        try:
            r = requests.post(TSI_ENDPOINT, json=payload, timeout=5)
            r.raise_for_status()
            logging.info(f"Alert sent to web app: {payload}")
            last_alert_time = now
        except Exception as e:
            logging.error(f"Failed to send alert: {e}")
