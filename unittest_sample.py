"""
Created on Tue Dec 27 11:16:58 2022

@author: Peter Opere
"""
# The Python unittest module is a built-in library that provides tools for testing Python code. It is a powerful and flexible tool that 
# can help you write and run efficient and reliable tests for your Python code.

# To get started with unittest, you will need to create a test class that inherits from unittest.TestCase. This test class will contain one
# or more test methods, which are functions that test a specific aspect of your code.

import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(2, -3), -1)
        
def calculate_area(length, width):
    return length * width

class TestCalculateArea(unittest.TestCase):
    def test_calculate_area(self):
        self.assertEqual(calculate_area(2, 3), 6)
        self.assertEqual(calculate_area(5, 5), 25)
        self.assertEqual(calculate_area(10, 2), 20)
        self.assertEqual(calculate_area(0, 10), 0)        
 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

class TestPoint(unittest.TestCase):
    def test_distance_to_origin(self):
        point1 = Point(3, 4)
        self.assertEqual(point1.distance_to_origin(), 5)
        
        point2 = Point(0, 5)
        self.assertEqual(point2.distance_to_origin(), 5)
        
        point3 = Point(-3, -4)
        self.assertEqual(point3.distance_to_origin(), 5)

def is_palindrome(s):
    return s == s[::-1]

class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('level'))
        self.assertTrue(is_palindrome('deified'))
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('world'))
               
if __name__ == '__main__':
    unittest.main()
