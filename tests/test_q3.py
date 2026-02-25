"""
Lab 5 Question 3 tests

You only need to test the from_string() alternate constructor of the Date class.
"""

import sys
import unittest
sys.path.append('.')
from src.q3 import Date

class TestDate(unittest.TestCase):
    """Unit tests for the Date class."""

    def test_constructor(self) -> None:
        """Test the regular constructor."""
        date = Date(2021, 1, 1)
        self.assertEqual(date.year, 2021)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)

    def test_from_timestamp(self) -> None:
        """Test the from_timestamp alternate constructor."""
        timestamp = 1609459200  # Corresponds to 2021-01-01
        date = Date.from_timestamp(timestamp)
        self.assertEqual(date.year, 2021)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)
