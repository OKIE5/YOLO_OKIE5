# webcam_yolo.py  (Jetson-friendly: V4L2 backend)
import cv2
from ultralytics import YOLO

CAMERA_INDEX = 0

def main():
    model = YOLO("yolo11n.pt")

    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_V4L2)
    if not cap.isOpened():
        cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera index {CAMERA_INDEX}")

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    print("Press 'q' to quit.")
    while True:
        ok, frame = cap.read()
        if not ok:
            print("Frame read failed.")
            break

        results = model.predict(source=frame, conf=0.25, verbose=False)
        annotated = results[0].plot()
        cv2.imshow("YOLO USB Camera", annotated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
