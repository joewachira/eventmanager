__author__ = 'joe'

# Operations to be handled on users accounts(adding or deleting user)
<<<<<<< HEAD
from .user_operations import UserManager
=======
from  .user_operations import UserManager
>>>>>>> d2e50a2593e7105a4d5bbdae5b3c06c39b5aa735


class User1(object):
    users = []

<<<<<<< HEAD
    def __init__(self, email, username,  password):
=======
    def __init__(self, email,  password):
>>>>>>> d2e50a2593e7105a4d5bbdae5b3c06c39b5aa735
        self.email = email
        self.username = username
        self.password = password
