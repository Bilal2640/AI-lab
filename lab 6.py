import math
# Basic math operations
print("Square root of 25:", math.sqrt(25))
print("Sine of 30 degrees:", math.sin(math.radians(30)))
print("Cosine of 45 degrees:", math.cos(math.radians(45)))

# Constants
print("Value of pi:", math.pi)
print("Value of e:", math.e)
import numpy as np

# Creating NumPy arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([[4, 5, 6], [7, 8, 9]])

# Basic array operations
print("Sum of arrays:", np.add(arr1, arr2))
print("Element-wise multiplication:", np.multiply(arr1, arr2))

# Linear algebra operations
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print("Matrix multiplication:", np.dot(matrix1, matrix2))
print("Determinant of matrix1:", np.linalg.det(matrix1))
import scipy.stats as stats
from scipy.optimize import minimize
from scipy.integrate import quad
import numpy as np
# Statistical operations
data = np.array([1, 2, 3, 4, 5])
print("Mean:", np.mean(data))
print("Standard deviation:", np.std(data))

# Optimization
def objective_function(x):
    return x**2 + 5*x + 6

result = minimize(objective_function, x0=0)
print("Optimal value:", result.fun)

# Integration
def integrand(x):
    return x**2

result, _ = quad(integrand, 0, 1)
print("Integral of x^2 from 0 to 1:", result)
