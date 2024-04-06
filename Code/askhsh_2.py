import numpy as np
import matplotlib.pyplot as plt
from modules import find_min_or_max

## Contraints
def f1(x): 
    return 500 - x

def f2(x): 
    return 400 - x

def f3(x):  
    return x / 3

# Erwthma a
def f4_a(x):
    return (6/4) * x

# Erwthma b1
def f4_b1(x):
    return x

# Erwthma b2
def f4_b2(x):
    return (4/6)*x

def f5(x):
    return np.full_like(x, 250)

## Cptimization function
def fz(x1, x2):
    return 3 * x1 + 4 * x2

def main():
    # Define the constraints
    d = np.linspace(0, 500, 300)
    x1, x2 = np.meshgrid(d, d)

    x = np.linspace(-500, 500, 3000)

    constraint1 = x1 + x2 <= 500
    constraint2 = x1 + x2 >= 400
    constraint3 = x1 - 3 * x2 <= 0
    constraint4_a = .6 * x1 - .4 * x2 >= 0
    constraint4_b1 = .5 * x1 - .5 * x2 >= 0
    constraint4_b2 = .4 * x1 - .6 * x2 >= 0
    constraint5 = x2 <= 250
    constraint6 = x1 >= 0
    constraint7 = x2 >= 0

    feasible_region_a = constraint1 & constraint2 & constraint3 & constraint4_a & constraint5 & constraint6 & constraint7
    feasible_region_b1 = constraint1 & constraint2 & constraint3 & constraint4_b1 & constraint5 & constraint6 & constraint7
    feasible_region_b2 = constraint1 & constraint2 & constraint3 & constraint4_b2 & constraint5 & constraint6 & constraint7

    ## Intersections
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
    # Erwthma a
    a4_a = np.array([[1, 1], [.6, -.4]])
    b4_a = np.array([400, 0])
    intersection4_a = np.linalg.solve(a4_a, b4_a)

    # Erwthma b1
    a4_b = np.array([[1, 1], [.5, -.5]])
    b4_b = np.array([400, 0])
    intersection4_b1 = np.linalg.solve(a4_b, b4_b)

    # constraint4 & constraint5
    a5 = np.array([[.6, -.4], [0, 1]])
    b5 = np.array([0, 250])
    intersection5_b1 = np.linalg.solve(a5, b5)

    # Erwthma b2
    # constraint1 & constraint4
    a = np.array([[1, 1], [.4, -.6]])
    b = np.array([500, 0])
    intersection3_b2 = np.linalg.solve(a, b)

    # constraint2 & constraint4
    a = np.array([[1, 1], [.4, -.6]])
    b = np.array([400, 0])
    intersection4_b2 = np.linalg.solve(a, b)


    intersections_a = np.array([intersection1, intersection2, intersection3, intersection4_a, intersection5_b1])
    intersections_b1 = np.array([intersection1, intersection2, intersection3, intersection4_b1])
    intersections_b2 = np.array([intersection1, intersection3, intersection3_b2, intersection4_b2])

    ## Maxima
    # Erwthma a
    print(f"----------------------Ερώτημα α----------------------")
    maxima, point = find_min_or_max(fz, 
                                    intersections_a, 
                                    "max")

    print(f"The maximum value of the function is: {maxima} at point {point} ")

    # Erwthma b1
    print(f"----------------------Ερώτημα β με 50% χυμό πορτοκαλιού----------------------")
    maxima, point = find_min_or_max(fz, 
                                    intersections_b1, 
                                    "max")

    print(f"The maximum value of the function is: {maxima} at point {point} ")

    # Erwthma b2
    print(f"----------------------Ερώτημα β με 60% χυμό πορτοκαλιού----------------------")
    maxima, point = find_min_or_max(fz, 
                                    intersections_b2, 
                                    "max")

    print(f"The maximum value of the function is: {maxima} at point {point} ")

    ## Plots
    plt.figure(figsize=(10, 7))  # Increase the figure size
    # Erwthma a
    # Feasible region
    plt.subplot(2, 2, 1)
    plt.title("Ερώτημα α")
    plt.imshow( (feasible_region_a).astype(int), 
                    extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha = 0.3)

    # Constraint plots
    plt.plot(x, f1(x), label='x1 + x2 <= 500')
    plt.plot(x, f2(x), label='x1 + x2 >= 400')
    plt.plot(x, f3(x), label='x1 - 3x2 <= 0')
    plt.plot(x, f4_a(x), label='0.6x1 - 0.4x2 >= 0')
    plt.plot(x, f5(x), label='x2 <= 250')

    # Ιntersection points
    for intersection in intersections_a:
        plt.plot(*intersection, 'ro')

    # Sauces
    plt.xlim(0, 500)
    plt.ylim(0, 500)
    plt.legend()

    # Erwthma b1
    # Feasible region
    plt.subplot(2, 2, 2)
    plt.title("Ερώτημα β me 50% χυμό πορτοκαλιού")
    plt.imshow((feasible_region_b1).astype(int),
            extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha=0.3)

    # Constraint plots
    plt.plot(x, f1(x), label='x1 + x2 <= 500')
    plt.plot(x, f2(x), label='x1 + x2 >= 400')
    plt.plot(x, f3(x), label='x1 - 3x2 <= 0')
    plt.plot(x, f4_b1(x), label='0.5x1 - 0.5x2 >= 0')
    plt.plot(x, f5(x), label='x2 <= 250')

    # Ιntersection points
    for intersection in intersections_b1:
        plt.plot(*intersection, 'ro')

    # Sauces
    plt.xlim(0, 500)
    plt.ylim(0, 500)
    plt.legend()
    
    # Erwthma b2
    # Feasible region
    plt.subplot(2, 2, 3)
    plt.title("Ερώτημα β me 60% χυμό πορτοκαλιού")
    plt.imshow((feasible_region_b2).astype(int),
            extent=(x1.min(), x1.max(), x2.min(), x2.max()), origin="lower", cmap="Greys", alpha=0.3)

    # Constraint plots
    plt.plot(x, f1(x), label='x1 + x2 <= 500')
    plt.plot(x, f2(x), label='x1 + x2 >= 400')
    plt.plot(x, f3(x), label='x1 - 3x2 <= 0')
    plt.plot(x, f4_b2(x), label='0.4x1 - 0.6x2 >= 0')
    plt.plot(x, f5(x), label='x2 <= 250')

    # Ιntersection points
    for intersection in intersections_b2:
        plt.plot(*intersection, 'ro')

    # Sauces
    plt.xlim(0, 500)
    plt.ylim(0, 500)
    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()