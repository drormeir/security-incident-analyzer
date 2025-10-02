#!/usr/bin/env python3
"""Download required models for the project"""

from pathlib import Path
from ultralytics import YOLO

def download_yolo_models():
    """Download YOLO models based on config tier"""
    models_dir = Path(__file__).parent / "yolo"
    models_dir.mkdir(exist_ok=True)
    
    print("Downloading YOLO nano model...")
    model = YOLO("yolov8n.pt")
    print("yolov8n.pt ready")

def main():
    print("Setting up models...")
    download_yolo_models()
    print("Model setup complete!")
    print("\nNext: Install Ollama and run 'ollama pull tinyllama:1.1b'")

if __name__ == "__main__":
    main()

