import numpy as np
from itertools import combinations
from modules import remove_nan
import scipy

# Objective function
def fz(x1, x2, x3, x4):
    return -2 * x1 + x2 - 4 * x3 + 3 * x4

# Constraints
def c1(x1, x2, x3, x4):
    return x1 + x2 + 3 * x3 + 2 * x4 <= 4

def c2(x1, x2, x3, x4):
    return x1 + 0*x2 - x3 + x4 <= 2

def c3(x1, x2, x3, x4):
    return 2 * x1 + x2 + 0*x3 + 0*x4 <= 3

def c4(x1, x2, x3, x4):
    return x1 + 0*x2 + 0*x3 + 0*x4 >= 0

def c5(x1, x2, x3, x4):
    return 0*x1 + x2 + 0*x3 + 0*x4 >= 0

def c6(x1, x2, x3, x4):
    return 0*x1 + 0*x2 + x3 + 0*x4 >= 0

def c7(x1, x2, x3, x4):
    return 0*x1 + 0*x2 + 0*x3 + x4 >= 0

# Combinations
def nCr_combs(arr, r):
    return list(combinations(arr, r))


def main():
    

    # Coefficients of the objective function
    c = np.array([-2, 1, -4, 3])

    # Coefficients of the inequality constraints
    g1 = np.array([1, 1, 3, 2])
    g2 = np.array([1, 0, -1, 1])
    g3 = np.array([2, 1, 0, 0])

    g4 = np.array([1, 0, 0, 0])
    g5 = np.array([0, 1, 0, 0])
    g6 = np.array([0, 0, 1, 0])
    g7 = np.array([0, 0, 0, 1])
    b = np.array([4, 2, 3, 0, 0, 0, 0])

    # Augmented matrix of the coefficients of the inequality constraints
    p1 = np.array([*g1, b[0]])
    p2 = np.array([*g2, b[1]])
    p3 = np.array([*g3, b[2]])
    p4 = np.array([*g4, b[3]])
    p5 = np.array([*g5, b[4]])
    p6 = np.array([*g6, b[5]])
    p7 = np.array([*g7, b[6]])
    A = np.array([p1, p2, p3, p4, p5, p6, p7])
    # print(A)

    # Solving all possible combinations of the constraints
    combs = nCr_combs(A, len(c))
    indices = np.linspace(0, 6, 7)
    indices = nCr_combs(indices, 4)
    solutions = []
    for i in range(len(combs)):
        augmented = np.array(combs[i])
        a = augmented[:, :-1]
        b_ = augmented[:, -1]
        # print(a)
        # print("----")
        # print(b_)
        try:
            solutions.append((np.round(np.linalg.solve(a, b_), 2), indices[i])) 
        except np.linalg.LinAlgError:
            continue
    print(f"Vertices of polytope:{len(solutions)}")    
    print("hyperplane  \t        x1\tx2\tx3\tx4")   
    for element in solutions:
        print(f"{element[1]} \t{element[0][0]}\t{element[0][1]}\t{element[0][2]}\t{element[0][3]}")

    print("-------------------------------------------")

    # Filtering the solutions that satisfy the constraints
    filtered_solutions = []
    for i in range(len(solutions)):
        if  c1(*solutions[i][0]) \
        and c2(*solutions[i][0]) \
        and c3(*solutions[i][0]) \
        and c4(*solutions[i][0]) \
        and c5(*solutions[i][0]) \
        and c6(*solutions[i][0]) \
        and c7(*solutions[i][0]):
            filtered_solutions.append(solutions[i])
        else:
            continue
    print(f"Vertices in feasible region:{len(filtered_solutions)}")
    print("hyperplane  \t        x1\tx2\tx3\tx4")
    for element in solutions:
        print(f"{element[1]} \t{element[0][0]}\t{element[0][1]}\t{element[0][2]}\t{element[0][3]}")
    print("-------------------------------------------")

    # Finding the degenerate vertices
    arr = np.array([element[0] for element in filtered_solutions])
    degenerate_vertices = np.array([x for x in arr if np.count_nonzero(np.all(arr == x, axis=1)) > 1])
    print("Degenerate Vertices:")
    print("hyperplane  \t        x1\tx2\tx3\tx4")
    for i, vertex in enumerate(degenerate_vertices):
        indices = np.where(np.all(arr == vertex, axis=1))[0]
        print(f"{filtered_solutions[indices[i]][1]} \t{degenerate_vertices[i][0]}\t{degenerate_vertices[i][1]}\t{degenerate_vertices[i][2]}\t{degenerate_vertices[i][3]}")
    
if __name__ == "__main__":
    main()









