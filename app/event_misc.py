__author__ = 'joe'

from app.events_declare import Items
from app.randomId import get_random_id


class EventMisc(object):

	def __init__(self, category, username):

		self.category = category
		self.username = username
		self.id = get_random_id()
		self.items = []

