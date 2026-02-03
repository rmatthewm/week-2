import numpy as np


# update/add code below ...

def ways(n, coin_types=[5,1]):
    """ Returns the number of ways to give change using only
    pennies and nickles.

    Each group of 5 pennies can be replaced by a single nickle.
    This gives n // 5 max number of nickles, and n // 5 + 1 ways
    to return change, because we also have the case with all pennies.

    This can be extended to any combination of coins by using
    recursion. This has horrible time complexity, but I couldn't
    think of a better solution at this time. For each way of using
    a larger coin, we have a number of ways to return the change that
    is left over using the other coins. These can be summed to find the
    total number of ways.

    Args:
        n (int): the amount of change to give in cents

    Returns:
        int: the number of ways to return the change
    """

    # Sort the coin types into descending order
    coin_types.sort()
    coin_types = coin_types[::-1]

    # The base case is when we have only one coin type left. It doesn't
    # matter if we can give exact change, because there is only one way
    # to return it, assuming we have a rule to always round a certain way.
    if len(coin_types) == 1:
        return 1

    # For each way that we can take out the largest coin, add the ways to
    # return the remaining change using the other coins
    ways_sum = 0
    for i in range(0, n // coin_types[0] + 1):
        ways_sum += ways(n - coin_types[0]*i, coin_types=coin_types[1:])

    # Return the total number of ways
    return ways_sum

def lowest_score(names, scores):
    """ Returns the name associated with the lowest score.

    Args:
        names (np.array(str)): a list of student names
        scores (np.array(int)): a list of scores corresponding to the names

    Returns:
        str: the name of the student with the lowest score
    """

    # Find the index of the student with the lowest score
    student_i = np.argmin(scores)

    # Return the name of that student
    return names[student_i]

def sort_names(names, scores):
    """ Returns an array of student names sorted by their scores

    Args:
        names (np.array(str)): a list of student names
        scores (np.array(int)): a list of scores corresponding to the names

    Returns:
        np.array(str): the sorted names
    """

    # Since we cannot combine data types in numpy arrays, we can find the
    # sort order from the scores using argsort, then sort the names accordingly.
    # To get descending order, we can reverse the array.
    sort_order_array = np.argsort(scores)[::-1]
    return names[sort_order_array]
