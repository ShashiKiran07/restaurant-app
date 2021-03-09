from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField,IntegerField
from wtforms.validators import DataRequired

class OrderForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[DataRequired()])
    dish_id = IntegerField('Dish ID', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Order')