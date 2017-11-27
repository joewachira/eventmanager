__author__ = 'joe'
from flask import session


class EventsManager(object):
	events = {}

	# def __init__(self):
	def add_event(self, key, value):
		if isinstance(key, str):
			self.events.setdefault(key, [] .append(value))
			return self.events
		else:
			raise ValueError

	# def update(self, new_event, new_category=None):

	def get_event_list(self, event_id):
		if isinstance(event_id, int):
			for all_list in self.events[session['username']]:
				if event_id == all_list.id:
					# the value exists, can fetch
					return all_list
		else:
			raise ValueError

		# self.name = name

	@staticmethod
	def update_event(name):
		if name is None or len(name) < 1:
			return 'Event must have a name'

		if not isinstance(name, str):
			return 'Event must be a string'

	@staticmethod
	def delete_event(name):
		pass