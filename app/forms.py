from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from wtforms.validators import DataRequired


class UploadForm(FlaskForm):
    badge_template = FileField('Badge template', validators=[DataRequired()])
    names_excel = FileField('Names', validators=[DataRequired()])
    font = FileField('Font (optional)')
    submit = SubmitField('Submit')