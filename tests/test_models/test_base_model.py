#!/usr/bin/python3
"""
Unit Testing for base_module
"""
import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):
    """
    Tests for class BaseModel from Class BaseModel
    """

    def setUp(self):
        """
        setup for test using instance
        """
        self.my_model = BaseModel()

    def test_str(self):
        """
        test for the __str__ in class BaseModel
        """
        strr = "[{}] ({}) {}".format(
            self.my_model.__class__.__name__, self.my_model.id, self.my_model.__dict__
        )
        self.assertEqual(str(self.my_model), strr)

    def test_init(self):
        """
        test for the __init__ in class base_model
        """
        self.assertIsInstance(self.my_model, BaseModel)
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime.datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime.datetime)

    def test_attributes(self):
        """
        test for the attributes
        """
        self.assertTrue(len(self.my_model.id) > 0)
        self.assertNotEqual(self.my_model.created_at, datetime.datetime.now())
        self.assertNotEqual(self.my_model.updated_at, datetime.datetime.now())

    def test_save(self):
        """
        test for the save in class BaseModel
        """
        up = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(up, self.my_model.updated_at)

    def test_to_dict(self):
        """
        test for the to_dict in class BaseModel
        """
        d = self.my_model.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["created_at"], self.my_model.created_at.isoformat())
        self.assertEqual(d["updated_at"], self.my_model.updated_at.isoformat())
        self.assertEqual(d["id"], self.my_model.id)

    def test_class_name(self):
        """
        test for class name in class BaseModel
        """
        self.assertEqual(self.my_model.__class__.__name__, "BaseModel")

    def test_id(self):
        """
        test for id is string or not in class BaseModel
        """
        self.assertIsInstance(self.my_model.id, str)

    def test_unique_id(self):
        my_model2 = BaseModel()
        self.assertNotEqual(my_model2.id, self.my_model.id)

    def test_update(self):
        """
        test for update after save function in class BaseModel
        """
        self.my_model.updated_at
        sv = self.my_model.save
        self.assertNotEqual(sv, self.my_model.updated_at)


if __name__ == "__main__":
    unittest.main()
