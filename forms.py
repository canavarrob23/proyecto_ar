from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError


class frm_producto(FlaskForm):
    """ REVISASAR DOCUMENTACION DE Flask-WTF y WTForms """
    """Formulario para el CRUD de productos"""
    codiprod = StringField('Produto', validators=[DataRequired(), Length(min=2, max=20)])
    descprod = StringField('Descripcion', validators=[DataRequired(), Length(min=2, max=100)])
    precprod = StringField('Precio', validators=[DataRequired()])
    cantstoc = StringField('Stock', validators=[DataRequired()])
    submit = SubmitField('Enviar')

