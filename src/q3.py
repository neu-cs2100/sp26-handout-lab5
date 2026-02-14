"""
Please implement the class below according to the documentation.
"""

class Temperature:
    """Allows users to get and set the tempterature using etiher Celsius of Fahrenheit."""
    def __init__(self, temp_celsius: float):
        """
        Initialize the Temperature object with a starting temperature in Celsius
        
        Args:
            temp_celsius (float): the initial temperature in Celsius
        
        Raises:
            ValueError if the initial temperature is below absolute zero (-273.15°C)
        """
        # TODO: implement
        pass
    
    @property
    def celsius(self) -> float:
        """Return the current temperature in Celsius"""
        # TODO: implement
        pass
    
    @celsius.setter
    def celsius(self, new_temp_celsius: float) -> None:
        """
        Update the tempterature using Celsius

        Args:
            new_temp_celsius (float): the new temperature to set
        
        Raises:
            ValueError if the desired temperature is below absolute zero (-273.15°C)
        """
        # TODO: implement
        pass
    
    @property
    def fahrenheit(self) -> float:
        """Return the current temperature in Fahrenheit"""
        # TODO: implement
        pass

    @fahrenheit.setter
    def fahrenheit(self, new_temp_fahrenheit: float) -> None:
        """
        Update the tempterature using Fahrenheit

        Args:
            new_temp_fahrenheit (float): the new temperature to set
        
        Raises:
            ValueError if the desired temperature is below absolute zero (-459.67°F)
        """
        # TODO: implement
        pass
