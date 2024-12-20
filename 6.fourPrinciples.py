import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Generate random matrices R (5x6) and S (6x3) with values between 0 and 1
np.random.seed(42)  # Setting seed for reproducibility
R = np.random.rand(5, 6)  # R (5x6)
S = np.random.rand(6, 3)  # S (6x3)

# Function for max-min composition
def max_min_composition(R, S):
    result = np.zeros((R.shape[0], S.shape[1]))
    for i in range(R.shape[0]):
        for j in range(S.shape[1]):
            result[i, j] = np.max(np.minimum(R[i, :], S[:, j]))  # R-> ith row, all cols(:); S-> jth col, all rows(:)
    return result

# Function for min-max composition
def min_max_composition(R, S):
    result = np.zeros((R.shape[0], S.shape[1]))
    for i in range(R.shape[0]):
        for j in range(S.shape[1]):
            result[i, j] = np.min(np.maximum(R[i, :], S[:, j]))
    return result

# Function for max-product composition
def max_product_composition(R, S):
    result = np.zeros((R.shape[0], S.shape[1]))
    for i in range(R.shape[0]):
        for j in range(S.shape[1]):
            result[i, j] = np.max(R[i, :] * S[:, j])
    return result

# Function for max-avg composition
def max_avg_composition(R, S):
    result = np.zeros((R.shape[0], S.shape[1]))
    for i in range(R.shape[0]):
        for j in range(S.shape[1]):
            result[i, j] = np.max((R[i, :] + S[:, j]) / 2)
    return result

# Calculate the compositions
max_min_result = max_min_composition(R, S)
min_max_result = min_max_composition(R, S)
max_product_result = max_product_composition(R, S)
max_avg_result = max_avg_composition(R, S)

# Print the results in table format
def print_table(matrix, title):
    print(title)
    print(tabulate(matrix, headers=[f"Col {i+1}" for i in range(matrix.shape[1])], tablefmt="grid"))

print("R:")
print(tabulate(R, headers=[f"Col {i+1}" for i in range(R.shape[1])], tablefmt="grid"))
print("\nS:")
print(tabulate(S, headers=[f"Col {i+1}" for i in range(S.shape[1])], tablefmt="grid"))

print("\n")
print_table(max_min_result, "Max-Min Composition")

print("\n")
print_table(min_max_result, "Min-Max Composition")

print("\n")
print_table(max_product_result, "Max-Product Composition")

print("\n")
print_table(max_avg_result, "Max-Avg Composition")


# Plot the results separately
def plot_matrix(matrix, title): #matrix: The matrix (a 2D NumPy array) that you want to visualize,title: A string that will be used as the title of the plot.
 plt.figure(figsize=(6, 5))
 plt.imshow(matrix, cmap='viridis', aspect='auto')

 plt.title(title)
 plt.colorbar() #Adds a colorbar to the side of the plot
 plt.show()
plot_matrix(max_min_result, "Max-Min Composition")
plot_matrix(min_max_result, "Min-Max Composition")
plot_matrix(max_product_result, "Max-Product Composition")
plot_matrix(max_avg_result, "Max-Avg Composition")