# image_yolo.py  (Jetson-friendly: POSIX paths, save next to source)
from pathlib import Path
import cv2
from ultralytics import YOLO

ROOT = Path(__file__).resolve().parent
WEIGHTS = ROOT / "ultralytics" / "weights" / "yolo11l.pt"
SRC_IMG = ROOT / "gptHollowween.png"\

model = YOLO(str(WEIGHTS))
results = model(str(SRC_IMG))

annotated = results[0].plot()

out_path = SRC_IMG.with_stem(SRC_IMG.stem + "_yolo")
out_path.parent.mkdir(parents=True, exist_ok=True)
cv2.imwrite(str(out_path), annotated)

print(f"Saved: {out_path}")
