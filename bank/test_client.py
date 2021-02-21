import unittest
from .client import Client
import datetime


class TestClient(unittest.TestCase):
    
    def setUp(self):
        self.date_joint_as_str = "2021/02/05"
        self.client = Client(1, self.date_joint_as_str, 1, "matt", "LAMAM")
    
    def test_getdatejoint(self):
        self.assertIsInstance(self.client.getDateJoint(), datetime.datetime)
        self.assertEqual(self.date_joint_as_str, self.client.getDateJoint().strftime("%Y/%m/%d"))
        self.assertEqual("05-02-2021", self.client.getDateJoint("%d-%m-%Y"))

if __name__ == "__main__":
    unittest.main()