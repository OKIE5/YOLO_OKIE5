# webcam_min_cam5.py
import cv2

CAMERA_INDEX = 5 # 0 for default camera, change as needed

cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    raise RuntimeError(f"Could not open camera index {CAMERA_INDEX}")

while True:
    ok, frame = cap.read()
    if not ok:
        break
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()