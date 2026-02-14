"""
Please implement the class below to fit the documentation.

You are not required to write tests for q2.
"""

import sys
from typing import Any
import requests
import pandas as pd
sys.path.append('.')
from src.q1 import WeatherURL

class WeatherForecast:
    """Retrieves the weather forecast from the National Weather Service"""

    def __init__(self, user_agent_file: str):
        """
        Gets the User Agent from the specified file
        
        Args:
            user_agent_file (str): the file that contains the User Agent
        """
        with open(user_agent_file, 'r', encoding='utf-8') as f:
            self._user_agent = f.read().strip()
    
    def get_weather(self, latitude: float = 37.8049, longitude: float = -122.2725) -> Any:
        """
        Return a dataframe containing the predicted temperatures and chances of precipitation,
        with timestamps.
        
        Args:
            latitude (float): the latitude for which we want the weather
            longitude (float): the longitude for which we want the weather
        """
        #TODO: use q1.WeatherURL.get_weather_url() to get the URL for the weather
        #TODO: parse through the "periods" in the weather (in the "properties" section),
        #       and put the data into a Pandas dataframe of this format:
        #       | startTime | endTime | temperature | probabilityOfPrecipitation |
        #
        #       The columns in the dataframe should be named as specified above.
        #       The temperature should be in Fahrenheit.
        pass