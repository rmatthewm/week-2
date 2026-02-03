import numpy as np


# update/add code below ...

def ways(n):
    """ Returns the number of ways to give change using only
    pennies and nickles.

    Each group of 5 pennies can be replaced by a single nickle.
    This gives n // 5 max number of nickles, which gives us the
    number of combinations including nickles, leaving one last
    case where we return only pennies. The base case of n = 0 
    also holds true because there is only one way to not return
    change.

    Args:
        n (int): the amount of change to give in cents

    Returns:
        int: the number of ways to return the change
    """
    return n // 5 + 1

def lowest_score(names, scores):
    return None

def sort_names(names, scores):
    return None

# temp testing
print(ways(12))
print(ways(20))
print(ways(3))
print(ways(0))
print(ways(127))