__author__ = 'joe'

# Operations to be handled on users accounts(adding or deleting user)
from  .user_operations import UserManager


class User1(object):
    users = []

    def __init__(self, email,  password):
        self.email = email
        self.password = password
