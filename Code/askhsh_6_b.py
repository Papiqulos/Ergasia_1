import numpy as np
import warnings
from modules import present_optimal_solution, present_tableau, contains_positive
warnings.filterwarnings("ignore", category=RuntimeWarning) 


def simplex_method_different_paths(c, A, b, path):

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
            pos_c_z = np.where(c_z > 0)[0]
            print(f"pos_c_z: {pos_c_z}")

            if iters == 1:
                # pivot_column = np.where(c_z == np.max(c_z))[0][0]
                pivot_column = pos_c_z[2]
                print(f"pivot_column: {pivot_column}")
            elif iters == 2:
                # pivot_column = np.where(c_z == np.max(c_z))[0][0]
                pivot_column = pos_c_z[1]
                print(f"pivot_column: {pivot_column}")
            elif iters == 4:
                # pivot_column = np.where(c_z == np.max(c_z))[0][0]
                pivot_column = pos_c_z[1]
                print(f"pivot_column: {pivot_column}")
            else:
                pivot_column = np.where(c_z == np.max(c_z))[0][0]
                print(f"pivot_column: {pivot_column}")
                        
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

            print(f"ratios: {ratios}")
            if np.inf in ratios and 0 in ratios:
                print(f"Non-feasible solution")
                # break
            elif 0 in ratios and np.inf not in ratios:
                print(f"Degenerate solution")
                # break
            else:
                min_ratio = min(ratios)
                pivot_row = ratios.index(min_ratio)
            
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
        # if iters == 5:
        #     break
    present_optimal_solution(z_value, c_B, b, basic_variables)



if __name__ == "__main__":

    c = np.array([5., 4., -1., 3.])
    a1 = np.array([3., 2., -3., 1.])
    a2 = np.array([3., 3., 1., 3.])
    A = np.array([a1, a2])
    b = np.array([24., 36.])

    # Dovetail
    # c = np.array([3., 2.])
    # a1 = np.array([1., 1.])
    # a2 = np.array([3., 1.])
    # a3 = np.array([1., 0.])
    # a4 = np.array([0., 1.])
    # A = np.array([a1, a2, a3, a4])
    # b = np.array([9., 18., 7., 6.])
    
    simplex_method_different_paths(c, A, b, 1)