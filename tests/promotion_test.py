import unittest
from app.models import Promotion,User
from app import db

class PromotionModelTest(unittest.TestCase):

    def setUp(self):
            self.user_Shalyne = User(email = 'sha@ms.com', username = 'Shalyne', password = 'potato')
            self.new_promotion_pitch = Promotion(promotion='Promotion Pitch',user = self.user_Shalyne )

    def tearDown(self):
            Promotion.query.delete()
            User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_promotion_pitch.promotion,'Promotion Pitch')
        self.assertEquals(self.new_promotion_pitch.user,self.user_Shalyne)

    def test_save_promotion_pitch(self):
        self.new_promotion_pitch.save_promotion()
        self.assertTrue(len(Promotion.query.all())>0)

    def test_get_promotion_by_id(self):

        self.new_promotion_pitch.save_promotion()
        got_promotions = Promotion.get_promotions(1)
        self.assertTrue(len(got_promotions) == 1)