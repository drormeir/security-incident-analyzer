# Security Incident Analyzer

A multi-modal AI pipeline that analyzes security video footage using computer vision and large language models to generate intelligent incident reports.

## Project Overview

This project demonstrates:
- Real-time video analysis using YOLO object detection
- Multi-modal AI combining computer vision with LLM capabilities
- Scalable model architecture (nano → production models)
- Production-ready ML pipeline design

## Quick Start

### Prerequisites
- Python 3.13+
- Ollama (for local LLM)

### Installation
```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/security-incident-analyzer.git
cd security-incident-analyzer

# Create virtual environment
python3.13 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Verify setup
python scripts/verify_setup.py

# Download Models
``` bash
 \# Download lightweight YOLO model (~6MB)
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"

\# Install and setup local LLM
curl -fsSL https://ollama.ai/install.sh | sh
ollama pull tinyllama:1.1b

# Project Structure
security-incident-analyzer/
├── src/                    # Core pipeline modules
├── notebooks/              # Jupyter notebooks for demos
├── models/                 # Model configurations and prompts
├── data/                   # Sample data and outputs
├── scripts/                # Utility scripts
└── tests/                  # Unit tests

# Configuration
The project uses a tiered model system for easy scaling:

Demo tier: Ultra-lightweight models (~650MB total)
Development tier: Balanced performance (~3GB total)
Production tier: High-performance models

Edit config.yaml to switch between tiers.


# Usage
``` bash
\# Run basic pipeline (coming soon)
python scripts/run_pipeline.py --input data/sample_videos/test.mp4

\# Launch Jupyter demo
jupyter notebook notebooks/demo.ipynb


# Development Status

* v Project setup and configuration
* v Model tier architecture
* x Video processing pipeline
* x Object detection integration
* x LLM report generation
* x Web interface
* x Docker deployment
 
# License
MIT License - see LICENSE file for details.

# Contributing
This is a demonstration project for ML engineering interviews. Feel free to explore and extend!


