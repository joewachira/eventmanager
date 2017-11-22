__author__ = 'joe'

# Operations to be handled on users accounts(adding or deleting user)


class Userr(object):
    def __init__(self, username, email,  password):
        self.username = username
        self.email = email
        self.password = password
