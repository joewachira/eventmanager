__author__ = 'joe'
from flask import jsonify, abort, request
from flask import make_response
from . import home

from app.randomId import get_random_id

events_info = [
    {
        'category': 'dance',
        'name': 'Salsa dance lessons',
        'description': 'learn the origin of amazing moves',
        'date': '12/11/17',
        'location': 'Uchumi ngong',

    }
    # {
    #     'category': 'wedding',
    #     'name': 'BW weds ER',
    #     'description': 'let's unite in this union',
    #     'date': '22/11/17',
    #     'location': 'greenspan gardens',

]
# create a new event


@home.route('/api/v1/events', methods=['GET'])
def add_event():
    if not request.json or 'category' not in request.json:
        abort(403)
    if not request.json or 'name' not in request.json:
        abort(403)
    if not request.json or 'description' not in request.json:
        abort(403)
    if not request.json or 'date' not in request.json:
        abort(403)
    if not request.json or 'location' not in request.json:
        abort(403)

    event = {
        "eventid": get_random_id(),
        "category": request.json.get('category'),
        "name": request.json['name'],
        "description": request.json.get('description', ''),
        "date": request.json.get('date', ''),
        "location": request.json.get('location')
    }
    events_info.append(event)
    return jsonify({'event': event}), 201


# fetching a specific event (using eventid)


@home.route('/api/v1/events/<int:eventid>', methods=['GET'])
def get_event(eventid):
    event = [event for event in events_info if event['eventid'] == eventid]
    if len(event) == 0:
        abort(404)
    return jsonify({'event': event[0]})


# endpoint for fetching all events

@home.route('/api/v1/events')
def view_events():
    return jsonify({'events': events_info})


# endpoint for deleting an event


@home.route('/api/v1/events/<int:eventid>', methods=['DELETE'])
def delete_event(eventid):
    event = [event for event in events_info if event['eventid'] == eventid]
    if len(event) == 0:
        abort(404)
    events_info.remove(event[0])
    return jsonify({'event': True})


# edit and event


@home.route('/api/v1/events/<int:eventid>', methods=['PUT'])
def edit_event(eventid):
    event = [event for event in events_info if event['eventid'] == eventid]
    if len(event) == 0:
        abort(404)
    if not request.json:
        abort(403)

    event[0]['category'] = request.json.get('category', event[0]['category'])
    event[0]['name'] = request.json.get('name', event[0]['name'])
    event[0]['description'] = request.json.get('description', event[0]['description'])
    event[0]['date'] = request.json.get('date', event[0]['date'])
    event[0]['location'] = request.json.get('location', event[0]['location'])
    return jsonify({'event': event[0]})


# search by location

@home.route('/api/v1/events/<string:name>', methods=['GET'])
def search_by_location(location):
    event_search = [event for event in events_info if event['name'] == location]
    if event_search:
        return jsonify({'events', event_search})
    abort(404)