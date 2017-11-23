__author__ = 'joe'
from flask import render_template, redirect, url_for, flash, session
from app.events_operations import EventsManager
from .eventform import EventsList
from app.event_misc import EventMisc
from . import home

# routes /endpoints


@home.route('/h')
def homepage():
	return redirect(url_for('auth.login'))  # render the homepage template on the / route
	return render_template('dashboard.html', title='Welcome')


@home.route('', methods=['POST', 'GET'])
def new_event():
	form = EventsList()
	if form.validate_on_submit():
		# create a new event
		event_misc = EventMisc(form.title.data, session['username'])
		new_event_misc = EventsManager().add_event(session['username'])
		flash('Event is saved')
		return render_template('dashboard.html', title='Dashboard', new_event=new_event)

	return render_template('', form=form, title='Add new event')


@home.route('/update/event-list/<_ids>', methods=['POST', 'GET'])
def update_event(_ids):
	ids = int(_ids)
	EventsList = EventsManager().get_event_list(ids)
	form_object = EventsList

	form = EventsList(oct=form_object)
	if form.validate_on_submit():
		form.populate_obj(form_object)
		return redirect(url_for('dashboard'))
	return render_template('/', form=form, title='update')

