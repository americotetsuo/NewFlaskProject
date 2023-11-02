from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class OrientacaoForm(FlaskForm):
    pacname = StringField('Nome do Paciente', validators=[DataRequired()])
    paccpf = StringField('CPF do Paciente', validators=[DataRequired()])
    content = TextAreaField('Orientação', validators=[DataRequired()])
    submit = SubmitField('Post')