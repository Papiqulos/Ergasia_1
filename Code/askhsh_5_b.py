import numpy as np


def main():
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

    b = np.array([4, 2, 3])

    ## Adding slack variables
    # Coefficients of the objective function with the addition of the slack variables
    c_s = np.array([*c, 0, 0, 0])

    # Coefficients of the inequality constraints with the addition of the slack variables
    g1_s = np.array([*g1, 1, 0, 0])
    g2_s = np.array([*g2, 0, 1, 0])
    g3_s = np.array([*g3, 0, 0, 1])

    A_s = np.array([g1_s, g2_s, g3_s])
    print(A_s)

    B1 = np.array([A_s[:, 0], A_s[:, 1], A_s[:, 2]]).T
    print(B1)
    # c_b = np.array([c_s[0], c_s[1], c_s[2]])
    # print(c_b)
    # print(c_b @ B1 @ b)




if __name__ == '__main__':
    main()

