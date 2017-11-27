__author__ = 'joe'
from .user_operations import UserManager
from .user_class import Userr
from flask import flash, redirect, render_template, url_for, session
from . import auth
from .forms import LoginForm, RegistrationForm
# routes /endpoints


@auth.route("/register", methods=['GET', 'POST'])
def register():
	# Handle requests to the /register route and add new user

	form = RegistrationForm()
	if form.validate_on_submit():
		# import pdb; pdb.set_trace()
		user = Userr(username=form.username.data,
					 email=form.email.data,
					 password=form.password.data, )

		# add new user to list
		is_register_ok = UserManager().register(user.email, user)
		if is_register_ok:
			return redirect(url_for("auth.register"))

		# load the registration template if an error occurred

		return render_template('signup.html', form=form, title='Registration')


@auth.route('/login', methods=['GET', 'POST'])
def login():
	# we now log a user in through the login form

	form = LoginForm
	if form.validate_on_submit():
		is_correct_user = UserManager().login(form.email.data, form.password.data)
		if is_correct_user:
			# we redirect

			session['username'] = form.email.data
			session['logged_in'] = True
			return redirect(url_for('home.dashboard'))
		flash("Sorry, Password or Email entered is incorrect")
		# redirect to the login page
		return redirect(url_for('auth.login'))

	# We load login template

	return render_template('login.html', form=form, title='Login')


@auth.route('logout')
def logout():
	# method for logging out user through the logout link

	session['logged_in'] = None
	flash("You have successfully been logged out.")

	# we now redirect to the login page
	return redirect(url_for('auth.login'))
