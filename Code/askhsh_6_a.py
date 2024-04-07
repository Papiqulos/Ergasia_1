import numpy as np
from modules import contains_positive
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) 

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

def simplex_method(c, A, b):

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
            print(f"\nIteration {iters+1}:")
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
            print(f"\n\nIteration {iters+1}:")
            pivot_column = np.where(c_z == np.max(c_z))[0][0]
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
    
    present_optimal_solution(z_value, c_B, b, basic_variables)

                                               

if __name__ == "__main__":

    c = np.array([5., 4., -1., 3.])
    a1 = np.array([3., 2., -3., 1.])
    a2 = np.array([3., 3., 1., 3.])
    A = np.array([a1, a2])
    b = np.array([24., 36.])
    simplex_method(c, A, b)
    
    # Random example
    # c = np.array([7., 6.])
    # a1 = np.array([2., 4.])
    # a2 = np.array([3., 2.])
    # A = np.array([a1, a2])
    # b = np.array([16., 12.])
    # simplex_method(c, A, b)

    # Dovetail
    c = np.array([3., 2.])
    a1 = np.array([1., 1.])
    a2 = np.array([3., 1.])
    a3 = np.array([1., 0.])
    a4 = np.array([0., 1.])
    A = np.array([a1, a2, a3, a4])
    b = np.array([9., 18., 7., 6.])
    simplex_method(c, A, b)

