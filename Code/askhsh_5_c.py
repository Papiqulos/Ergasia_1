# import numpy as np
# from modules import nCr_combs, contains_negative, contains_zero, nice_print_5b
# import math


# def main():
#     # Coefficients of the objective function
#     c = np.array([-2, 1, -4, 3])

#     # Coefficients of the inequality constraints
#     g1 = np.array([1, 1, 3, 2,])
#     g2 = np.array([1, 0, -1, 1])
#     g3 = np.array([2, 1, 0, 0,])

#     b = np.array([4, 2, 3])

#     ## Adding slack variables
#     # Coefficients of the objective function with the addition of the slack variables
#     c_s = np.array([*c, 0, 0, 0])

#     # Coefficients of the inequality constraints with the addition of the slack variables
#     g1_s = np.array([*g1, 1, 0, 0])
#     g2_s = np.array([*g2, 0, 1, 0])
#     g3_s = np.array([*g3, 0, 0, 1])

#     A_s = np.array([g1_s, g2_s, g3_s])

#     combos = math.comb(len(g1_s), len(b))
#     basic_variables = np.linspace(0, 6, 7, dtype=int)
#     basic_variables = nCr_combs(basic_variables, 3)

#     Bs = []

#     Bs_inv = []

#     # Finding every possible combination of the constraints (B matrices)
#     for i in range(combos):
#         Bs.append( ( np.array([ A_s[ :, basic_variables[i][0] ], A_s[ :, basic_variables[i][1] ], A_s[ :, basic_variables[i][2] ]]).T, basic_variables[i] ) )

#     # Finding the inverse of every B matrix
#     for i in range(combos):
#         try:
#             # print("---------------")
#             Bs_inv.append( (np.linalg.inv(Bs[i][0]), basic_variables[i]) )
#         except:
#             continue
    
#     ## Finding all the possible general solutions and their basic variables
#     general_solutions = []
#     for i in range(len(Bs_inv)):
#         try:
#             x_b = Bs_inv[i][0] @ b
#             general_solutions.append( (x_b, basic_variables[i]) )
            
#         except:
#             continue

#     # Printing the general solutions and their according basic variables
#     print("------------------------------------------")
#     print(f"Number of general solutions: {len(general_solutions)}")
#     print(f"basic variables\t\t     general solution")
#     nice_print_5b(general_solutions)

#     ## Finding which of the solutions are feasible and degenerate 
#     feasible_solutions = []
#     degenerate_solutions = []
#     for i in range(len(general_solutions)):
#         if contains_negative(general_solutions[i][0]) == False:
#             feasible_solutions.append( general_solutions[i] )
#         if contains_zero(general_solutions[i][0]) == True:
#             degenerate_solutions.append( general_solutions[i] )

#     # Printing the feasible solutions and their according basic variables  
#     print("------------------------------------------")
#     print(f"Number of feasible solutions: {len(feasible_solutions)}")
#     print(f"basic variables\t\t     feasible solution")
#     nice_print_5b(feasible_solutions)

#     # Printing the degenerate solutions and their according basic variables 
#     print("------------------------------------------")
#     print(f"Number of degenerate solutions: {len(degenerate_solutions)}")
#     print(f"basic variables\t\t     degenerate solution")
#     nice_print_5b(degenerate_solutions)

#     ## Finding the optimal solution
#     # Calculating the value of the objective function for every feasible solution
#     z = []
#     for i in range(len(feasible_solutions)):
#         # Selecting the coefficients of the basic variables
#         c_b  = [ c_s[ feasible_solutions[i][1][0] ], c_s[ feasible_solutions[i][1][1] ], c_s[ feasible_solutions[i][1][2] ] ]
#         z.append( ( c_b @ feasible_solutions[i][0], feasible_solutions[i][1]) )
    
#     # Printing the value of the objective function for every feasible solution and their according basic variables
#     print("------------------------------------------")
#     print(f"basic variables\t\t     value of the objective function")
#     for i in z:
#         print(f"{i[1]}\t\t     {i[0]:.2f}")
    
#     # Finding the optimal solution
#     values_only = [i[0] for i in z]
#     maxima = -np.inf
#     for value in values_only:
#         if value > maxima:
#             maxima = value
        
#     print("------------------------------------------")
#     print(f"Optimal solution: {maxima:.2f}")



# if __name__ == '__main__':
#     main()

