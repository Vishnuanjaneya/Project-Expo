import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img

def draw_lines(img, lines, color=(0, 0, 255), thickness=3):
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

cap = cv2.VideoCapture(0)  # Open the webcam (0 is typically the default camera)
cap.set(3, 1280)
cap.set(4, 720)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Define a region of interest (ROI) where the lane lines are expected
    height, width = frame.shape[:2]
    roi_vertices = [(0, height), (width / 2, height / 2), (width, height)]
    roi = region_of_interest(edges, np.array([roi_vertices], np.int32))

    # Apply Hough Line Transform to detect lines in the ROI
    lines = cv2.HoughLinesP(roi, 1, np.pi / 180, threshold=50, minLineLength=50, maxLineGap=30)

    if lines is not None:
        # Draw the detected lane lines on the frame
        draw_lines(frame, lines)

    # Display the resulting frame
    cv2.imshow('Lane Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
