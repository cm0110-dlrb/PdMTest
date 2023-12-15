from flask import Flask, request, render_template_string
import csv
import pandas as pd
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Create an upload folder
if not os.path.exists('uploads'):
    os.makedirs('uploads')

# HTML code to render
html_code = '''
<!DOCTYPE html>
<html>
<head>
    <title>Data Upload</title>
</head>
<body>
    <h1>Upload Your Data</h1>
    <form action="{{ url_for('upload_data') }}" method="POST" enctype="multipart/form-data">
        <input type="file" name="file" required accept=".csv">
        <br>
        <button type="submit">Upload Data</button>
    </form>
</body>
</html>
'''

# Allowed file extensions
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_data():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join('uploads', filename))
            
            # Call your predictive maintenance model here
            # and pass the uploaded CSV file
            
            return 'File uploaded and processed!'
            
    return render_template_string(html_code)

if __name__ == '__main__':
    app.run(debug=True)