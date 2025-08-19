# Vision-Based-Autonomous-Navigation-with-SLAM
# Vision-Based Autonomous Navigation with SLAM

## Overview

This project develops a vision-based navigation system for mobile robots. The robot uses a camera to follow a line or path, and integrates Simultaneous Localization and Mapping (SLAM) to map its environment and localize itself in real time. This approach enables autonomous movement in environments where GPS is unavailable or unreliable.

## Expected Outcomes

- Line/path detection for vision-based navigation
- Integration of SLAM for mapping and localization
- Demo of autonomous movement in a GPS-denied environment

## Structure

```
.
├── line_follower.py           # Line/path detection and navigation logic
├── slam_runner.py             # SLAM integration and map/localization
├── robot_control.py           # Robot movement interface (simulation or hardware)
├── requirements.txt
└── README.md
```

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the line follower:
    ```bash
    python line_follower.py
    ```

3. Run SLAM integration (example with RTAB-Map or ORB-SLAM2 required):
    ```bash
    python slam_runner.py
    ```

## Notes

- The code uses OpenCV for computer vision and [RTAB-Map](https://introlab.github.io/rtabmap/) or [ORB-SLAM2](https://github.com/raulmur/ORB_SLAM2) for SLAM (external setup may be needed for full SLAM integration).
- The robot control interface is kept abstract for easy adaptation to simulation or real robots.
