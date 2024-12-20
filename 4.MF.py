import numpy as np
import matplotlib.pyplot as plt

# Define Fuzzy Set x ranging between [1-10]
x = np.arange(1, 11)

# Triangular Membership Function
def triangular(a, b, m, x):
    if x <= a or x >= b:
        return 0
    elif a < x <= m:
        return (x - a) / (m - a)
    elif m < x < b:
        return (b - x) / (b - m)

# Trapezoidal Membership Function
def trapezoidal(a, b, c, d, x):
    if x <= a or x >= d:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)  # Increasing slope
    elif b < x <= c:
        return 1  # Constant at 1
    elif c < x < d:
        return (d - x) / (d - c)  # Decreasing slope

# Gaussian Membership Function
def gaussian(c, sigma, x):
    return np.exp(-((x - c) ** 2) / (2 * sigma ** 2))

# Parameters for the triangular, trapezoidal, and gaussian functions
a_triangular = 1
b_triangular = 10
m_triangular = 5

a_trapezoidal = 2
b_trapezoidal = 4
c_trapezoidal = 6
d_trapezoidal = 8

c_gaussian = 5  # Mean of Gaussian
sigma_gaussian = 1.5  # Standard deviation of Gaussian

# Calculate membership values
mu_x_triangular = np.array([triangular(a_triangular, b_triangular, m_triangular, val) for val in x])
mu_x_trapezoidal = np.array([trapezoidal(a_trapezoidal, b_trapezoidal, c_trapezoidal, d_trapezoidal, val) for val in x])
mu_x_gaussian = np.array([gaussian(c_gaussian, sigma_gaussian, val) for val in x])

# Plot all three functions
plt.plot(x, mu_x_triangular, marker='o', color='r', label='Triangular Membership')
plt.plot(x, mu_x_trapezoidal, marker='x', color='b', label='Trapezoidal Membership')
plt.plot(x, mu_x_gaussian, marker='s', color='g', label='Gaussian Membership')

# Adding titles and labels
plt.title('Triangular, Trapezoidal, and Gaussian Membership Functions')
plt.xlabel('Fuzzy set x')
plt.ylabel('Membership Degree')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Print the membership values
print(f"Triangular Membership Function: {mu_x_triangular}")
print(f"Trapezoidal Membership Function: {mu_x_trapezoidal}")
print(f"Gaussian Membership Function: {mu_x_gaussian}")
