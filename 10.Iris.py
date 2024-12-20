import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# Load the Iris dataset
from sklearn.datasets import load_iris
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Calculate statistics
statistics = {
    "Mean": df.mean(),
    "Variance": df.var(),
    "Skewness": df.apply(skew),
    "Kurtosis": df.apply(kurtosis),
}

# Create a DataFrame for visualization
stats_df = pd.DataFrame(statistics)

# Plotting
plt.figure(figsize=(12, 10))

# Mean Plot
plt.subplot(2, 2, 1)
sns.barplot(x=stats_df.index, y=stats_df["Mean"], palette="Blues_d")
plt.title("Mean of Features", fontsize=10)
plt.ylabel("Mean", fontsize=12)
plt.xticks(rotation=45)

# Variance Plot
plt.subplot(2, 2, 2)
sns.barplot(x=stats_df.index, y=stats_df["Variance"], palette="Greens_d")
plt.title("Variance of Features", fontsize=16)
plt.ylabel("Variance", fontsize=12)
plt.xticks(rotation=45)

# Skewness Plot
plt.subplot(2, 2, 3)
sns.barplot(x=stats_df.index, y=stats_df["Skewness"], palette="Oranges_d")
plt.title("Skewness of Features", fontsize=16)
plt.ylabel("Skewness", fontsize=12)
plt.xticks(rotation=45)

# Kurtosis Plot
plt.subplot(2, 2, 4)
sns.barplot(x=stats_df.index, y=stats_df["Kurtosis"], palette="Reds_d")
plt.title("Kurtosis of Features", fontsize=16)
plt.ylabel("Kurtosis", fontsize=12)
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
