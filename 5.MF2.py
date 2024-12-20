import numpy as np
import matplotlib.pyplot as plt

# Triangular Membership Function
def triangular(a, b, m, x):
    if x <= a or x >= b:
        return 0
    elif a < x <= m:
        return (x - a) / (m - a)
    elif m < x < b:
        return (b - x) / (b - m)

# Fuzzy set x ranging between [1-10]
x = np.arange(1, 11)

# Parameters for triangular membership functions of sets A and B
a_A, b_A, m_A = 1, 10, 5
a_B, b_B, m_B = 1, 10, 7

# Calculate membership values for sets A and B
mu_A = np.array([triangular(a_A, b_A, m_A, val) for val in x])
mu_B = np.array([triangular(a_B, b_B, m_B, val) for val in x])

# Union of fuzzy sets A and B (maximum of A and B for each element)
union_AB = np.maximum(mu_A, mu_B)

# Plot the membership functions
plt.plot(x, mu_A, marker='o', color='r', label='Set A (Triangular MF)')
plt.plot(x, mu_B, marker='x', color='b', label='Set B (Triangular MF)')
plt.plot(x, union_AB, marker='s', color='g', label='Union A ∪ B')

# Adding labels and title
plt.xlabel('Elements')
plt.ylabel('Membership Degree')
plt.title('Union of Fuzzy Sets A and B with Triangular MF')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()

# Print the membership values
print(f"Set A Membership (Triangular): {mu_A}")
print(f"Set B Membership (Triangular): {mu_B}")
print(f"Union (A ∪ B) Membership: {union_AB}")
