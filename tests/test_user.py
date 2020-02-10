import unittest
from app.models import User

class TestUserModel(unittest.TestCase):
    '''
    Test class for the User Model
    '''
    
    def setUp(self):
        '''
        Function to prepare for every test case
        '''
        self.new_user = User(password = 'kamau')

    def test_password_setter(self):
        '''
        Test that the password setter works
        '''
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        '''
        Confirm that attribute error is raised when we try to access password attrib
        '''
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        '''
        Test the verify_password function
        '''
        self.assertTrue(self.new_user.verify_password('kamau'))

