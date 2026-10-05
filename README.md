# Assignment 1: Finger Count Detection Using ESP32-CAM

## Overview
This project detects hands and counts the number of extended fingers in real-time using computer vision. The system streams video from an AI Thinker ESP32-CAM module to a Python application utilizing OpenCV and cvzone (built on Google's MediaPipe).

## Project Structure
- `assignment1/finger_counter.py`: Main Python script for hand detection and finger counting.
- `assignment1/demo.png`: Screenshot showing live finger count detection output.
- `README.md`: Setup instructions and project overview.

## Dependencies
Install required Python libraries:
```bash
pip install opencv-python cvzone mediapipe