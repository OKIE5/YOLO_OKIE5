#!/usr/bin/env python3
import sys

# Force use of system OpenCV (which has GStreamer support)
if '/usr/lib/python3/dist-packages' not in sys.path:
    sys.path.insert(0, '/usr/lib/python3/dist-packages')

import cv2
from ultralytics import YOLO
import time

print("OpenCV location:", cv2.__file__)
print("OpenCV version:", cv2.__version__)

# Load YOLO model
print("Loading YOLO model...")
model = YOLO('yolov8n.pt')

# GStreamer pipeline - back to original working settings
gst_pipeline = (
    "nvarguscamerasrc sensor-id=0 ! "
    "video/x-raw(memory:NVMM), width=1280, height=720, framerate=30/1, format=NV12 ! "
    "nvvidconv ! "
    "video/x-raw, format=BGRx ! "
    "videoconvert ! "
    "appsink max-buffers=1 drop=true"
)

cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

if not cap.isOpened():
    print("ERROR: Could not open CSI camera")
    exit()

print("Camera opened successfully!")
print("Warming up camera...")

# Give camera time to initialize and auto-adjust
for i in range(30):
    ret, frame = cap.read()
    if ret and frame is not None:
        print(f"Warmup frame {i+1}: shape={frame.shape}, min={frame.min()}, max={frame.max()}")
    time.sleep(0.1)

print("\nRunning YOLO detection... Press 'q' to quit")

frame_count = 0
skip_frames = 1  # Process every frame (adjust if too slow)

while True:
    ret, frame = cap.read()
    
    if not ret or frame is None:
        print("Error: Can't receive frame")
        break
    
    frame_count += 1
    
    # Check if frame is valid (not all black)
    if frame.mean() < 1:
        print(f"Warning: Frame {frame_count} is black (mean={frame.mean():.2f})")
        cv2.imshow('YOLO Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        continue
    
    # Process frame with YOLO
    if frame_count % skip_frames == 0:
        try:
            results = model(frame, verbose=False, imgsz=640)
            annotated_frame = results[0].plot()
            cv2.imshow('YOLO Detection', annotated_frame)
        except Exception as e:
            print(f"YOLO error: {e}")
            cv2.imshow('YOLO Detection', frame)
    else:
        cv2.imshow('YOLO Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"Processed {frame_count} frames")
