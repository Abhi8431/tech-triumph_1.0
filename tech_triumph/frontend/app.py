from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from fileinput import filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./static/uploads/"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        f = request.files['userPic']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(filename)

        # image is saved

    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)