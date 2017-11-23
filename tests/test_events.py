__author__ = 'joe'

import unittest
from app.events_operations import EventsManager


class TestEvent(unittest.TestCase):
	def setUp(self):
		self.event = EventsManager()
		# self.items = dict(category="hackathon", name="rubics cube", time="11:45pm", location="galana plaza")

		# checks method types in adding an event

	def test_add_event_if_key_anInt(self):
			self.assertRaises(ValueError, self.event.add_event, 4, "number")

	def test_update_event(self):
			self.assertRaises(ValueError, self.event.update_event())

	def test_get_event_list_for_nonInt(self):
		self.assertRaises(ValueError, self.event.get_event_list(2, 'Night Dance'))
