"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


"""
Initialization
"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 0


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """

    bake_time_remaining = EXPECTED_BAKE_TIME - elapsed_bake_time
    return(bake_time_remaining)


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time in minutes.

    Parameters:
        number_of_layers (int): The number of layers added to the lasagna.

    Returns:
        int: The total preparation time (in minutes) for the given number of layers.
    """
    prep_time = number_of_layers * 2 
    return(prep_time)


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time (prep + bake) in minutes.

    Parameters:
        number_of_layers (int): The number of layers added to the lasagna.
        elapsed_bake_time (int): The number of minutes the lasagna has been baking.

    Returns:
        int: The total number of minutes spent cooking.
    """
    total_time = preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    return(total_time)

