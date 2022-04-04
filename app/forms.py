from tkinter.messagebox import CANCEL
from flask_wtf import FlaskForm 
from wtforms import StringField,TextAreaField,SubmitField,IntegerField
from wtforms.validators import InputRequired

class tracker_form(FlaskForm):
    tracker_name = StringField('Tracker',validators=[InputRequired()])
    comment = TextAreaField('Comment',validators=[InputRequired()])
    rate = IntegerField('Rate value', validators=[InputRequired()])
    submit = SubmitField('Submit')

class logForm(FlaskForm):
    name = StringField('Log',validators=[InputRequired()])
    comment = TextAreaField('Comment',validators=[InputRequired()])
    rate = IntegerField('Rate value', validators=[InputRequired()])
    submit = SubmitField('Submit')