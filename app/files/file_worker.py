import os
from os import listdir
from os.path import isfile, join
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

    @staticmethod
    def get_uploaded_files():
        upload_folder = app.config['UPLOAD_FOLDER']
        files_content = dict()
        files = [f for f in listdir(upload_folder) if isfile(join(upload_folder, f))]
        for file in files:
            with open(upload_folder + '\\' + file, 'rb') as content_file:
                files_content[file] = content_file.read()
        return files_content
