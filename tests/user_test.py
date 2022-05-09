import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'banana')

    #Ascertains that the password is being hashed and the password_hashes column contains a value.
    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hashes is not None)

    #Confirms that the application raises an AttributeError when we try and access the password property
    def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

    #Confirms that our password_hash can be verified when we pass in the correct password
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('banana'))
