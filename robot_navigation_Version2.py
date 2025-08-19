import numpy as np

class SimpleNavigator:
    def __init__(self, robot, detector):
        self.robot = robot
        self.detector = detector

    def process_frame(self, frame):
        detections = self.detector.detect(frame)
        # Example: obstacle avoidance logic
        for det in detections:
            if det['label'] in ['person', 'box', 'obstacle']:
                x1, y1, x2, y2 = det['bbox']
                cx = (x1 + x2) // 2
                if cx < frame.shape[1] // 3:
                    self.robot.turn_right()
                elif cx > 2 * frame.shape[1] // 3:
                    self.robot.turn_left()
                else:
                    self.robot.stop()
                return
        self.robot.move_forward()