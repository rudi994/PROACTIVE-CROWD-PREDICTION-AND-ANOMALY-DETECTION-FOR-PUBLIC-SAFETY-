# yolo_model.py
from ultralytics import YOLO
import cv2

class YOLOModel:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)

    def process_frame(self, frame):
        # Run YOLOv8 inference on the frame
        results = self.model(frame)

        # Extract detections
        detections = []  # List of detections, each detection is (x1, y1, x2, y2, confidence, class_id)
        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                confidence = box.conf[0].cpu().numpy()
                class_id = box.cls[0].cpu().numpy()
                detections.append((x1, y1, x2, y2, confidence, class_id))

        # Annotate the frame with detections
        annotated_frame = results[0].plot()

        return annotated_frame, detections

    def count_violations(self, detections):
        # This is a placeholder for violation logic.
        # The user should implement their own violation counting logic.
        # For example, counting people too close (social distancing) or in restricted areas.
        violation_count = 0
        # ... violation logic ...

        return violation_count