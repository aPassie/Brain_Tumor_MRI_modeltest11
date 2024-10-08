from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
from ultralytics import YOLO
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load YOLO model
model_path = "best.pt"  # Adjust path to your model
model = YOLO(model_path)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        # Save the uploaded file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Perform inference using YOLOv8 model
        image = cv2.imread(filepath)
        results = model(image)
        detections = results[0].boxes.xyxy
        confidences = results[0].boxes.conf

        # Draw bounding boxes
        for i, box in enumerate(detections):
            x1, y1, x2, y2 = map(int, box)
            confidence = confidences[i]
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 1)
            cv2.putText(image, f"Acc: {confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 87, 51), 2)

        # Save the processed image
        processed_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'processed_' + file.filename)
        cv2.imwrite(processed_image_path, image)

        return render_template('index.html', uploaded_image=file.filename, processed_image='processed_' + file.filename)

if __name__ == "__main__":
    app.run(debug=True)
