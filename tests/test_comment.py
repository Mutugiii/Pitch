import unittest
from app.models import Comment
from app import db

class TestCommentModel(unittest.TestCase):
    '''
    Test class for the Comment Model
    '''
    
    def setUp(self):
        '''
        Function to prepare for every test case
        '''
        self.new_comment = Comment(content = 'I love this pitch')

    def tearDown(self):
        '''
        Function to clear up after every test case
        '''
        Comment.query.delete()

    def test_init(self):
        '''
        Test if variables are correctly initialzed
        '''
        self.assertEqual(self.new_comment.content, 'I love this pitch')
        
    def test_save_comment(self):
        '''
        Test saving to test db
        '''
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)

