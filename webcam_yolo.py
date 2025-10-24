# webcam_yolo_cam5.py
import cv2
from ultralytics import YOLO

CAMERA_INDEX = 5

def main():
    model = YOLO("yolo11n.pt")

    # Open the camera
    cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_MSMF)
    if not cap.isOpened():
        cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera index {CAMERA_INDEX}")

    # Quit Operation
    print("Press 'q' to quit.")
    
    while True:
        ok, frame = cap.read()
        if not ok:
            print("Frame read failed.")
            break

        results = model.predict(source=frame, conf=0.25, verbose=False)
        annotated = results[0].plot()
        cv2.imshow("YOLO Camera 5", annotated)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
