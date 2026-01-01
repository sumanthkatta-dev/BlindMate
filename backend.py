from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
import cv2
import numpy as np
import math

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for local testing, allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load YOLO model
model = YOLO("yolov8n.pt")  # replace with your trained model

# Define risk categories
high_risk_labels = {"car", "bus", "truck", "motorbike", "bicycle"}
medium_risk_labels = {"person", "dog", "cat", "horse", "cow", "sheep"}

prev_positions = {}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    global prev_positions

    # Read image from frontend
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    frame_h, frame_w, _ = frame.shape

    results = model(frame)

    high_risk_list, medium_risk_list, low_risk_list = [], [], []
    current_positions = {}

    for r in results:
        for i, box in enumerate(r.boxes):
            x1, y1, x2, y2 = box.xyxy[0]
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]

            obj_center = ((x1 + x2) / 2, (y1 + y2) / 2)
            obj_id = f"{label}_{i}"
            current_positions[obj_id] = obj_center

            # Direction
            if obj_center[0] < frame_w * 0.33:
                direction = "slightly left"
            elif obj_center[0] > frame_w * 0.66:
                direction = "slightly right"
            else:
                direction = "straight ahead"

            # Distance approximation
            box_h = (y2 - y1)
            if box_h > frame_h * 0.6:
                distance = "1 meter"
            elif box_h > frame_h * 0.3:
                distance = "about 2 meters"
            else:
                distance = "more than 3 meters"

            # Risk assessment
            risk = "Low risk"
            if label in high_risk_labels:
                risk = "High risk"
            elif label in medium_risk_labels:
                risk = "Medium risk"

            # Movement detection
            if obj_id in prev_positions:
                dx = obj_center[0] - prev_positions[obj_id][0]
                dy = obj_center[1] - prev_positions[obj_id][1]
                movement = math.sqrt(dx**2 + dy**2)
                if movement > 15:
                    risk = "High risk (moving)"

            msg = {
                "label": label,
                "confidence": conf,
                "bbox": [float(x1), float(y1), float(x2), float(y2)],
                "direction": direction,
                "distance": distance,
                "risk": risk
            }

            if "High" in risk:
                high_risk_list.append(msg)
            elif "Medium" in risk:
                medium_risk_list.append(msg)
            else:
                low_risk_list.append(msg)

    prev_positions = current_positions

    # Return prioritized detections
    all_detections = high_risk_list + medium_risk_list + low_risk_list
    return JSONResponse(content={"detections": all_detections})