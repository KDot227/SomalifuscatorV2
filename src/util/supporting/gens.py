import random


class Cesar_value:
    def __init__(self) -> None:
        """
        Initializes a new instance of the Cesar_value class with a random integer between 1 and 13 as the rotation value.
        """
        self.cesar_val = random.randint(1, 13)

    @property
    def value(self):
        """
        Gets the rotation value for the caesar cipher.
        """
        return self.cesar_val

    def rotate(self):
        """
        Rotates the rotation value for the caesar cipher to a new random integer between 1 and 13, and returns the new value.
        """
        self.cesar_val = random.randint(1, 13)
        return self.cesar_val


# this is the cesar_value for all instances
c_val = Cesar_value()
