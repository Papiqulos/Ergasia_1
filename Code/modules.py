import numpy as np

def find_min_or_max(fz, intersections:np.array, type:str)->tuple:
    """
    Finds the minimum or maximum value of a function at the given intersections.

    Args:
        fz1: The function to be optimized.
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
    
