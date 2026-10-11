# websocket_server.py
import asyncio
import websockets
import json
import cv2
import base64
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

async def video_stream(websocket, path):
    camera = cv2.VideoCapture(0)
    
    try:
        while True:
            success, frame = camera.read()
            if not success:
                break
            
            # Process frame with YOLOv8
            processed_frame, stats = model.process_frame(frame)
            
            # Encode frame to base64
            _, buffer = cv2.imencode('.jpg', processed_frame)
            frame_base64 = base64.b64encode(buffer).decode('utf-8')
            
            # Send frame and stats
            message = {
                'frame': frame_base64,
                'stats': stats
            }
            
            await websocket.send(json.dumps(message))
            await asyncio.sleep(0.03)  # ~30 FPS
            
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        camera.release()

start_server = websockets.serve(video_stream, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()