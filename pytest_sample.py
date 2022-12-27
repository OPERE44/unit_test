"""
Created on Tue Dec 27 12:01:58 2022

@author: Peter Opere
"""
# Pytest is a popular testing framework for Python that makes it easy to write and run tests for your Python code. 
# It is a powerful and flexible tool that can help you write and run efficient and reliable tests for your Python code.

# To get started with pytest, you will need to install it using pip. You can do this by running the following command:
# pip install pytest

# Once you have pytest installed, you can write test functions or methods in your Python code. Test functions are functions that start
# with the test_ prefix and are decorated with the @pytest.mark.test decorator. Test methods are methods in a class that start with the test_ prefix and are decorated with the @pytest.mark.test decorator.

# Here is an example of a simple test function that tests a function that adds two numbers:

import pytest


def add(x, y):
    return x + y

@pytest.mark.test
def test_add():
    assert add(2, 3) == 5
    assert add(-2, 3) == 1
    assert add(2, -3) == -1
    
def calculate_area(length, width):
    return length * width

@pytest.mark.test
def test_calculate_area():
    assert calculate_area(2, 3) == 6
    assert calculate_area(5, 5) == 25
    assert calculate_area(10, 2) == 20
    assert calculate_area(0, 10) == 0    

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

class TestPoint:
    @pytest.mark.test
    def test_distance_to_origin(self):
        point1 = Point(3, 4)
        assert point1.distance_to_origin() == 5
        
        point2 = Point(0, 5)
        assert point2.distance_to_origin() == 5
        
        point3 = Point(-3, -4)
        assert point3.distance_to_origin() == 5

def is_palindrome(s):
    return s == s[::-1]

@pytest.mark.test
def test_is_palindrome():
    assert is_palindrome('racecar')
    assert is_palindrome('level')
    assert is_palindrome('deified')
    assert not is_palindrome('hello')
    assert not is_palindrome('world')        
