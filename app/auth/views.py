from flask import jsonify, abort, request, session
from flask import make_response
from . import user_class

from . import auth


# api endpoint to register user
@auth.route('/api/v1/auth/register', methods=['POST'])
def register():
    if not request.json or 'email' not in request.json: 	# email and password must be included
        abort(403)
    if not request.json or 'password' not in request.json:	 # password must be included
        abort(403)
    user = {
        'id': len(user_class.User1.users)+1,
        'email': request.json['email'],
        'username': request.json['username'],
        'password': request.json['password']
    }
    user_class.User1.users.append(user)
    return jsonify({'user': user}), 201

# endpoint for user to login


@auth.route('/api/v1/auth/login', methods=['POST'])
def login():    
    if not request.json or 'email' not in request.json: 	# when no email provided
        abort(403)
    
    email = request.json['email']
    password = request.json['password']
    
    user = [user for user in user_class.User1.users if user['email'] == email and user['password'] == password]
    if user:
        session.email = user[0]['email']
        session.userid = user[0]['id']
        
        return jsonify({'user': user}), 200
    abort(404)


# user can edit password

@auth.route('/api/v1/auth/reset-password/<string:email>', methods=['PUT'])
def password_reset(email):
    user = [user for user in user_class.User1.users if user['email'] == email]
    if not user:
        abort(404)
    user[0]['password'] = request.json.get('password', user[0]['password'])
    return jsonify({'user': user}), 200