import unittest
from app.models import Interview,User
from app import db

class UserModelTest(unittest.TestCase):

    def setUp(self):
            self.user_Shalyne = User(email = 'sha@ms.com', username = 'Shalyne', password = 'potato')
            self.new_interview_pitch = Interview(interview='Interview Pitch',user = self.user_Shalyne )

    def tearDown(self):
            Interview.query.delete()
            User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_interview_pitch.interview,'Interview Pitch')
        self.assertEquals(self.new_interview_pitch.user,self.user_Shalyne)

    def test_save_interview_pitch(self):
        self.new_interview_pitch.save_interview()
        self.assertTrue(len(Interview.query.all())>0)

    def test_get_interview_by_id(self):

        self.new_interview_pitch.save_interview()
        got_interviews = Interview.get_interviews(1)
        self.assertTrue(len(got_interviews) == 1)