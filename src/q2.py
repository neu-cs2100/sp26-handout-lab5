"""
Lab 5 Question 2: Inheritance and Encapsulation

Read the SocialMedisUser class below. Make sure to trace how these attributes
and properties get their values:

- self.__user_id
- self.user_id
- self._username
- self.username
- self.display_name

Your task: add two new classes:

1. RegularUser: Inherits from SocialMediaUser without adding any new attributes or methods

2. VerifiedUser: Inherits from SocialMediaUser, representing a verified user. The constructor
should take an additional parameter, is_verified (boolean), which indicates whether the user 
is verified. If the user is not verified, raise a ValueError in the constructor. Then,
override the display_name property to append a checkmark (✓) to the username to indicate 
the user is verified.
"""

class SocialMediaUser:
    """Base class for social media users."""
    def __init__(self, user_id: str, username: str):
        """
        Initialize a SocialMediaUser with a user ID and username.
        
        Args:
            user_id (str): The unique identifier for the user
            username (str): The username for the user
        
        Raises:
            ValueError: If the username is less than 3 characters long or contains spaces
        """
        self.__user_id = user_id
        self.username = username

    @property
    def user_id(self) -> str:
        """Get the user's unique identifier."""
        return self.__user_id

    @property
    def username(self) -> str:
        """Get the user's username."""
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        """
        Set the user's username, ensuring it is valid (at least 3 characters and no spaces)

        Args:
            value (str): The new username to set
        
        Raises:
            ValueError: If the username is less than 3 characters long or contains spaces
        """
        if len(value) < 3 or ' ' in value:
            raise ValueError(
                "Username must be at least 3 characters long and cannot contain spaces.")
        self._username = value

    @property
    def display_name(self) -> str:
        """Return the display name for the user."""
        return self._username
