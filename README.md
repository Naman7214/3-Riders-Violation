# 3 Riders Violation Detection Application

This application processes videos to detect violations (e.g., three riders on a vehicle) using a YOLO model.

## Setup Instructions

### 1. Clone the Repository
To get started, clone the repository to your local machine:
```bash
git clone https://github.com/Naman7214/3-Riders-Violation.git
cd 3-Riders-Violation
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:
```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies
Install the required dependencies using `pip`:
```bash
pip install -r requirements.txt
```

### 4. Run the Application
Start the Flask application by running the following command:
```bash
python app.py
```

By default, the application will run on `http://127.0.0.1:5000/`.

## How to Interact with the Application

### 1. Access the Application
Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

### 2. Upload a Video
- On the home page, you will see an option to upload a video.
- Select a video file (e.g., `.mp4`) and click the **Upload** button.

### 3. Process the Video
- The application will process the uploaded video to detect violations using the YOLO model.
- Once processing is complete, the processed video will be downloaded automatically.

### 4. Output
- The processed video will have bounding boxes and other annotations indicating detected violations.

## Folder Structure
- `uploads/`: Folder where uploaded videos are temporarily stored.
- `processed/`: Folder where processed videos are saved.
- `app.py`: Main application script.
- `requirements.txt`: List of required dependencies.

## Notes
- Ensure the custom YOLO model file (`custom_yolov8s_cctvV4.pt`) is present in the root directory before running the application.
- For issues or contributions, feel free to open an issue or submit a pull request in the [GitHub repository](https://github.com/Naman7214/3-Riders-Violation.git).

## License
This project is licensed under the terms specified in the repository. Please check the LICENSE file for details.

