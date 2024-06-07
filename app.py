from flask import Flask, request, render_template, redirect, url_for
from model import predict
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        prediction = predict(file_path)
        os.remove(file_path)  # Clean up the uploaded file after prediction
        return render_template('result.html', prediction=prediction)
    return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)
