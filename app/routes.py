from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import UploadForm
from app.files.file_worker import FileWorker


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vania Maksymiv'}
    return render_template('index.html', title='Upload your files', user=user)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        FileWorker.create_upload_folder()
        FileWorker.save_upload_files(request.files)

        flash('Uploaded files: template - {}, names - {}{}'.format(
            form.badge_template.name,
            form.names_excel.name,
            ', font - ' + form.font.name if form.font is None else ''))
        return redirect(url_for('index'))
    return render_template('upload.html', title='Upload your files', form=form)