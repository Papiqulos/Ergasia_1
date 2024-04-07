import numpy as np
import math
from modules import nCr_combs, all_non_positive, contains_positive



## Our optimization problem
# Objective function coefficients
c = np.array([5, 4, -1, 3])

# Constraints coefficients
a1 = np.array([3, 2, -3, 1])
a2 = np.array([3, 3, 1, 3])
A = np.array([a1, a2])

b = np.array([24, 36])

# Adding slack variables
c_B = np.append(c, np.zeros(2))
A_s = np.column_stack((A, np.eye(2)))

z = []
# combos = math.comb(len(c_B), len(b))
# basic_variables = np.linspace(0, 5, 6, dtype=int)
# basic_variables = nCr_combs(basic_variables, 2)

# for i, basic_vars in enumerate(basic_variables):
#     print(f"Combination {i+1}: {basic_vars}")

z = np.zeros(6)
c_z = np.ones(6)
i = 0
basic_variables = [4, 5]

while contains_positive(c_z):
    # Initial Simplex Tableau
    if i == 0:
        print(f"Iteration {i+1}:")
        print(f"starting basic variables: x{basic_variables[0]+1}, x{basic_variables[1]+1}")
        temp1 = [ c_B[basic_variables[0]], c_B[basic_variables[1]] ]
        for j in range(len(z)):
            temp2 = A_s[:, j]
            z_j = temp1 @ temp2
            z[j] = z_j
        print(f"-c_B : \n{np.array([temp1]).T}")
        print(f"-A_s : \n{np.round(A_s, 2)}")
        print(f"-b : \n{np.array([b]).T}")
        print(f"-z : \n{np.round(z, 2)}")
        c_z = c_B - z
        print(f"-c-z : \n{np.round(c_z, 2)}")
        z_value = temp1 @ b
        print(f"Value of the objective function: {z_value}")
    
    else:
        print(f"\nIteration {i+1}:")
        pivot_column = np.where(c_z == np.max(c_z))[0][0]
        print(f"pivot column: {pivot_column+1}")
        # print(f"new basic variable: x{pivot_column+1}")
        try:
            ratio1 = b[0] / A_s[0][pivot_column]
        except ZeroDivisionError:
            ratio1 = np.inf

        try:
            ratio2 = b[0] / A_s[1][pivot_column]
        except ZeroDivisionError:
            ratio2 = np.inf

        if ratio1 == ratio2:
            print("Ratios are equal")
            ratios = [ratio1, ratio2]
            min_ratio = ratio1
            pivot_row = ratios.index(min_ratio)
            print(f"pivot row: {pivot_row+1}")
            # print(f"Min ratio: {min_ratio}\nRow of basic variable to change: {ratio_index}")
        else:
            ratios = [ratio1, ratio2]
            min_ratio = min(ratios)
            pivot_row = ratios.index(min_ratio)
            print(f"pivot row: {pivot_row+1}")
            # print(f"Ratios: {ratio1}, {ratio2}")
            # print(f"Min ratio: {min_ratio}\nRow of basic variable to change: {ratio_index}")
        
        basic_variables[pivot_row] = pivot_column
        print(f"new basic variables: x{basic_variables[0]+1}, x{basic_variables[1]+1}")

        # Gaussian elimination

        pivot_element = A_s[pivot_row][pivot_column]

        A_s[pivot_row] = A_s[pivot_row] / pivot_element
        b[pivot_row] = b[pivot_row] / pivot_element

        A_s[1-pivot_row] = A_s[1-pivot_row] - ( ( A_s[1-pivot_row][pivot_column] ) * A_s[pivot_row] )
        b[1-pivot_row] = b[1-pivot_row] - ( ( A_s[1-pivot_row][pivot_column] ) * b[pivot_row] )

        temp1 = [ c_B[basic_variables[0]], c_B[basic_variables[1]] ]
        for j in range(len(z)):
            temp2 = A_s[:, j]
            z_j = temp1 @ temp2
            z[j] = z_j
        print(f"-c_B : \n{np.array([temp1]).T}")
        print(f"-A_s : \n{np.round(A_s, 2)}")
        print(f"-b : \n{np.array([b]).T}")
        print(f"-z : \n{np.round(z, 2)}")
        c_z = c_B - z
        print(f"-c-z : \n{np.round(c_z, 2)}")
        z_value = temp1 @ b
        print(f"Value of the objective function: {z_value}")

    if i == 2:
        break
    i += 1

                                               


