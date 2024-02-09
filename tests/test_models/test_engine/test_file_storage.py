#!/usr/bin/python3
"""
Unit Testing for file_storage
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import unittest
import os
import models


class TestFileStorage(unittest.TestCase):
    """
    Tests for class BaseModel from Class BaseModel
    """

    def setUp(self):
        """
        setup for test using instance
        """
        self.file_storage = FileStorage()

    def test_file_path(self):
        """
        test_file_path from class FileStorage
        """
        self.assertEqual(str, type(self.file_storage._FileStorage__file_path))

    def test__objects(self):
        """
        test__objects from class FileStorage
        """
        self.assertEqual(dict, type(self.file_storage._FileStorage__objects))

    def test_class_name(self):
        """
        test for class name in class FileStorage
        """
        self.assertEqual(self.file_storage.__class__.__name__, "FileStorage")

    def test_all_no_args(self):
        """
        Test All not Arguments in class FileStorage
        """
        self.assertEqual(type(self.file_storage.all()), dict)

    def test_FileStorage_no_args(self):
        """
        test_FileStorage_no_args in class FileStorage
        """
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_storage(self):
        """
        test_storage in class FileStorage
        """
        self.assertEqual(type(models.storage), FileStorage)

    def test_all_with_arg(self):
        """
        Test All With Arguments in class FileStorage
        """
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_without_id(self):
        """
        Test if new works correctly with
        an object without id in class FileStorage
        """

        class Test:
            pass

        test = Test()
        with self.assertRaises(AttributeError):
            models.storage.new(test)

    def test_reload_with_arg(self):
        """
        Test Reload With Args in class FileStorage
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_save_empty_objects(self):
        """
        Test If Save Works Correctly With Empty __objects in class FileStorage
        """
        self.file_storage._FileStorage__objects = {}
        models.storage.save()
        with open("file.json", "r") as file:
            self.assertEqual(file.read(), "{}")

    if __name__ == "__main__":
        unittest.main()
