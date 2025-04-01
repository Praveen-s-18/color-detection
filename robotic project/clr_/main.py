import cv2
import numpy as np
from utils import get_limits

# Define colors to detect
colors = {
    "red": ["red1", "red2"],
    "blue": ["blue"],
    "green": ["green"],
    "yellow": ["yellow"]
}

cap = cv2.VideoCapture(0)  # Use 0 for default webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, hsv_keys in colors.items():
        mask = np.zeros_like(hsvImage[:, :, 0])

        for key in hsv_keys:
            lowerLimit, upperLimit = get_limits(key)
            mask += cv2.inRange(hsvImage, lowerLimit, upperLimit)

        # Morphological filtering (removes noise)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

        # Find contours for each color
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Filter out small detections
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, color_name, 
                            (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
