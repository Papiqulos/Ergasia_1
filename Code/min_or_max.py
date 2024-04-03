import numpy as np

def find_min_or_max(fz1, intersections, type):
    if type == "max":
        index = 0
        maxima = -np.inf
        for i, intersection in enumerate(intersections):
            z = fz1(intersection[0], intersection[1])
            if z > maxima:
                maxima = z
                index = i
        return maxima, intersections[index]
    else:
        index = 0
        minima = np.inf
        for i, intersection in enumerate(intersections):
            z = fz1(intersection[0], intersection[1])
            if z < minima:
                minima = z
                index = i
        return minima, intersections[index]
