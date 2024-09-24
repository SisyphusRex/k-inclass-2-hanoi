"""class for solving tower of Hanoi"""

# Walter Podewil
# CIS 226
# September 24, 2024


class Hanoi:
    """Solves Tower of Hanoi problem"""

    def solve(self, n: int):
        """Solve method"""
        self.__move_disc(n, "A", "B", "C")

    def __move_disc(self, n, src, temp, dest):
        """Recursive method to solve"""
        if n == 1:
            print(f"Move {src} -> {dest}")
            return
        self.__move_disc(n - 1, src, dest, temp)
        self.__move_disc(1, src, temp, dest)
        self.__move_disc(n - 1, temp, src, dest)
