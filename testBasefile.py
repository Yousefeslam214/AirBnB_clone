#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Setup test objects"""
        self.base_model = BaseModel()

    def test_id_generation(self):
        """Test if id is generated"""
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        """Test if created_at is properly set"""
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """Test if updated_at is properly set"""
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str_representation(self):
        """Test the __str__ representation"""
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict(self):
        """Test the to_dict method"""
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.base_model.updated_at.isoformat())
        self.assertTrue('id' in model_dict)

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated_at, self.base_model.updated_at)

if __name__ == '__main__':
    unittest.main()
