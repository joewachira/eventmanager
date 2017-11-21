__author__ = 'joe'
# This class is used to build test cases for user functionality like addUser and deleteUser
import unittest
from app.auth.user_operations import UserManager


class UserFunctionalityTests(unittest.TestCase):
    # initialize the User class
    def setUp(self):
        self.user = UserManager()
        self.newUser = UserManager()

    # assert that email in login is not int
    def test_login_email_for_int(self):
        self.assertRaises(ValueError, self.user.login, 123, "abnoz")

    def test_login_email_for_int_if_pass_is_allInt(self):
        self.assertRaises(ValueError, self.user.login, 123, 1234)

    def test_login_email_for_int_if_password_is_mixed(self):
        self.assertRaises(ValueError, self.user.login, 123, "12344abnoz")

        # method to test for creating user account

    def test_create_account(self):
        self.newUser.users = {}
        current_count = len(self.newUser.users)
        result = self.newUser.register('email@mail.com', 'name')
        self.assertEqual(current_count + 1, result, "User successfully created")

    def test_null_username(self):
        # method to checking when user name is empty
        result = self.newUser.register('xyz@gmail.com', '')
        self.assertEqual(6, result, 'User name cannot be empty')

    def test_null_email(self):
        # method to check if the email is empty
        result = self.newUser.register('', 'James')
        self.assertEqual(6, result, 'Email cannot be empty'), self.user.login, 123, "1234ertgf"