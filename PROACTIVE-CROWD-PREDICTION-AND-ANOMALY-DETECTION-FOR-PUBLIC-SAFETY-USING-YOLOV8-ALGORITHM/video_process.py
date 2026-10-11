import cv2
import time
from ultralytics import YOLO
from collections import deque
from config import SHOW_PROCESSING_OUTPUT, SAMPLE_EVERY_N_FRAMES

# ⚡ Use medium model (much faster)
model = YOLO("yolov8m.pt")

# 🔥 REMOVE DUPLICATES (VERY IMPORTANT)
def remove_duplicates(boxes, iou_thresh=0.5):
    final_boxes = []

    for box in boxes:
        keep = True
        x1, y1, x2, y2 = box

        for fb in final_boxes:
            fx1, fy1, fx2, fy2 = fb

            # IoU calculation
            inter_x1 = max(x1, fx1)
            inter_y1 = max(y1, fy1)
            inter_x2 = min(x2, fx2)
            inter_y2 = min(y2, fy2)

            inter_area = max(0, inter_x2 - inter_x1) * max(0, inter_y2 - inter_y1)
            area1 = (x2 - x1) * (y2 - y1)
            area2 = (fx2 - fx1) * (fy2 - fy1)

            union = area1 + area2 - inter_area

            if union > 0 and (inter_area / union) > iou_thresh:
                keep = False
                break

        if keep:
            final_boxes.append(box)

    return final_boxes


def detect_with_tiling(frame, tile_size=800):
    

    h, w, _ = frame.shape
    detections_all = []

    for y in range(0, h, tile_size):
        for x in range(0, w, tile_size):

            tile = frame[y:y+tile_size, x:x+tile_size]

            if tile.shape[0] == 0 or tile.shape[1] == 0:
                continue

            results = model(tile, conf=0.05, iou=0.8, imgsz=640)

            for box in results[0].boxes:
                if int(box.cls[0]) == 0:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    detections_all.append([
                        x1 + x,
                        y1 + y,
                        x2 + x,
                        y2 + y
                    ])

    # 🔥 REMOVE DUPLICATES
    return remove_duplicates(detections_all)


def video_process(cap, frame_size, crowd_data_writer=None):

    crowd_buffer = deque(maxlen=10)
    frame_id = 0

    print("Processing started...")

    frame_id = 0
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    while True:
        ret, frame = cap.read()

        if not ret or frame_id >= total_frames:
           print("Video finished properly ✅")
           break

           frame_id += 1

        # 🔥 SKIP FRAMES → HUGE SPEED BOOST
        if frame_id % SAMPLE_EVERY_N_FRAMES != 0:
            continue

        frame = cv2.resize(frame, (1280, 720))

        # 🔥 DETECT
        boxes = detect_with_tiling(frame)

        count = len(boxes)

        # 🔥 SMOOTH COUNT
        crowd_buffer.append(count)
        stable_count = int(sum(crowd_buffer) / len(crowd_buffer))

        # 🔥 SAVE DATA (FIXED)
        if crowd_data_writer:
            timestamp = int(time.time())
            crowd_data_writer.writerow([
                timestamp,
                stable_count,
                0,
                0,
                0
            ])

        # 🔥 DRAW (ONLY IF ENABLED)
        if SHOW_PROCESSING_OUTPUT:
            for (x1, y1, x2, y2) in boxes:
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

            cv2.putText(frame, f"Crowd Count: {stable_count}", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            cv2.imshow("Improved Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

    print("Processing complete.")