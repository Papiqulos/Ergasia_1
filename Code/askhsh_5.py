import numpy as np
import math
from modules import nCr_combs, contains_negative, contains_zero, nice_print_a, nice_print_b

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

def erwthma_a():
    
    # Coefficients of the objective function
    c = np.array([-2., 1., -4., 3.])

    # Coefficients of the inequality constraints
    g1 = np.array([1., 1., 3., 2.])
    g2 = np.array([1., 0., -1., 1.])
    g3 = np.array([2., 1., 0., 0.])

    g4 = np.array([1., 0., 0., 0.])
    g5 = np.array([0., 1., 0., 0.])
    g6 = np.array([0., 0., 1., 0.])
    g7 = np.array([0., 0., 0., 1.])
    b = np.array([4., 2., 3., 0., 0., 0., 0.])

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
    indices = np.linspace(0, len(b)-1, len(b), dtype=int)
    indices = nCr_combs(indices, len(c))
    vertices = []
    for i in range(len(combs)):
        augmented = np.array(combs[i])
        a = augmented[:, :-1]
        b_ = augmented[:, -1]
        try:
            vertices.append((np.round(np.linalg.solve(a, b_), 2), indices[i])) 
        except np.linalg.LinAlgError:
            continue
    
    ## Finding the feasible solutions and the hyperplanes they belong to
    feasible_vertices = []
    for i in range(len(vertices)):
        if  c1(*vertices[i][0]) \
        and c2(*vertices[i][0]) \
        and c3(*vertices[i][0]) \
        and c4(*vertices[i][0]) \
        and c5(*vertices[i][0]) \
        and c6(*vertices[i][0]) \
        and c7(*vertices[i][0]):
            feasible_vertices.append(vertices[i])
        else:
            continue
    
    ## Finding the degenerate vertices and the hyperplanes they belong to
    vert_only = np.array([element[0] for element in feasible_vertices])
    degenerate_vertices = np.array([x for x in vert_only if np.count_nonzero(np.all(vert_only == x, axis=1)) > 1])

    
    return vertices, feasible_vertices, degenerate_vertices, vert_only

def erwthma_b():
    # Coefficients of the objective function
    c = np.array([-2, 1, -4, 3])

    # Coefficients of the inequality constraints
    g1 = np.array([1., 1., 3., 2.])
    g2 = np.array([1., 0., -1., 1.])
    g3 = np.array([2., 1., 0., 0.])

    b = np.array([4., 2., 3.])

    ## Adding slack variables
    # Coefficients of the objective function with the addition of the slack variables
    c_s = np.array([*c, 0., 0., 0.])

    # Coefficients of the inequality constraints with the addition of the slack variables
    g1_s = np.array([*g1, 1., 0., 0.])
    g2_s = np.array([*g2, 0., 1., 0.])
    g3_s = np.array([*g3, 0., 0., 1.])

    A_s = np.array([g1_s, g2_s, g3_s])

    combos = math.comb(len(g1_s), len(b))
    basic_variables = np.linspace(0, 6, 7, dtype=int)
    basic_variables = nCr_combs(basic_variables, 3)

    Bs = []

    Bs_inv = []

    # Finding every possible combination of the constraints (B matrices)
    for i in range(combos):
        Bs.append( ( np.array([ A_s[ :, basic_variables[i][0] ], A_s[ :, basic_variables[i][1] ], A_s[ :, basic_variables[i][2] ]]).T, basic_variables[i] ) )

    # Finding the inverse of every B matrix
    for i in range(combos):
        try:
            # print("---------------")
            Bs_inv.append( (np.linalg.inv(Bs[i][0]), basic_variables[i]) )
        except:
            continue
    
    ## Finding all the possible general solutions and their basic variables
    general_solutions = []
    for i in range(len(Bs_inv)):
        try:
            x_b = Bs_inv[i][0] @ b
            general_solutions.append( (x_b, basic_variables[i]) )
            
        except:
            continue

    

    ## Finding which of the solutions are feasible and degenerate 
    feasible_solutions = []
    degenerate_solutions = []
    for i in range(len(general_solutions)):
        if contains_negative(general_solutions[i][0]) == False:
            feasible_solutions.append( general_solutions[i] )
        if contains_zero(general_solutions[i][0]) == True:
            degenerate_solutions.append( general_solutions[i] )

    

    ## Finding the optimal solution
    # Calculating the value of the objective function for every feasible solution
    z = []
    for i in range(len(feasible_solutions)):
        # Selecting the coefficients of the basic variables
        c_b  = [ c_s[ feasible_solutions[i][1][0] ], c_s[ feasible_solutions[i][1][1] ], c_s[ feasible_solutions[i][1][2] ] ]
        z.append( ( c_b @ feasible_solutions[i][0], feasible_solutions[i][1]) )
    
    
    
    # Finding the optimal solution
    values_only = [i[0] for i in z]
    maxima = -np.inf
    for value in values_only:
        if value > maxima:
            maxima = value
    
    

    return general_solutions, feasible_solutions, degenerate_solutions, z, maxima

if __name__ == "__main__":

    vertices, feasible_vertices, degenerate_vertices, vert_only = erwthma_a()
    nice_print_a(vertices, feasible_vertices, degenerate_vertices, vert_only)

    general_solutions, feasible_solutions, degenerate_solutions, z, maxima = erwthma_b()
    nice_print_b(general_solutions, feasible_solutions, degenerate_solutions, z, maxima)

    # There was an attempt...
    # feasible solutions that correspond to the feasible vertices
    
    # for solution, basic_vars in feasible_solutions:
    #     for vertice, hyperplane in feasible_vertices:
    #         var_arr = np.array([*basic_vars])
    #         if  np.all(var_arr <= 3):
    #             # print(f"basic variables: {basic_vars}")
    #             if solution[]
        
    # print("-------------------------------------------------")
    # for solution, basic_vars in feasible_solutions:
    #     var_arr = np.array([*basic_vars])
    #     if  np.any(var_arr > 3):
    #         print(f"basic variables: {basic_vars}")
        
                

                    

                
            
    
        

    







