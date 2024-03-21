from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ChatbotForm(FlaskForm):
    user_input = StringField('User Input')
    submit = SubmitField('Send')
