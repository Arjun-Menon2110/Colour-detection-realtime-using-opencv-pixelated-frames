import cv2
import numpy as np

# Function to classify color based on HSV ranges (detailed classification)
def detect_color(h, s, v):
    if s < 40 and v > 200:
        return "White"
    if v < 50:
        return "Black"
    if 0 <= h <= 10 or h >= 170:
        return "Red"
    if 10 < h <= 25:
        return "Orange"
    if 25 < h <= 35:
        return "Yellow"
    if 35 < h <= 85:
        return "Green"
    if 85 < h <= 100:
        return "Cyan"
    if 100 < h <= 125:
        return "Blue"
    if 125 < h <= 145:
        return "Purple"
    if 145 < h <= 160:
        return "Magenta"
    if 160 < h <= 170:
        return "Pink"
    return "Undefined Color"

# Start video capture (webcam feed)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Get the center pixel of the frame
    height, width, _ = frame.shape
    center_x, center_y = width // 2, height // 2

    # Convert the frame from BGR to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the HSV value of the center pixel
    h, s, v = hsv_frame[center_y, center_x]

    # Detect color based on the HSV values
    color_name = detect_color(h, s, v)

    # Display a circle at the center and show detected color
    cv2.circle(frame, (center_x, center_y), 5, (255, 255, 255), 2)
    cv2.putText(frame, f'Color: {color_name}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Full-Range Color Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()






