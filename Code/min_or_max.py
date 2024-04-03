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
        print(f"Κρίσιμα σημέια: {intersections}")
        return maxima, intersections[index]
    elif type == "min":
        
        index = 0
        minima = np.inf
        for i, intersection in enumerate(intersections):
            z = fz1(intersection[0], intersection[1])
            if z < minima:
                minima = z
                index = i
        print(f"Κρίσιμα σημέια: {intersections}")
        return minima, intersections[index]
