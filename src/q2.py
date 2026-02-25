"""
Lab 5 Question 2: Creating and raising custom errors

Use the provided CourseFullError exception to implement the enroll() method of the Course class
according the the documentation. Make sure to write tests, as usual.
"""

class CourseFullError(Exception):
    """
    Custom exception to indicate that a course is full.
    """

class Course:
    """
    Represents a course with a maximum capacity of students.
    """
    def __init__(self, course_number: str, name: str, max_students: int):
        """
        Constructs a Course object with the given course number, name, and maximum 
        number of students.
        
        Args:
            course_number (str): The course number.
            name (str): The name of the course.
            max_students (int): The maximum number of students allowed in the course.
        """
        self.course_number = course_number
        self.name = name
        self.max_students = max_students
        self.__students: list[str] = []

    def enroll(self, student_id: str) -> None:
        """
        Enrolls a student in the course if there is capacity.
        
        Args:
            student_id (str): The ID of the student to enroll.
        
        Raises:
            CourseFullError: If the course is already full.
        """
        #TODO: Implememt and test
