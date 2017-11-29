__author__ = 'joe'

# Operations to be handled on users accounts(adding or deleting user)
from .user_operations import UserManager


class User1(object):
    users = []

    def __init__(self, email, username,  password):
        self.email = email
        self.username = username
        self.password = password
