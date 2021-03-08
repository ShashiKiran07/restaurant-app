from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField,IntegerField
from wtforms.validators import DataRequired

class TypeForm(FlaskForm):
    user = IntegerField()
    dish = IntegerField()
    submit = SubmitField('Cart')