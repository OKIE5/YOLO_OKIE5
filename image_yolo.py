# image_yolo_save_same_dir.py
from pathlib import Path
import cv2
from ultralytics import YOLO

WEIGHTS = r"C:\Users\jpenv\Documents\scripts\YOLO\ultralytics\weights\yolo11l.pt"
SRC_IMG = r"C:\Users\jpenv\Documents\scripts\YOLO\YOLO\gptHollowween.png"


model = YOLO(WEIGHTS)
results = model(SRC_IMG)

annotated = results[0].plot()

src = Path(SRC_IMG)
out_path = src.with_stem(src.stem + "_yolo")
cv2.imwrite(str(out_path), annotated)

print(f"Saved: {out_path}")
