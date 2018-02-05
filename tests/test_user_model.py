import unittest
from app.models import User

class UserModelTestCase(unittest.TestCase):
	def test_username_setter(self):
		u = User(email='test@sap.com')