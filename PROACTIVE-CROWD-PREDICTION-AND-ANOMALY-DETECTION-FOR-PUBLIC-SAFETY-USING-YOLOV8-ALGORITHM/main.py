import os
import csv
import json
import time
import datetime
import cv2

from config import (VIDEO_CONFIG, FRAME_SIZE, DATA_RECORD_RATE,
                    SHOW_PROCESSING_OUTPUT)
from video_process import video_process

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ── Video source ──────────────────────────────────────
video_path = os.path.join(BASE_DIR, "assets", "videoplayback.mp4")
print(f"Loading video: {video_path}")
print(f"File exists: {os.path.exists(video_path)}")

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    exit()

# ── FPS ───────────────────────────────────────────────
VID_FPS = cap.get(cv2.CAP_PROP_FPS) or 30
VID_FPS = max(1, VID_FPS)
print(f"FPS: {VID_FPS}")

DATA_RECORD_FRAME = max(1, int(VID_FPS / DATA_RECORD_RATE))
print(f"Recording every {DATA_RECORD_FRAME} frames")

# ── Output files ──────────────────────────────────────
os.makedirs("processed_data", exist_ok=True)

movement_data_file = open("processed_data/movement_data.csv", "w",
                          newline="", encoding="utf-8")
crowd_data_file    = open("processed_data/crowd_data.csv", "w",
                          newline="", encoding="utf-8")

movement_data_writer = csv.writer(movement_data_file)
crowd_data_writer    = csv.writer(crowd_data_file)

crowd_data_writer.writerow(
    ["Time", "Human Count", "Social Distance Violations",
     "Restricted Entry", "Abnormal Activity"])

movement_data_writer.writerow(
    ["Track ID", "Entry Time", "Exit Time", "Movement Tracks"])

print("CSV files ready.")

# ── Run ───────────────────────────────────────────────
START_TIME = time.time()

try:
    # ✅ FIXED: only 2 arguments now
    video_process(cap, FRAME_SIZE, crowd_data_writer)

except Exception as e:
    print(f"Error: {e}")
    import traceback; traceback.print_exc()

finally:
    cv2.destroyAllWindows()
    movement_data_file.close()
    crowd_data_file.close()
    cap.release()

END_TIME = time.time()
print(f"Total time: {END_TIME - START_TIME:.2f}s")

# ── Save metadata ─────────────────────────────────────
with open("processed_data/video_data.json", "w") as f:
    json.dump({
        "VID_FPS": float(VID_FPS),
        "FRAME_SIZE": FRAME_SIZE,
        "DATA_RECORD_FRAME": DATA_RECORD_FRAME,
        "START_TIME": datetime.datetime.fromtimestamp(START_TIME).strftime("%d/%m/%Y %H:%M:%S"),
        "END_TIME":   datetime.datetime.fromtimestamp(END_TIME).strftime("%d/%m/%Y %H:%M:%S"),
    }, f, indent=2)

print("Done. Data saved in processed_data/")