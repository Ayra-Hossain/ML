import numpy as np
import matplotlib.pyplot as plt

# Define the range of the fuzzy sets
x = np.arange(101, 201)

# Generate random membership values between 0 and 1 for sets A and B
np.random.seed(0)  # Seed for reproducibility
mu_A = np.random.rand(100)
np.random.seed(1)
mu_B = np.random.rand(100)

# Calculate Fuzzy Union and Intersection
mu_union = np.maximum(mu_A, mu_B)
mu_intersection = np.minimum(mu_A, mu_B)

# Plot the membership functions
plt.figure(figsize=(20, 10))

# Plot for Fuzzy Set A
plt.plot(x, mu_A, label='Fuzzy Set A', color='blue', linestyle='-', marker='o')

# Plot for Fuzzy Set B
plt.plot(x, mu_B, label='Fuzzy Set B', color='green', linestyle='-', marker='s')

# Plot for Fuzzy Union
plt.plot(x, mu_union, label='Fuzzy Union (A ∪ B)', color='red', linestyle='--')

# Plot for Fuzzy Intersection
plt.plot(x, mu_intersection, label='Fuzzy Intersection (A ∩ B)', color='purple', linestyle='--')

# Customize the plot
plt.title('Fuzzy Sets and Their Union & Intersection')
plt.xlabel('Elements')
plt.ylabel('Membership Value')
plt.grid(True)

# Display the plot
plt.show()
