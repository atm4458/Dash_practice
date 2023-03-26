from flask_wtf import FlaskForm
from wtforms import StringField, MultipleFileField, SubmitField
from wtforms.validators import DataRequired

class InitForm(FlaskForm):
    user = StringField("User", validators=[DataRequired()])
    project = StringField("Project name", validators=[DataRequired()])
    files = MultipleFileField("Pickles Upload", render_kw={"accept": ".pickle"})
    submit = SubmitField()