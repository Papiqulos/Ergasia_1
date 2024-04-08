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

def nCr_combs(arr:np.array, r:int)->list:
    """
    Returns all possible combinations of r elements from an array.
    Args:
        arr: The array to be used.
        r: The number of elements in each combination.
    Returns:
        A list containing all possible combinations of r elements from the array.
    """
    return list(combinations(arr, r))

def all_non_positive(arr:np.array)->bool:
    """
    Checks if all elements of an array are non-positive.
    Args:
        arr: The array to be checked.
    Returns:
        True if all elements are non-positive, False otherwise.
    """
    return np.all(arr <= 0.)

def contains_positive(arr:np.array)->bool:
    """
    Checks if an array contains positive elements.
    Args:
        arr: The array to be checked.
    Returns:
        True if the array contains positive elements, False otherwise.
    """
    return np.any(arr > 0)

def contains_negative(arr:np.array)->bool:
    """
    Checks if an array contains negative elements.
    Args:
        arr: The array to be checked.
    Returns:
        True if the array contains negative elements, False otherwise.
    """
    return np.any(arr < 0)

def contains_zero(arr:np.array)->bool:
    """
    Checks if an array contains zero elements.
    Args:
        arr: The array to be checked.
    Returns:
        True if the array contains zero elements, False otherwise.
    """
    return np.any(arr == 0)

# Prettier printing
def nice_print_vertices(arr:list)->None:    
    """
    Prints the vertices of a polytope in a nice format.
    Args:
        arr: The vertices of the polytope.
    Returns:
        None

    """
    print("hyperplanes  \t        x1\tx2\tx3\tx4")   
    for element in arr:
        print(f"{element[1]} \t\t{element[0][0]}\t{element[0][1]}\t{element[0][2]}\t{element[0][3]}")

def nice_print_solutions(arr:list)->None:
    """
    Prints the solutions of a system of equations in a nice format.
    Args:
        arr: The solutions of the system of equations.
    Returns:
        None

    """
    for i in range(len(arr)):
        print(f"{arr[i][1]}\t\t     [{np.round(arr[i][0], 2)[0]}\t{np.round(arr[i][0], 2)[1]}\t{np.round(arr[i][0], 2)[2]}]")   

def nice_print_a(vertices:list, feasible_vertices:list, degenerate_vertices:list, vert_only:np.array)->None:
    """
    Prints the vertices of a polytope, the feasible vertices and the degenerate vertices in a nice format.
    Args:
        vertices: The vertices of the polytope.
        feasible_vertices: The vertices that satisfy the constraints.
        degenerate_vertices: The degenerate vertices.
        vert_only: The vertices of the polytope without the hyperplanes.
    Returns:
        None

    """
    # Printing the solutions and the hyperplanes they belong to
    print("-------------------------------------------")
    print(f"Number of vertices of polytope: {len(vertices)}")
    nice_print_vertices(vertices)

    # Printing the solutions that satisfy the constraints and the hyperplanes they belong to
    print("-------------------------------------------")
    print(f"Number of vertices in feasible region: {len(feasible_vertices)}")
    nice_print_vertices(feasible_vertices)

    # Printing the degenerate vertices and the hyperplanes they belong to
    print("-------------------------------------------")
    print(f"Number of degenerate vertices: {len(degenerate_vertices)}")
    print("hyperplanes  \t        x1\tx2\tx3\tx4")
    for i, vertex in enumerate(degenerate_vertices):
        indices = np.where(np.all(vert_only == vertex, axis=1))[0]
        print(f"{feasible_vertices[indices[i]][1]} \t\t{degenerate_vertices[i][0]}\t{degenerate_vertices[i][1]}\t{degenerate_vertices[i][2]}\t{degenerate_vertices[i][3]}")

def nice_print_b(general_solutions:list, feasible_solutions:list, degenerate_solutions:list, z:list, maxima:float)->None:
    """
    Prints the general solutions, the feasible solutions, the degenerate solutions and the value of the objective function in a nice format.
    Args:
        general_solutions: The general solutions.
        feasible_solutions: The feasible solutions.
        degenerate_solutions: The degenerate solutions.
        z: The value of the objective function for every feasible solution.
        maxima: The optimal solution.
    Returns:
        None

    """
    # Printing the general solutions and their according basic variables
    print("------------------------------------------")
    print(f"Number of general solutions: {len(general_solutions)}")
    print(f"basic variables\t\t     general solution")
    nice_print_solutions(general_solutions)

    # Printing the feasible solutions and their according basic variables  
    print("------------------------------------------")
    print(f"Number of feasible solutions: {len(feasible_solutions)}")
    print(f"basic variables\t\t     feasible solution")
    nice_print_solutions(feasible_solutions)

    # Printing the degenerate solutions and their according basic variables 
    print("------------------------------------------")
    print(f"Number of degenerate solutions: {len(degenerate_solutions)}")
    print(f"basic variables\t\t     degenerate solution")
    nice_print_solutions(degenerate_solutions)

    # Printing the value of the objective function for every feasible solution and their according basic variables
    print("------------------------------------------")
    print(f"basic variables\t\t     value of the objective function")
    for i in z:
        print(f"{i[1]}\t\t     {i[0]:.2f}")
        
    print("------------------------------------------")
    print(f"Optimal solution: {maxima:.2f}")

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