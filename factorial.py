#Walter Podewil
#CIS 226
#September 19, 2024
import math
"""Factorial Module"""

class Factorial:
    """Class for Solving Factorial"""
    def solve(self, number):
        """Solve factorial method"""
        #base case
        if number == 1:
            return number
        #not base case
        result = self.solve(number - 1)
        return number * result

    def solve2(self, number):
        return math.factorial(number)
