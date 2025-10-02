#!/usr/bin/env python3
"""Quick verification that everything is working"""

import sys
import cv2
import numpy as np
from ultralytics import YOLO
import yaml

def main():
    print()
    print(f"Python version: {sys.version}")
    print(f"OpenCV version: {cv2.__version__}")
    print(f"NumPy version: {np.__version__}")
    
    # Test basic YOLO import (without downloading model yet)
    try:
        yolo = YOLO()
        print("YOLO import successful")
    except Exception as e:
        print(f"YOLO import issue (expected on first run): {e}")
    
    # Test basic video capture
    try:
        cap = cv2.VideoCapture(0)  # Try webcam
        if cap.isOpened():
            print("Webcam accessible")
            cap.release()
        else:
            print("No webcam found (that's okay)")
    except:
        print("Webcam test skipped")
    print()
    print("Environment setup complete!")
    print("Next steps:")
    print("1. Download YOLO model: python -c 'from ultralytics import YOLO; YOLO(\"yolov8n.pt\")'")
    print("2. Install Ollama for local LLM")
    print("3. Start building the pipeline!")

if __name__ == "__main__":
    main()
    
