"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the time taken in minutes to prepare the lasagne based 
    on number of layers.

    Parameters:
        number_of_layers (int): The number of layers of lasagne.
    
    Returns:
        int: The number of minutes requires to prepare a lasagne of N layers. 

    Function that takes the number of layers and multiplies that by the 
    number of minutes each layer takes to prepare (PREPARATION_TIME).
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculates the total time elapsed in kitchen so far.

    Parameters:
        number_of_layers (int): The number of layers of lasagna to assemble.
        elapsed_bake_time (int): The time in minutes the lasagna has been baking.
    Returns:
        int: The number of minutes spent in the kitche so far.

    Function which takes number of layers of lasagna, plus current elapsed bake time, 
    to calculate how long has been spent in the kitchen (total PREPARATION_TIME plus elapsed baking time)
    """

    return elapsed_bake_time + (number_of_layers * PREPARATION_TIME)

