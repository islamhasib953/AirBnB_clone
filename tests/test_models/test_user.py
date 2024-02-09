#!/usr/bin/python3
"""
Unit Testing for user
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Tests for class User from Class User
    """

    def setUp(self):
        """
        setup for test using instance
        """
        self.my_model = User()

    def test_class_name(self):
        """
        test for class name in class User
        """
        self.assertEqual(self.my_model.__class__.__name__, "User")

    def test_type_of_attributes(self):
        """
        test_type_of_attributes
        """
        self.assertEqual(str, type(self.my_model.email))
        self.assertEqual(str, type(self.my_model.first_name))
        self.assertEqual(str, type(self.my_model.password))
        self.assertEqual(str, type(self.my_model.last_name))

    def test_contain_of_attributes(self):
        """
        test_contain_of_attributes
        """
        self.assertEqual("", self.my_model.last_name)
        self.assertEqual("", self.my_model.password)
        self.assertEqual("", self.my_model.first_name)
        self.assertEqual("", self.my_model.email)

    def test_name_of_attributes(self):
        """
        test_name_of_attributes
        """
        self.assertEqual(hasattr(self.my_model, "email"), True)
        self.assertEqual(hasattr(self.my_model, "password"), True)
        self.assertEqual(hasattr(self.my_model, "first_name"), True)
        self.assertEqual(hasattr(self.my_model, "last_name"), True)

    def test_number_attributes_in_user(self):
        """
        test_number_attributes_in_user
        """
        class_attributes = vars(User)
        self.assertEqual(len(class_attributes), 6)


if __name__ == "__main__":
    unittest.main()
