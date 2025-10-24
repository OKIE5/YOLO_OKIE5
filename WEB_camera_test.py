import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera")
    exit()

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Can't receive frame")
        break
    
    cv2.imshow('Camera Feed', frame)
    
    # Wait for 'q' key to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()