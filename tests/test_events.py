__author__ = 'joe'

import unittest
from app.events_operations import Events


class TestEvent(unittest.TestCase):
	def setUp(self):
		self.event = Events()
		# self.items = dict(category="hackathon", name="rubics cube", time="11:45pm", location="galana plaza")

		# checks method types in adding an event

		def test_add_event(self):
			self.assertRaises(ValueError, self.event.add_event, 4, "number")

		def test_update(self):
			self.assertRaises



