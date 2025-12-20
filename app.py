
from flask import Flask, render_template, request, redirect, url_for, flash
import os
from PIL import Image
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret')

# 👇 Place this block right after initializing app
UPLOAD_PATH = os.path.join(app.root_path, 'uploads')
os.makedirs(UPLOAD_PATH, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_PATH
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB

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

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part in the request. Please choose a file.')
            return redirect(url_for('index'))
        uploaded_file = request.files['file']
        if not uploaded_file or uploaded_file.filename == '':
            flash('No file selected. Please choose an image file to upload.')
            return redirect(url_for('index'))
        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(file_path)
            # Verify the image content (not just extension)
            try:
                with Image.open(file_path) as img:
                    img.verify()
            except Exception:
                # Remove invalid file and return an error
                try:
                    os.remove(file_path)
                except OSError:
                    pass
                flash('Invalid image file. Please upload a valid image.')
                return redirect(url_for('index'))
            
            # Here you'd add your model prediction code
            prediction_result = "Normal / Osteoporotic"  # Placeholder
            return render_template('results.html', result=prediction_result)
        else:
            flash('File type not allowed. Allowed: png, jpg, jpeg, gif, bmp. Max size 5 MB.')
            return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.errorhandler(413)
def request_entity_too_large(e):
    flash('File too large. Maximum allowed size is 5 MB.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)