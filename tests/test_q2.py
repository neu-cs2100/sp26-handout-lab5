"""
Lab 5 Question 2 tests

You only need to write tests for the two classes that you added.
"""

import sys
import unittest
sys.path.append('.')
from src.q2 import SocialMediaUser, RegularUser, VerifiedUser

class TestSocialMediaUser(unittest.TestCase):
    """Unit tests for the SocialMediaUser class. Provided for completeness."""

    def test_user_id_is_read_only(self) -> None:
        """Test that the user_id property is read-only."""
        user = SocialMediaUser("123", "testuser")
        with self.assertRaises(AttributeError):
            user.user_id = "456" # type: ignore[misc]

    def test_username_too_short(self) -> None:
        """Test that a username less than 3 characters raises a ValueError."""
        with self.assertRaises(ValueError):
            SocialMediaUser("123", "ab")

    def test_username_with_spaces(self) -> None:
        """Test that a username containing spaces raises a ValueError."""
        with self.assertRaises(ValueError):
            SocialMediaUser("123", "test user")
    
    def test_valid_username(self) -> None:
        """Test that a valid username is set correctly."""
        user = SocialMediaUser("123", "validuser")
        self.assertEqual(user.username, "validuser")
    
    def test_display_name(self) -> None:
        """Test that the display_name is the same as the username."""
        user = SocialMediaUser("123", "regularuser")
        self.assertEqual(user.display_name, "regularuser")