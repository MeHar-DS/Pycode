from enum import Enum


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


color = Color(input("Enter the colour of your choice : \"red\" \"green\" or \"blue\" \n").strip().casefold())


def match(color):
    """ This function matches the user provided color.
    Implemented as a function since match is not supported in my current python version"""
    if color == Color.RED:
        print("I see red!")
    elif color == Color.BLUE:
        print("Feeling blue!")
    elif color == Color.GREEN:
        print("Grass is green!")


match(color)


