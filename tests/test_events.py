__author__ = 'joe'

import unittest
from app.events_operations import Events


class TestEvent(unittest.TestCase):
	def setUp(self):
		self.event = Events()
		self.items = dict(category="hackathon", name="rubics cube", time="11:45pm", location="galana plaza")

		# checks if event is created successfully. If so create method returns true

		def test_event_creation(self):
			mod_event = self.event
			items = self.items
			status = mod_event(items.pop('category'),
							   items.pop('name'),
							   items.pop('time'),
							   items.pop('location'))
			self.assertTrue(status)



