import numpy as np
import matplotlib.pyplot as plt
from min_or_max import find_min_or_max

## Contraint functions
def f1(x): 
    return 500 - x

def f2(x): 
    return 400 - x

def f3(x):  
    return x / 3

def f4_a(x):
    return (6/4) * x

def f4_b(x):
    return x

def f5(x):
    return np.full_like(x, 250)

# Define the constraints
d = np.linspace(0, 500, 300)
x1, x2 = np.meshgrid(d, d)

x = np.linspace(-500, 500, 3000)

constraint1 = x1 + x2 <= 500
constraint2 = x1 + x2 >= 400
constraint3 = x1 - 3 * x2 <= 0
constraint4_a = .6 * x1 - .4 * x2 >= 0
constraint4_b = .5 * x1 - .5 * x2 >= 0
constraint5 = x2 <= 250
constraint6 = x1 >= 0
constraint7 = x2 >= 0

## Cptimization functions
def fz1(x1, x2):
    return 3 * x1 + 4 * x2

## Find the intersection points of the constraints
# Erwthma a
# constraint1 & constraint3
a1 = np.array([[1, 1], [1, -3]])
b1 = np.array([500, 0])
intersection1 = np.linalg.solve(a1, b1)

# constraint1 & constraint5
a2 = np.array([[1, 1], [0, 1]])
b2 = np.array([500, 250])
intersection2 = np.linalg.solve(a2, b2)

# constraint2 & constraint3
a3 = np.array([[1, 1], [1, -3]])
b3 = np.array([400, 0])
intersection3 = np.linalg.solve(a3, b3)

# constraint2 & constraint4
a4_a = np.array([[1, 1], [.6, -.4]])
b4_a = np.array([400, 0])
intersection4_a = np.linalg.solve(a4_a, b4_a)

a4_b = np.array([[1, 1], [.5, -.5]])
b4_b = np.array([400, 0])
intersection4_b = np.linalg.solve(a4_b, b4_b)

# constraint4 & constraint5
a5 = np.array([[.6, -.4], [0, 1]])
b5 = np.array([0, 250])
intersection5 = np.linalg.solve(a5, b5)

# Erwthma b

## Find the maximum value of the function
# Erwthma a
print(f"----------------------Ερώτημα α----------------------")
maxima, point = find_min_or_max(fz1, 
                                np.array([intersection1, intersection2, intersection3, intersection4_a, intersection5]), 
                                "max")

print(f"The maximum value of the function is: {maxima} at point {point} ")

# Erwthma b
print(f"----------------------Ερώτημα β----------------------")
maxima, point = find_min_or_max(fz1, 
                                 np.array([intersection1, intersection2, intersection3, intersection4_b, intersection5]), 
                                "max")

print(f"The maximum value of the function is: {maxima} at point {point} ")

## Plots
plt.figure(figsize=(10, 6))  # Increase the figure size
# Erwthma a
# Feasible region
plt.subplot(1, 2, 1)
plt.imshow( ((constraint1 & constraint2 & constraint3 & constraint4_a & constraint5 & constraint6 & constraint7) ).astype(int), 
                extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha = 0.3)

# Constraint plots
plt.plot(x, f1(x), label='x1 + x2 <= 500')
plt.plot(x, f2(x), label='x1 + x2 >= 400')
plt.plot(x, f3(x), label='x1 - 3 * x2 <= 0')
plt.plot(x, f4_a(x), label='0.6 * x1 - 0.4 * x2 >= 0')
plt.plot(x, f5(x), label='x2 <= 250')

# Ιntersection points
plt.plot(intersection1[0], intersection1[1], 'ro')
plt.plot(intersection2[0], intersection2[1], 'ro')
plt.plot(intersection3[0], intersection3[1], 'ro')
plt.plot(intersection4_a[0], intersection4_a[1], 'ro')
plt.plot(intersection5[0], intersection5[1], 'ro')

# Sauces
plt.xlim(0, 500)
plt.ylim(0, 500)
plt.legend()


# Erwthma b
# Feasible region
plt.subplot(1, 2, 2)
plt.imshow(((constraint1 & constraint2 & constraint3 & constraint4_b & constraint5 & constraint6 & constraint7)).astype(int),
           extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha=0.3)

# Constraint plots
plt.plot(x, f1(x), label='x1 + x2 <= 500')
plt.plot(x, f2(x), label='x1 + x2 >= 400')
plt.plot(x, f3(x), label='x1 - 3 * x2 <= 0')
plt.plot(x, f4_b(x), label='0.5 * x1 - 0.5 * x2 >= 0')
plt.plot(x, f5(x), label='x2 <= 250')

# Ιntersection points
plt.plot(intersection1[0], intersection1[1], 'ro')
plt.plot(intersection2[0], intersection2[1], 'ro')
plt.plot(intersection3[0], intersection3[1], 'ro')
plt.plot(intersection4_b[0], intersection4_b[1], 'ro')

# Sauces
plt.xlim(0, 500)
plt.ylim(0, 500)
plt.legend()

plt.show()