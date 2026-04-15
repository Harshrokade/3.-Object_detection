import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # downloads automatically on first run (~6MB)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# COCO class colors (consistent color per class)
import random
random.seed(42)
COLORS = {i: [random.randint(50, 255) for _ in range(3)] for i in range(80)}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True, conf=0.4, verbose=False)

    object_counts = {}

    for r in results:
        for box in r.boxes:
            # Coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            label = model.names[cls]
            color = COLORS[cls]

            # Count objects
            object_counts[label] = object_counts.get(label, 0) + 1

            # Draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            # Label background
            text = f"{label} {conf:.0%}"
            (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 1)
            cv2.rectangle(frame, (x1, y1 - th - 8), (x1 + tw + 4, y1), color, -1)
            cv2.putText(frame, text, (x1 + 2, y1 - 4),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    # Object count panel (top-right)
    panel_x = frame.shape[1] - 220
    cv2.rectangle(frame, (panel_x - 10, 10), (frame.shape[1] - 10, 30 + len(object_counts) * 24), (20, 20, 20), -1)
    cv2.putText(frame, "Detected", (panel_x, 28),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

    for i, (name, count) in enumerate(object_counts.items()):
        color = COLORS[list(model.names.values()).index(name) if name in model.names.values() else 0]
        cv2.putText(frame, f"{name}: {count}", (panel_x, 52 + i * 24),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 1)

    # FPS counter
    cv2.putText(frame, f"YOLOv8n | Press Q to quit", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

    cv2.imshow("Real-Time Object Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()