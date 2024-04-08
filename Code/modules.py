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

def present_tableau(temp1, A_s, b, z, c_z, z_value, basic_variables, c_B):
    print("\n")
    print("\t\t|", end="")
    for i in range(len(z)):
        print(f"\tx{i+1}", end="\t")
    print("|")
    
    print("Basis\tc_b\t|", end="")
    for j in range(len(c_B)):
        print(f"\t{np.round(c_B[j], 2)}", end="\t")
    print("|\tb")
    print(20*len(z)*"-")

    for i in range(len(basic_variables)):
        print(f"x{basic_variables[i]+1}\t{temp1[i]}\t|", end="")
        for j in range(len(z)):
            print(f"\t{np.round(A_s[i][j], 2)}", end="\t")
        print(f"|\t{np.round(b[i], 2)}")  
    print(20*len(z)*"-")

    print("z\t\t|", end="")
    for j in range(len(z)):
        print(f"\t{np.round(z[j], 2)}", end="\t")
    print(f"|\t{np.round(z_value, 2)}")
    print("c-z\t\t|", end="")
    for j in range(len(c_z)):
        print(f"\t{np.round(c_z[j], 2)}", end="\t")
    print(f"|\t")

def present_optimal_solution(z_value, c_B, b, basic_variables):
    print(f"\nOptimal solution: {z_value}", end="")
    result_dict = {}
    for i in range(len(c_B)):
        result_dict[f"x{i+1}"] = 0
    for i in range(len(basic_variables)):
        result_dict[f"x{basic_variables[i]+1}"] = b[i]      
    result_dict = dict(sorted(result_dict.items()))
    for key, value in result_dict.items():
        print(f"\nx{key[1:]} = {np.round(value, 2)}", end="")  