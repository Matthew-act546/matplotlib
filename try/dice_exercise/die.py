from random import randint

class Die:
    """A class that represent a single dice"""

    def __init__(self, num_sides=6):
        """Assuming a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides"""
        return randint(1, self.num_sides)