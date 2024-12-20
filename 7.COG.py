import numpy as np
import matplotlib.pyplot as plt
# Set a random seed for reproducibility
np.random.seed(42)
# Generate 20 random elements for fuzzy sets A and B
elements = np.random.randint(1, 101, 20) # Elements are integers between 1 and 100
# Generate 20 random membership values between 0 and 1
membership_values_A = np.random.random(20)
membership_values_B = np.random.random(20)

# Calculate the Center of Gravity (COG) for A and B
COG_A = np.sum(elements * membership_values_A) / np.sum(membership_values_A)
COG_B = np.sum(elements * membership_values_B) / np.sum(membership_values_B)

# Calculate the Weighted Average Value (WAV) for A and B
WAV_A = np.sum(membership_values_A * elements) / np.sum(membership_values_A)
WAV_B = np.sum(membership_values_B * elements) / np.sum(membership_values_B)

# Print the results
print("Elements:", elements)
print("\nMembership Values for Set A:", membership_values_A)
print("\nMembership Values for Set B:", membership_values_B)
print("\nCOG for Set A:", COG_A)
print("\nCOG for Set B:", COG_B)
print("\nWAV for Set A:", WAV_A)
print("\nWAV for Set B:", WAV_B)

# Function to plot a fuzzy set with COG and WAV
def plot_fuzzy_set(elements, membership_values, COG, WAV, title):
 plt.figure(figsize=(8, 5))
 plt.scatter(elements, membership_values, color='orange', label='Membership Values')
 plt.plot(elements, membership_values, color='orange')
 plt.axvline(COG, color='red', linestyle='--', label=f'COG: {COG:.2f}')
 plt.axvline(WAV, color='green', linestyle='--', label=f'WAV: {WAV:.2f}')
 plt.title(title)
 plt.xlabel('Elements')
 plt.ylabel('Membership Values')
 plt.legend()
 plt.show()
# Plot fuzzy set A
plot_fuzzy_set(elements, membership_values_A, COG_A, WAV_A, 'Fuzzy Set A')
# Plot fuzzy set B
plot_fuzzy_set(elements, membership_values_B, COG_B, WAV_B, 'Fuzzy Set B')