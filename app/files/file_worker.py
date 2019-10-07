import os
from app import app
from werkzeug.utils import secure_filename


class FileWorker:
    @staticmethod
    def create_upload_folder():
        upload_folder = app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)

    @staticmethod
    def save_upload_files(files):
        for file_key in files:
            file = files[file_key]
            filename = secure_filename(file.filename)
            if filename == '' or filename is None:
                continue
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))