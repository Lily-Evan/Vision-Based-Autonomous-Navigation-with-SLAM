import cv2
import numpy as np
from robot_control import DummyRobot

def detect_line(frame):
    # Convert to grayscale and blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    # Threshold to get binary image
    _, thresh = cv2.threshold(blur, 130, 255, cv2.THRESH_BINARY_INV)
    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        # Find largest contour, assume it's the line
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] > 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            return (cx, cy), contours
    return None, contours

def main():
    cap = cv2.VideoCapture(0)
    robot = DummyRobot()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        (cx, cy), contours = None, []
        line_center, contours = detect_line(frame)
        if line_center:
            cx, cy = line_center
            # Draw center point
            cv2.circle(frame, (cx, cy), 8, (0, 255, 0), -1)
            # Robot navigation logic
            frame_center = frame.shape[1] // 2
            error = cx - frame_center
            if abs(error) < 30:
                robot.forward()
            elif error < 0:
                robot.turn_left()
            else:
                robot.turn_right()
        else:
            robot.stop()

        # Draw contours
        cv2.drawContours(frame, contours, -1, (255, 0, 0), 2)
        cv2.imshow('Line Follower', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()