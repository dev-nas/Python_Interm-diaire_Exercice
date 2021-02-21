""" 
    test unitaire de la méthode getFullName
    de la classe bank.Person
"""
# imports requis pour le test unitaire
import unittest
from .client import Person

class TestPerson(unittest.TestCase):
    
    def setUp(self):
        self.p = Person(1, "john", "smith")
    
    def test_firstname_is_str(self):
        # assertRaises test si le développeur a géré les erreurs d'instanciation
        # assertRaises s'utilise avec un gestionnaire de contexte
        with self.assertRaises(TypeError):
            Person(1, f=123, l="SMITH")
    
    def test_getfullname(self):       
        # self.assertEqual("John SMITH", self.p.getFullName())
        assert "John SMITH" == self.p.getFullName()
    
    def tearDown(self):
        del self.p

# code pour lancer le test depuis le module comme programme principal
if __name__ == "__main__":
    unittest.main()