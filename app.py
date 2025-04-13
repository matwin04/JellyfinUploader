from flask import Flask, request, render_template, redirect
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "/media"
ALLOWED_TYPES = ["Movies", "Shows", "Music", "Photos"]

@app.route("/", methods=["GET"])
def index():
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    media_type = request.form.get("type")
    file = request.files.get("media")

    if media_type not in ALLOWED_TYPES or file is None:
        return "Invalid request", 400

    filename = secure_filename(file.filename)
    dest_path = os.path.join(UPLOAD_FOLDER, media_type)
    os.makedirs(dest_path, exist_ok=True)
    file.save(os.path.join(dest_path, filename))

    return f"✅ Uploaded {filename} to {media_type}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8083,debug=True)
