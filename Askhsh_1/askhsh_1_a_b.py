import numpy as np
import matplotlib.pyplot as plt


# Contraint functions
def f1(x): # >=
    return 10 - x

def f2(x): # <=
    return 10 + 10 * x

def f3(x):  # <=
    return 20 + 4 * x

def f4(x): # >=
    return 5 - x / 4

# Cptimization functions
def fz1(x1, x2):
    return 2 * x1 - x2

def fz2(x1, x2):
    return 11 * x1 - x2

# Define the constraints
d = np.linspace(0, 35, 300)
x1, x2 = np.meshgrid(d, d)

x = np.linspace(-100, 100, 3000)

constraint1 = x1 + x2 >= 10
constraint2 = -10 * x1 + x2 <= 10
constraint3 = -4 * x1 + x2 <= 20
constraint4 = x1 + 4 * x2 >= 20
constraint5 = x1 >= 0
constraint6 = x2 >= 0

# Find the intersection points of the constraints
a1 = np.array([[1, 1], [-10, 1]])
b1 = np.array([10, 10])
intersection1 = np.linalg.solve(a1, b1)

a2 = np.array([[-10, 1], [-4, 1]])
b2 = np.array([10, 20])
intersection2 = np.linalg.solve(a2, b2)

a3 = np.array([[1, 1], [1, 4]])
b3 = np.array([10, 20])
intersection3 = np.linalg.solve(a3, b3)

intersection4 = [20, 0]

# Erwthma a
intersections = [intersection1, intersection2, intersection3, intersection4]
print(intersections)
index = 0
minima = np.inf
for i, intersection in enumerate(intersections):
    z = fz1(intersection[0], intersection[1])
    if z < minima:
        minima = z
        index = i

print(f"The minimum value of the function is: {minima} at point {intersections[index]} ")

# Erwthma b
index = 0
minima = np.inf
for i, intersection in enumerate(intersections):
    z = fz2(intersection[0], intersection[1])
    if z < minima:
        minima = z
        index = i

print(f"The minimum value of the function is: {minima} at point {intersections[index]} ")

## Plots
# Feasible region
plt.imshow( ((constraint1 & constraint2 & constraint3 & constraint4 & constraint5 & constraint6) ).astype(int), 
                extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha = 0.3)

# Constraint plots
plt.plot(x, f1(x), label='x1 + x2 >= 10')
plt.plot(x, f2(x), label='-10x1 + x2 <= 10')
plt.plot(x, f3(x), label='-4x1 + x2 <= 20')
plt.plot(x, f4(x), label='x1 + 4x2 >= 20')

# Ιntersection points
plt.plot(intersection1[0], intersection1[1], 'ro')
plt.plot(intersection2[0], intersection2[1], 'ro')
plt.plot(intersection3[0], intersection3[1], 'ro')
plt.plot(intersection4[0], intersection4[1], 'ro')

# Sauces
plt.xlim(-1, 35)
plt.ylim(-1, 35)
plt.legend()
plt.show()





