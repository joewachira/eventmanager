__author__ = 'joe'
import unittest
from app import create_app
from flask import json
# from app.events_operations import EventsManager
# from app.events_declare import Items

# class to contain test cases for events


class TestEvent(unittest.TestCase):
	def setUp(self):
		self.gaks = create_app()
		self.event = self.gaks.test_client
		self.items = dict(
			category="hackathon",
			event_name="rubics cube",
			date="12/11/17",
			location="galana plaza",
			description="one night of intense outputs",
		)

	# checks method types in adding an event
	def test_add_event(self):
		result = self.event().post('/api/v1/events', data=json.dumps(self.items, content_type='application/json'))
		self.assertEqual(result.status_code, 201)

	def test_add_event_has_location(self):
		result = self.event().post('/api/v1/events', data=json.dumps(self.items), content_type='application/json')
		self.assertEqual(result.status_code, 403)

	def test_add_event_has_name(self):
		result = self.event().post('/api/v1/events', data=json.dumps(self.event), content_type='application/json')
		self.assertEqual(result.status_code, 403)

	def test_add_event_has_userid(self):
		result = self.event().post('/api/v1/events', data=json.dumps(self.event), content_type='application/json')
		self.assertEqual(result.status_code, 403)

	def test_can_get_events(self):
		result = self.event().get('/api/v1/events', content_type='application/json')
		self.assertEqual(result.status_code, 404)
