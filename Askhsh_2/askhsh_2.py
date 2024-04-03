import numpy as np
import matplotlib.pyplot as plt


# Contraint functions
def f1(x): 
    return 500 - x

def f2(x): 
    return 400 - x

def f3(x):  
    return x / 3

def f4(x):
    return (-3/4) * x

def f5(x):
    return np.full_like(x, 250)


# Cptimization functions
def fz1(x1, x2):
    return 

# Define the constraints
d = np.linspace(0, 500, 300)
x1, x2 = np.meshgrid(d, d)

x = np.linspace(-500, 500, 3000)

constraint1 = x1 + x2 <= 500
constraint2 = x1 + x2 <= 400
constraint3 = x1 - 3 * x2 <= 0
constraint4 = .3 * x1 + .4 * x2 <= 0
constraint5 = x2 <= 250
constraint6 = x1 >= 0
constraint7 = x2 >= 0

# Find the intersection points of the constraints


# Erwthma a


# print(f"The minimum value of the function is: {minima} at point {intersections[index]} ")

## Plots
# Feasible region
plt.imshow( ((constraint1 & constraint2 & constraint3 & constraint4 & constraint5 & constraint6 & constraint7) ).astype(int), 
                extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha = 0.3)

# Constraint plots
plt.plot(x, f1(x), label='x1 + x2 <= 500')
plt.plot(x, f2(x), label='x1 + x2 <= 400')
plt.plot(x, f3(x), label='x1 - 3 * x2 <= 0')
plt.plot(x, f4(x), label='0.3 * x1 + 0.4 * x2 <= 0')
plt.plot(x, f5(x), label='x2 <= 250')



# Ιntersection points
# plt.plot(intersection1[0], intersection1[1], 'ro')
# plt.plot(intersection2[0], intersection2[1], 'ro')
# plt.plot(intersection3[0], intersection3[1], 'ro')
# plt.plot(intersection4[0], intersection4[1], 'ro')

# Sauces
plt.xlim(-1, 500)
plt.ylim(-1, 500)
plt.legend()
plt.show()