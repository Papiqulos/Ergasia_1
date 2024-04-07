import numpy as np
from itertools import combinations

def find_min_or_max(fz, intersections:np.array, type:str)->tuple:
    """
    Finds the minimum or maximum value of a function (2 decision variables) at the given intersections.

    Args:
        fz: The function to be optimized.
        intersections: The intersections of the constraints.
        type: The type of the optimization. It can be either "min" or "max".
    Returns:
        A tuple containing the minimum or maximum value of the function and the point where it occurs.
    """

    assert type in ["min", "max"], "The type must be either 'min' or 'max'."
    if type == "max":

        index = 0
        maxima = -np.inf
        for i, intersection in enumerate(intersections):
            z = fz(intersection[0], intersection[1])
            if z > maxima:
                maxima = z
                index = i
        print(f"Κορυφές:\n {intersections}")
        return maxima, intersections[index]
    elif type == "min":
        
        index = 0
        minima = np.inf
        for i, intersection in enumerate(intersections):
            z = fz(intersection[0], intersection[1])
            if z < minima:
                minima = z
                index = i
        print(f"Κορυφές:\n {intersections}")
        return minima, intersections[index]

# Combinations
def nCr_combs(arr, r):
    return list(combinations(arr, r))

def all_non_positive(arr):
    return np.all(arr <= 0.)

def contains_positive(arr):
    return np.any(arr > 0)

def contains_negative(arr):
    return np.any(arr < 0)

def contains_zero(arr):
    return np.any(arr == 0)

def nice_print_5a(arr):    
    print("hyperplanes  \t        x1\tx2\tx3\tx4")   
    for element in arr:
        print(f"{element[1]} \t\t{element[0][0]}\t{element[0][1]}\t{element[0][2]}\t{element[0][3]}")

def nice_print_5b(arr):
    for i in range(len(arr)):
        print(f"{arr[i][1]}\t\t     [{np.round(arr[i][0], 2)[0]}\t{np.round(arr[i][0], 2)[1]}\t{np.round(arr[i][0], 2)[2]}]")
    

    