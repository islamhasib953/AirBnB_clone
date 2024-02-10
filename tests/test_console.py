#!/usr/bin/python3
"""
Unit Testing for console
"""
from console import HBNBCommand
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review

import unittest


class TestConsol(unittest.TestCase):
    """
    Tests for class HBNBCommand from console
    """

    def setUp(self):
        """
        setup for test using instance
        """
        self.my_model = HBNBCommand()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.state = State()
        self.user = User()
        self.review = Review()

    def test_name(self):
        """
        test_name
        """
        self.assertEqual(self.city.__class__.__name__, "City")
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")
        self.assertEqual(self.state.__class__.__name__, "State")
        self.assertEqual(self.place.__class__.__name__, "Place")
        self.assertEqual(self.user.__class__.__name__, "User")
        self.assertEqual(self.review.__class__.__name__, "Review")

    def test_number_attributes(self):
        """
        test_number_attributes
        """
        class_attributes1 = vars(User)
        class_attributes2 = vars(Amenity)
        class_attributes3 = vars(Place)
        class_attributes4 = vars(State)
        class_attributes5 = vars(Review)
        class_attributes6 = vars(City)

        self.assertEqual(len(class_attributes1), 6)
        self.assertEqual(len(class_attributes2), 3)
        self.assertEqual(len(class_attributes3), 13)
        self.assertEqual(len(class_attributes4), 3)
        self.assertEqual(len(class_attributes5), 5)
        self.assertEqual(len(class_attributes6), 4)
