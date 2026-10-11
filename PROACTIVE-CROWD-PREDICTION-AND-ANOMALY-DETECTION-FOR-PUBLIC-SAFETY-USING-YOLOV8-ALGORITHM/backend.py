from flask import Flask, jsonify
from flask_cors import CORS
import cv2
import time
import threading
import os
from datetime import datetime

# Import your YOLO pipeline
from video_process import detect_with_tiling

app = Flask(__name__)
CORS(app)

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_SOURCE = os.path.join(BASE_DIR, "assets", "videoplayback.mp4")

# ─────────────────────────────────────────────
# GLOBAL STATE
# ─────────────────────────────────────────────
processing_active = False
processing_thread = None

current_stats = {
    'crowd_count': 0,
    'processing_status': 'stopped',
    'frames_processed': 0,
    'current_frame': 0,
    'total_frames': 0,
    'processing_fps': 0,
    'restricted_entry': False,
    'abnormal_activity': False
}

crowd_data_history = []

# ─────────────────────────────────────────────
# MAIN PROCESSING FUNCTION
# ─────────────────────────────────────────────
def process_video():
    global processing_active, current_stats, crowd_data_history

    try:
        cap = cv2.VideoCapture(VIDEO_SOURCE)

        if not cap.isOpened():
            current_stats['processing_status'] = 'error'
            print("❌ Cannot open video")
            return

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = cap.get(cv2.CAP_PROP_FPS) or 30

        current_stats.update({
            'total_frames': total_frames,
            'processing_status': 'running',
            'start_time': datetime.now().isoformat()
        })

        frame_id = 0
        start_time = time.time()

        print("🔥 Backend using YOLOv8 + tiling")

        while processing_active and cap.isOpened():

            ret, frame = cap.read()
            if not ret:
                break

            frame_id += 1

            # 🔥 Skip frames for speed
            if frame_id % 5 != 0:
                continue

            frame = cv2.resize(frame, (1280, 720))

            # 🔥 REAL DETECTION
            boxes = detect_with_tiling(frame)
            crowd_count = len(boxes)

            # 🔥 Update stats
            current_stats.update({
                'crowd_count': crowd_count,
                'frames_processed': frame_id,
                'current_frame': frame_id,
                'restricted_entry': crowd_count > 50,
                'abnormal_activity': crowd_count > 70
            })

            # 🔥 FPS
            elapsed = time.time() - start_time
            if elapsed > 0:
                current_stats['processing_fps'] = frame_id / elapsed

            # 🔥 Store data for frontend
            current_time = datetime.now().strftime("%H:%M:%S")

            crowd_data_history.append({
                'time': current_time,
                'human_count': crowd_count,
                'restricted_entry': current_stats['restricted_entry'],
                'abnormal_activity': current_stats['abnormal_activity']
            })

            # Limit memory
            if len(crowd_data_history) > 200:
                crowd_data_history.pop(0)

        cap.release()
        current_stats['processing_status'] = 'completed'
        print("✅ Processing finished")

    except Exception as e:
        current_stats['processing_status'] = 'error'
        print("❌ Error:", e)


# ─────────────────────────────────────────────
# API ROUTES
# ─────────────────────────────────────────────

@app.route('/')
def home():
    return jsonify({
        'message': 'Crowd Detection Backend Running 🚀',
        'video_source': VIDEO_SOURCE
    })


@app.route('/stats')
def get_stats():
    return jsonify(current_stats)


@app.route('/crowd_data')
def get_crowd_data():
    return jsonify({
        'data': crowd_data_history
    })


@app.route('/start_processing', methods=['POST'])
def start_processing():
    global processing_active, processing_thread

    if processing_active:
        return jsonify({'status': 'already running'})

    processing_active = True

    # Reset stats
    current_stats.update({
        'crowd_count': 0,
        'frames_processed': 0,
        'current_frame': 0,
        'processing_status': 'starting'
    })

    processing_thread = threading.Thread(target=process_video, daemon=True)
    processing_thread.start()

    return jsonify({'status': 'started'})


@app.route('/stop_processing', methods=['POST'])
def stop_processing():
    global processing_active

    processing_active = False
    current_stats['processing_status'] = 'stopped'

    return jsonify({'status': 'stopped'})


@app.route('/system_status')
def system_status():
    return jsonify({
        'processing_active': processing_active,
        'current_stats': current_stats,
        'data_points': len(crowd_data_history)
    })


# ─────────────────────────────────────────────
# RUN SERVER
# ─────────────────────────────────────────────
if __name__ == '__main__':
    print("🚀 Backend started")
    print(f"📹 Video Source: {VIDEO_SOURCE}")
    print("🌐 http://localhost:5000")

    app.run(host='0.0.0.0', port=5000, debug=True)