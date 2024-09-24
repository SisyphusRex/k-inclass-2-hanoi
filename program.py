"""Program code"""

from factorial import Factorial
from hanoi import Hanoi
import sys


def main(*args):
    """Method to run program"""
    factorial = Factorial()
    hanoi = Hanoi()
    # Show menu and collect input
    choice = int(input("Press 1 for factorial, 2 for tower of hanoi, 3 to exit\n"))
    while choice < 3:
        if choice == 1:
            number = int(input("Give me factorial number: \n"))
            # solved = factorial.solve(number)
            solved = factorial.solve2(number)
            print(solved)
        if choice == 2:
            number = int(input("How many disks in the Tower?\n"))
            hanoi.solve(number)

        choice = int(input("Press 1 for factorial, 2 for tower of hanoi, 3 to exit\n"))

    sys.exit("Goodbye")
