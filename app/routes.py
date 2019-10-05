from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Vania Maksymiv'}
    return render_template('index.html', title='Upload your files', user=user)