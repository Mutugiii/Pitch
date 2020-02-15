import unittest
from app.models import Pitch
from app import db

class TestPitchClass(unittest.TestCase):
    '''
    Test to test the Pitch class/Table in db
    '''
    def setUp(self):
        '''
        To set up before each test case
        '''
        self.new_pitch = Pitch(title = 'My Pitch',content =  'I love this game', category = 'promotion')
        
    def tearDown(self):
        '''
        Function to clear up after every test case
        '''
        Pitch.query.delete()

    def test_init(self):
        '''
        Test if variables are correctly initialzed
        '''
        self.assertEqual(self.new_pitch.title, 'My Pitch')
        self.assertEqual(self.new_pitch.content, 'I love this game')
        self.assertEqual(self.new_pitch.category, 'promotion')

    def test_save_pitch(self):
        '''
        Test saving to test db
        '''
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

