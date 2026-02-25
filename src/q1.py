"""
Lab 5 Question 1: Overwriting __eq__()


Please implement and test the __eq__() method for the following class.

Two Vector3D objects are considered equal if the distance between them is less than 0.01.
Use the MAX_DISTANCE constant provided.
"""

import math

MAX_DISTANCE = 0.01 # maximum distance for two Vector3Ds to be considered equal

class Vector3D:
    """
    Represents a vector in 3D space with x, y, and z coordinates.
    """
    def __init__(self, x: float, y: float, z: float):
        """
        Constructs a Vector3D object with the given x, y, and z coordinates.

        Args:
            x (float): The x-coordinate of the vector.
            y (float): The y-coordinate of the vector.
            z (float): The z-coordinate of the vector.
        """
        self._x = x
        self._y = y
        self._z = z

    def distance_between(self, other: 'Vector3D') -> float:
        """
        Returns the distance between this vector and another Vector3D object.
        
        Args:
            other (Vector3D): Another Vector3D object to calculate the distance to.
        
        Returns:
            float: The distance between the two vectors, if other is a Vector3D.
                    If other is not a Vector3D, returns False.
        """
        dist_squared = (self._x - other._x) ** 2 + (self._y - other._y) ** 2 + (self._z - other._z) ** 2
        return math.sqrt(dist_squared)

    def __eq__(self, other: object) -> bool:
        #TODO: Implement and test
        pass
