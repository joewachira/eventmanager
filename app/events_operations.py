__author__ = 'joe'

from app.randomID import get_random_id
from app.events_declare import Items


class Events(object):
	def __init__(self):

		self.id = get_random_id()
		self.items = []
		self.category = category()

	def add_event(self, event_name):

		if event_name is None or len(event_name) < 1:
			return "event must have a name"

		if not isinstance(event_name, str):
			return "Event must be a string"

		for item in self.items:
			if item.name == event_name:
				return event_name + "already exists"

		new_item = Items(event_name)
		self.items.append(event_name)

		return new_item.id

	def update(self, new_event, new_category=None):

		if new_category
