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

# temp testing
names = np.array(['Bob', 'Alice', 'P', 'Q', 'R'])
scores = np.array([1,5,2,4,3])
print(sort_names(names, scores))