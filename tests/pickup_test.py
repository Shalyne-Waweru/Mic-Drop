import unittest
from app.models import Pickup,User
from app import db

class PickuplineModelTest(unittest.TestCase):

    def setUp(self):
            self.user_Shalyne = User(email = 'sha@ms.com', username = 'Shalyne', password = 'potato')
            self.new_pickupline = Pickup(pickupLine='If you’re feeling down, I can feel you up.',user = self.user_Shalyne )

    def tearDown(self):
            Pickup.query.delete()
            User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pickupline.pickupLine,'If you’re feeling down, I can feel you up.')
        self.assertEquals(self.new_pickupline.user,self.user_Shalyne)

    def test_save_pickupline(self):
        self.new_pickupline.save_pickup_line()
        self.assertTrue(len(Pickup.query.all())>0)

    def test_get_pickupline_by_id(self):

        self.new_pickupline.save_pickup_line()
        got_pickuplines = Pickup.get_pickup_lines(1)
        self.assertTrue(len(got_pickuplines) == 1)