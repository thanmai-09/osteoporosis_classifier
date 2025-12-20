# Osteoporosis Classifier (Flask)

A simple web application for uploading medical images (e.g., X-rays) and displaying a classification result for osteoporosis. The current version uses a placeholder result; you can plug in your ML model to provide real predictions.

## Features
- Upload a single image and view a result
- Allowed image types: `png`, `jpg`, `jpeg`, `gif`, `bmp`
- Simple pages: Home, Read Me, Results
- Automatic creation of an `uploads/` folder

## Project Structure
```
osteoporosis_classifier/
├── app.py
├── datasets/
│   ├── MedicalExperti-I.zip
│   └── MedicalExperti-II (1).zip
├── static/
│   └── styles.css
└── templates/
    ├── index.html
    ├── read_me.html
    └── results.html
```

## Prerequisites
- Python 3.8+
- pip

## Quick Start
1. (Optional) create and activate a virtual environment:
   - Windows (PowerShell):
     - `python -m venv .venv`
     - `.\.venv\Scripts\Activate.ps1`
2. Install dependencies:
   - `pip install flask`
3. Run the app:
   - `python app.py`
4. Open the app in a browser:
   - `http://localhost:5000/`

## Usage
- Go to `Home`
- Use the file picker to upload an image
- Click `Upload & Analyze` to see the result
- Visit `Read Me` from the navbar for in-app instructions

Uploaded files are saved to `uploads/` (created automatically next to `app.py`).

## Integrating Your Model
The app currently returns a placeholder result in `app.py`:
```python
# Placeholder
prediction_result = "Normal / Osteoporotic"
```
Replace that section with your model inference code. A minimal example outline:
```python
# 1) Load your model once at startup
# model = load_model('path/to/model')

# 2) In the /result route, after saving the uploaded file
# image = preprocess_image(file_path)
# prediction = model.predict(image)
# prediction_result = decode_prediction(prediction)
```
Tips:
- If you use PyTorch or TensorFlow, add the required packages to your environment and import them at the top of `app.py`.
- Make sure your preprocessing matches the model’s training pipeline.
- Consider returning confidence scores and class labels.

## Datasets Note
`datasets/` contains zip archives (e.g., MedicalExperti). These are not automatically used by the app. If you want to extract or train from them, add your own data processing script or integrate it into your training workflow.

## Configuration
- Upload folder: created at `uploads/` on app start
- Allowed extensions: defined in `ALLOWED_EXTENSIONS` in `app.py`
- Server defaults: debug mode, `host='0.0.0.0'`, `port=5000`

## Security Considerations
- The app restricts uploads by file extension only. For production, add stronger validation (MIME type checks, file size limits, antivirus scans).
- Disable debug mode and run behind a proper web server when deploying.

## Troubleshooting
- If Flask is not found, install it: `pip install flask`
- If the server doesn’t start, check Python version and that port 5000 is free
- If uploads fail, verify file type matches allowed extensions and that `uploads/` is writable

## License
No license specified. Add one if you plan to distribute.