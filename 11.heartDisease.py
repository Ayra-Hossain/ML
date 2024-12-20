import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# Load Heart Disease dataset directly from the UCI repository
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"

# Load the dataset
# The dataset has no column names, so we provide them manually
column_names = [
    "age", "sex", "cp", "trestbps", "chol", "fbs", "restecg",
    "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num"
]
df = pd.read_csv(url, header=None, names=column_names)

# Replace '?' with NaN and drop rows with missing values
df.replace("?", pd.NA, inplace=True)
df.dropna(inplace=True)

# Convert numeric columns to proper types
df = df.astype(float)

# Drop target column ('num') for analysis
df_numeric = df.drop(columns=["num"])

# Calculate statistics
statistics = {
    "Mean": df_numeric.mean(),
    "Variance": df_numeric.var(),
    "Skewness": df_numeric.apply(skew),
    "Kurtosis": df_numeric.apply(kurtosis),
}

# Create a DataFrame for visualization
stats_df = pd.DataFrame(statistics)

# Plotting
plt.figure(figsize=(12, 10))

# Mean Plot
plt.subplot(2, 2, 1)
sns.barplot(x=stats_df.index, y=stats_df["Mean"], palette="Blues_d")
plt.title("Mean of Features", fontsize=16)
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
