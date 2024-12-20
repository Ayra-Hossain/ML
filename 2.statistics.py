import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate a random 100x100 matrix
matrix = np.random.randint(100, size=(100, 100))

# Calculate statistics for each column
mean = np.mean(matrix, axis=0)
variance = np.var(matrix, axis=0)
kurtosis = stats.kurtosis(matrix, axis=0)
skewness = stats.skew(matrix, axis=0)

# Create a figure with subplots
fig, axs = plt.subplots(2, 2, figsize=(20, 10))

# Plot Mean
axs[0, 0].plot(mean, marker='o', color='blue')
axs[0, 0].set_title('Mean of Each Column')
axs[0, 0].set_xlabel('Column Index')
axs[0, 0].set_ylabel('Mean')
axs[0, 0].grid(True)

# Plot Variance
axs[0, 1].plot(variance, marker='o', color='green')
axs[0, 1].set_title('Variance of Each Column')
axs[0, 1].set_xlabel('Column Index')
axs[0, 1].set_ylabel('Variance')
axs[0, 1].grid(True)

# Plot Skewness
axs[1, 0].plot(skewness, marker='o', color='red')
axs[1, 0].set_title('Skewness of Each Column')
axs[1, 0].set_xlabel('Column Index')
axs[1, 0].set_ylabel('Skewness')
axs[1, 0].grid(True)

# Plot Kurtosis
axs[1, 1].plot(kurtosis, marker='o', color='purple')
axs[1, 1].set_title('Kurtosis of Each Column')
axs[1, 1].set_xlabel('Column Index')
axs[1, 1].set_ylabel('Kurtosis')
axs[1, 1].grid(True)

# Adjust layout and show the plot
plt.tight_layout()
plt.show()