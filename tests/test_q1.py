"""
Lab 5 Question 1 tests

You only need to test the __eq__() method of the Vector3D class.
"""

import sys
import unittest
sys.path.append('.')
from src.q1 import Vector3D

class TestVector3D(unittest.TestCase):
    """Unit tests for the Vector3D class."""
    def setUp(self) -> None:
        self.vector = Vector3D(1.0, 2.0, 3.0)

    def test_x(self) -> None:
        """Test the x property."""
        self.assertEqual(self.vector.x, 1.0)
    
    def test_y(self) -> None:
        """Test the y property."""
        self.assertEqual(self.vector.y, 2.0)
    
    def test_z(self) -> None:
        """Test the z property."""
        self.assertEqual(self.vector.z, 3.0)
    
    def test_distance_between_equal(self) -> None:
        """Test the distance_between method."""
        other_vector = Vector3D(1.0, 2.0, 3.0)
        self.assertEqual(self.vector.distance_between(other_vector), 0.0)
    
    def test_distance_between_not_equal(self) -> None:
        """Test the distance_between method."""
        other_vector = Vector3D(2.0, 3.0, 4.0)
        self.assertGreater(self.vector.distance_between(other_vector), 1.0)
