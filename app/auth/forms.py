from flask.ext.wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, length

__author__ = 'joe'


class RegistrationForm(FlaskForm):
	# Form for users to create new account

	email = StringField('Email', validators=[DataRequired(), Email])
	username = StringField('Username', validators=[DataRequired, Email])
	password = PasswordField('Password', validators=[
		DataRequired(),
		EqualTo('confirm_password', message='password mismatch'),
		length(min=7)])
	submit = SubmitField('Register')


class LoginForm(FlaskForm):
	# form for users to login

	email = StringField('Email', validators=[DataRequired, Email()])
	password = PasswordField('Password', validators=[DataRequired])
	submit = SubmitField('Login')
