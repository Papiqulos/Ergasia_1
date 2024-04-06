# # Test
# B = np.array([[1, 0, 0, 0],
#               [-1, 1, 0, 0],
#               [0, 0, 1, 0],
#               [-1, 0, 0, 1]])

# b = np.array([9, 18, 7, 6])
# c1 = np.array([0, 0, 0, 0])

# print( c1 @ B @ b )


# Calculating the value of the objective function for the feasible solutions
# z = np.zeros((len(filtered_solutions), 1))
# for i in range(len(filtered_solutions)):
#     z[i] = (fz(*filtered_solutions[i]))
# print(f"feasible solutions:\n{z}")
# print("----------------------------")

# Sorting the feasible solutions
# print(f"sorted feasible solutions:\n{np.sort(z, axis=0)}")
# print("----------------------------")

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