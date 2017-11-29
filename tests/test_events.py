__author__ = 'joe'
import unittest
<<<<<<< HEAD
from app import create_app
from flask import json
# from app.events_operations import EventsManager
# from app.events_declare import Items
=======
from app.events_operations import EventsManager
>>>>>>> d2e50a2593e7105a4d5bbdae5b3c06c39b5aa735

# class to contain test cases for events


class TestEvent(unittest.TestCase):
	def setUp(self):
<<<<<<< HEAD
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
=======
		self.event = EventsManager()
		self.items = dict(
			category="hackathon",
			name="rubics cube",
			description="one night of intense outputs",
			date="11:45pm",
			location="galana plaza"
			)

		# checks method types in adding an event

	def test_add_event_if_key_anInt(self):
		self.assertRaises(ValueError, self.event.add_event, 4, "number")

	def test_update_event(self):
		self.assertRaises(ValueError, self.event.update_event(2))

	def test_get_event_list(self):
		self.assertRaises(ValueError, self.event.get_event_list(3))
	#
	# def test_delete_event(self):
	# 	self.assertTrue(ValueError, self.event.delete_event, msg='delete failed')
	#

>>>>>>> d2e50a2593e7105a4d5bbdae5b3c06c39b5aa735
