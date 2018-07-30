import numpy as np


def print_max_min(index,max_index,array) -> None:
    """uses recursion to find the min and max of the array"""
    if index >= max_index:
        return
    else:
        MIN = min(array[index])
        MAX = max(array[index])
        print("{0} and {1} are the minimum and maximum items in the array at index {2}".format(MIN, MAX, index))
        print_max_min(index + 1, max_index,array)


#generates a narray with random numbers

rand_arry = np.random.rand(10,10)
print_max_min(0,rand_arry.shape[0],rand_arry)

