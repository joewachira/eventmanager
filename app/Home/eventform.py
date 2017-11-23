__author__ = 'joe'

from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired


class EventsList(FlaskForm):

	# form for users to input events

	title = wtforms.StringField('Category', validators=[DataRequired])
	event = wtforms.StringField('Name', validators=[DataRequired])
	location = wtforms.StringField('Location', validators=[DataRequired])
	date = wtforms.DateField('Date', validators=[DataRequired])
	submit = wtforms.SubmitField('add')