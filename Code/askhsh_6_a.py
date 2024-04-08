import numpy as np
import warnings
from modules import present_optimal_solution, present_tableau, contains_positive
warnings.filterwarnings("ignore", category=RuntimeWarning) 


def simplex_method_optimal(c:np.array, A:np.array, b:np.array)->None:
    """
    Solves a linear programming problem using the Simplex Method and prints each tableu step in terminal.
    Args:
        c: The coefficients of the objective function.
        A: The coefficients of the constraints.
        b: The right-hand side of the constraints.
    Returns:
        None
    """
    # Adding slack variables
    c_B = np.append(c, np.zeros(len(A)))
    A_s = np.column_stack((A, np.eye(len(A))))

    z = np.zeros(len(c_B))
    c_z = np.ones(len(c_B))
    iters = 0
    basic_variables = [i for i in range(len(c), len(c_B))]

    while contains_positive(c_z):

        # Initial Simplex Tableau
        if iters == 0:
            print(f"\nInitial Simplex Tableau:")
            print(f"starting basic variables: ", end="")
            for var in range(len(basic_variables)):
                print(f"x{basic_variables[var]+1}", end=" ")
            temp1 = [ c_B[basic_variables[i]] for i in range(len(basic_variables))]
            for j in range(len(z)):
                temp2 = A_s[:, j]
                z_j = temp1 @ temp2
                z[j] = z_j
            c_z = c_B - z
            z_value = temp1 @ b
            present_tableau(temp1, A_s, b, z, c_z, z_value, basic_variables, c_B)
        
        else:
            print(f"\n\nIteration {iters}:")
            pivot_column = np.where(c_z == np.max(c_z))[0][0]

            # Κριτήριο ελαχίστου λόγου
            ratios = []
            for i in range(len(b)):
                try:
                    ratio = b[i] / A_s[i][pivot_column]
                    if ratio < 0:
                        ratio = np.inf
                        ratios.append(ratio)
                    else:
                        ratios.append(ratio)
                except:
                    ratio = np.inf
                    ratios.append(ratio)

            min_ratio = min(ratios)
            if min_ratio == 0:
                ratios.remove(0)
                min_ratio = min(ratios)
            pivot_row = ratios.index(min_ratio)

            # New basic variables
            basic_variables[pivot_row] = pivot_column

            # Gaussian elimination
            pivot_element = A_s[pivot_row][pivot_column]

            A_s[pivot_row] = A_s[pivot_row] / pivot_element

            a = b[pivot_row] / pivot_element
            b[pivot_row] = a

            for i in range(len(A_s)):
                if i != pivot_row:
                    el = A_s[i][pivot_column]
                    A_s[i] = A_s[i] - ( el  * A_s[pivot_row] )

                    b[i] = b[i] - (  el  * b[pivot_row] )

            temp1 = [ c_B[basic_variables[i]] for i in range(len(basic_variables))]
            for j in range(len(z)):
                temp2 = A_s[:, j]
                z_j = temp1 @ temp2
                z[j] = z_j
            
            c_z = c_B - z
            z_value = temp1 @ b
            present_tableau(temp1, A_s, b, z, c_z, z_value, basic_variables, c_B)

        iters += 1
    
    present_optimal_solution(z_value, c_B, b, basic_variables)
σ
if __name__ == "__main__":


    # All arrays must be numpy arrays with dtype=float
    c = np.array([5., 4., -1., 3.])
    a1 = np.array([3., 2., -3., 1.])
    a2 = np.array([3., 3., 1., 3.])
    A = np.array([a1, a2])
    b = np.array([24., 36.])
    simplex_method_optimal(c, A, b)
    
    # Random example
    # c = np.array([7., 6.])
    # a1 = np.array([2., 4.])
    # a2 = np.array([3., 2.])
    # A = np.array([a1, a2])
    # b = np.array([16., 12.])
    # simplex_method(c, A, b)

    # Dovetail
    # c = np.array([3., 2.])
    # a1 = np.array([1., 1.])
    # a2 = np.array([3., 1.])
    # a3 = np.array([1., 0.])
    # a4 = np.array([0., 1.])
    # A = np.array([a1, a2, a3, a4])
    # b = np.array([9., 18., 7., 6.])
    # simplex_method(c, A, b)

