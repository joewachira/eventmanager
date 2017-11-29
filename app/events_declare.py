__author__ = 'joe'

from app.randomId import get_random_id


class Items(object):
	def __init__(self, category, event_name, time, location, list_id):
		self.category = category
		self.event_name = event_name
		self.time = time
		self.location = location
		self.list_id = list_id
		self.id = get_random_id()