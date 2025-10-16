
from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# 👇 Place this block right after initializing app
UPLOAD_PATH = os.path.join(app.root_path, 'uploads')
os.makedirs(UPLOAD_PATH, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

# You can specify allowed extensions for security purposes
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

print(f"Uploads folder path: {UPLOAD_PATH}")

# Your routes start below
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read_me')
def read_me():
    return render_template('read_me.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(file_path)
            
            # Here you'd add your model prediction code
            prediction_result = "Normal / Osteoporotic"  # Placeholder
            return render_template('result.html', result=prediction_result)
        else:
            return "File type not allowed. Please upload an image file.", 400
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
'''
from flask import Flask, render_template, request, redirect, url_for
import os
import zipfile
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set up upload path
UPLOAD_PATH = os.path.join(app.root_path, 'uploads')
os.makedirs(UPLOAD_PATH, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH

# Set up allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

print(f"Uploads folder path: {UPLOAD_PATH}")

# ✅ Unzip function to extract dataset zip files into dataset/images/
def unzip_dataset():
    zip_files = ['dataset/your_first_zip.zip', 'dataset/your_second_zip.zip']  # 🔁 Change to your actual zip names
    extract_to = 'dataset/images/'
    os.makedirs(extract_to, exist_ok=True)

    for zip_path in zip_files:
        if os.path.exists(zip_path):
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                print(f"Extracting {zip_path}...")
                zip_ref.extractall(extract_to)
        else:
            print(f"{zip_path} not found. Skipping.")

# Call unzip function once when the app starts
unzip_dataset()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/read_me')
def read_me():
    return render_template('read_me.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(file_path)

            # Placeholder for model prediction
            prediction_result = "Normal / Osteoporotic"
            return render_template('result.html', result=prediction_result)
        else:
            return "File type not allowed. Please upload an image file.", 400
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
'''