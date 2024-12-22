from flask import Flask, request, render_template, send_file
import os
import cv2
from ultralytics import YOLO
import uuid

# Initialize Flask app
app = Flask(__name__)

# Folder to save uploaded and processed videos
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

# Load YOLO model
MODEL_PATH = 'custom_yolov8s_cctvV4.pt'
model = YOLO(MODEL_PATH)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return "No video file provided", 400

    video_file = request.files['video']
    if video_file.filename == '':
        return "No selected file", 400

    # Save the uploaded video
    video_path = os.path.join(UPLOAD_FOLDER, video_file.filename)
    video_file.save(video_path)

    # Process the video
    processed_video_path = process_video(video_path)

    return send_file(processed_video_path, as_attachment=True)

def process_video(video_path):
    """Run inference on the video and save the processed video."""
    # Capture video
    cap = cv2.VideoCapture(video_path)
    
    # Get video properties
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Output video path
    output_filename = f"processed_{uuid.uuid4().hex}.mp4"
    output_path = os.path.join(PROCESSED_FOLDER, output_filename)

    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO inference
        results = model(frame)

        # Render results on the frame
        rendered_frame = results[0].plot()

        # Write the frame to the output video
        out.write(rendered_frame)

    # Release resources
    cap.release()
    out.release()

    return output_path

if __name__ == '__main__':
    app.run(debug=True)
