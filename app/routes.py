from flask import render_template, flash, redirect, url_for, request, send_from_directory
from app import app
from app.forms import UploadForm
from app.files.file_worker import FileWorker
from app.excel.excel_worker import ExcelWorker


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
        return redirect(url_for('review'))
    return render_template('upload.html', title='Upload your files', form=form)


@app.route('/review', methods=['GET', 'POST'])
def review():
    files = FileWorker.get_uploaded_files()
    return render_template('review.html', title='Review your uploads', files=files,
                           upload_dir=app.config['UPLOAD_FOLDER'], get_excel_content=ExcelWorker.get_excel_content)


@app.route('/preview_pdf/<path:pdf_name>', methods=['GET', 'POST'])
def preview_pdf(pdf_name):
    return send_from_directory(app.config['UPLOAD_FOLDER_REL'], pdf_name)
