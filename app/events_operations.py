__author__ = 'joe'


class Events(object):
	events = {}

	def add_event(self, key, value):
		if isinstance(key, str):
			self.events.setdefault(key, [] .append(value))
			return self.events
		else:
			raise ValueError

	# def update(self, new_event, new_category=None):