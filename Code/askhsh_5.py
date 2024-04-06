import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from itertools import combinations
from modules import remove_nan

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

# Coefficients of the objective function
c = np.array([-2, 1, -4, 3])
# Coefficients of the inequality constraints
g1 = np.array([1, 1, 3, 2,])
g2 = np.array([1, 0, -2, 1])
g3 = np.array([2, 1, 0, 0,])
g4 = np.array([1, 0, 0, 0,])
g5 = np.array([0, 1, 0, 0,])
g6 = np.array([0, 0, 1, 0,])
g7 = np.array([0, 0, 0, 1,])

b = np.array([4, 2, 3, 0, 0, 0, 0])

p1 = np.array([*g1, b[0]])
p2 = np.array([*g2, b[1]])
p3 = np.array([*g3, b[2]])
p4 = np.array([*g4, b[3]])
p5 = np.array([*g5, b[4]])
p6 = np.array([*g6, b[5]])
p7 = np.array([*g7, b[6]])

# Augmented matrix of the coefficients of the inequality constraints
A = np.array([p1, p2, p3, p4, p5, p6, p7])

# Solving 35 4x4 linear systems
combs = nCr_combs(A, len(c))
solutions = np.zeros((len(combs), len(c)))
for i in range(len(combs)):
    augmented = np.array(combs[i])
    a = augmented[:, :-1]
    b = augmented[:, -1]
    try:
        solutions[i] = np.linalg.solve(a, b)
    except:
        solutions[i] = [None, None, None, None]
        continue

solutions = remove_nan(solutions)
print(f"vertices of polytope:\n{solutions}")
print("----------------------------")

# Filtering the solutions that satisfy the constraints
filtered_solutions = np.zeros((len(combs), len(c)))
for i in range(len(solutions)):
    if  c1(*solutions[i]) \
    and c2(*solutions[i]) \
    and c3(*solutions[i]) \
    and c4(*solutions[i]) \
    and c5(*solutions[i]) \
    and c6(*solutions[i]) \
    and c7(*solutions[i]):
        filtered_solutions[i] = solutions[i]
    else:
        filtered_solutions[i] = [None, None, None, None]
filtered_solutions = remove_nan(filtered_solutions)
print(f"vertices of polytope of feasible solutions:\n{filtered_solutions}")
print("----------------------------")

# Calculating the value of the objective function for the feasible solutions
# z = np.zeros((len(filtered_solutions), 1))
# for i in range(len(filtered_solutions)):
#     z[i] = (fz(*filtered_solutions[i]))
# print(f"feasible solutions:\n{z}")
# print("----------------------------")

# Sorting the feasible solutions
# print(f"sorted feasible solutions:\n{np.sort(z, axis=0)}")
# print("----------------------------")

# Finding the degenerate vertices and solutions
degenerate_vertices = np.array([x for x in filtered_solutions if np.count_nonzero(np.all(filtered_solutions == x, axis=1)) > 1])
print(f"degenerate_vertices:\n{np.unique(degenerate_vertices, axis=0)}")
print("----------------------------")

# degenerate_solutions = np.array([x for x in z if np.count_nonzero(np.all(z == x, axis=1)) > 1])
# print(f"degenerate_solutions:\n{np.unique(degenerate_solutions, axis=0)}")
# print("----------------------------")








# a = np.array([[1, 1, 3, 2], [1, 0, -2, 1], [2, 1, 0, 0]])
# print(a)

# item_del = np.array([2, 1, 0, 0])

# item_del_index = np.where(np.all(a == item_del, axis=1))[0][0]
# print(item_del_index)

# a = np.delete(a, item_del_index, 0)
# print(a)









