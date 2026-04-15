# 👁️ Real-Time Object Detector

A simple and powerful tool that uses your computer's camera to "see" and identify objects in real-time! Whether it's a person, a cell phone, or a coffee mug, this app will spot it and count it for you.

## ✨ What does it do?
- **Real-time Recognition**: Instantly identifies objects through your webcam.
- **Smart Counting**: Keeps a live tally of every object it sees on the screen.
- **Color-Coded Labels**: Different objects get different colors, making it easy to track multiple things at once.
- **High Performance**: Uses state-of-the-art AI technology to run smoothly on most computers.

## 🚀 How to Get Started

### 1. Requirements
Before you begin, make sure you have:
- A computer with a webcam.
- [Python](https://www.python.org/downloads/) installed.

### 2. Setup (The "One-Time" Part)
Open your terminal or command prompt in this folder and run these commands one by one:

```bash
# Create a virtual environment (keeps things tidy)
python -m venv obj_env

# Activate the environment
# On Windows:
obj_env\Scripts\activate
# On Mac/Linux:
source obj_env/bin/activate

# Install the necessary "brains" for the detector
pip install ultralytics opencv-python "numpy<2"
```

### 3. Run the Detector
Whenever you want to start the detector, just run:

```bash
python detect.py
```

## 🎮 How to Use
1. Once the window opens, point your webcam at different objects.
2. You will see colored boxes appear around objects with their names (like "Person", "Bottle", etc.).
3. Look at the **top-right corner** to see a live count of everything the AI is currently seeing.
4. **To Exit**: Simply press the **'Q'** key on your keyboard or close the window.

## 🛠️ Tech Details (For the Curious)
This project uses **YOLOv8** (You Only Look Once), a famous AI model for image recognition, and **OpenCV** for handling the video feed. It's designed to be fast, accurate, and fun to use!

---
*Made with ❤️ for exploring AI.*
