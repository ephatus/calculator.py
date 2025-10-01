# ==============================
# Data Analysis & Visualization
# Using Pandas, Matplotlib & Seaborn
# ==============================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Apply seaborn style
sns.set(style="whitegrid")

# ==============================
# Task 1: Load and Explore Dataset
# ==============================

try:
    # Load Iris dataset directly from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # DataFrame with features + target
    df["species"] = df["target"].map(dict(enumerate(iris.target_names)))  # map labels

    print("✅ Dataset loaded successfully.\n")
    print("First few rows:\n", df.head())

    # Check structure
    print("\nData Info:")
    print(df.info())

    # Missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())

except FileNotFoundError:
    print("⚠️ Error: Dataset file not found.")
except Exception as e:
    print(f"⚠️ An error occurred: {e}")

# ==============================
# Task 2: Basic Data Analysis
# ==============================

print("\n=== Statistical Summary ===")
print(df.describe())

# Group by species and compute mean petal length
grouped = df.groupby("species")["petal length (cm)"].mean()
print("\nAverage petal length per species:")
print(grouped)

# Observations
print("\nObservations:")
print("• Setosa has the smallest petal length on average.")
print("• Virginica shows the largest values across multiple features.")
print("• Versicolor is typically in the middle range.")

# ==============================
# Task 3: Data Visualization
# ==============================

plt.figure(figsize=(12, 10))

# 1. Line Chart – sepal length trend (index as x-axis)
plt.subplot(2, 2, 1)
plt.plot(df.index, df["sepal length (cm)"], marker="o", linestyle="-", color="b", label="Sepal Length")
plt.title("Sepal Length Trend")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()

# 2. Bar Chart – average petal length per species
plt.subplot(2, 2, 2)
grouped.plot(kind="bar", color=["skyblue", "lightgreen", "salmon"])
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")

# 3. Histogram – distribution of sepal width
plt.subplot(2, 2, 3)
plt.hist(df["sepal width (cm)"], bins=10, color="purple", edgecolor="black", alpha=0.7)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")

# 4. Scatter Plot – sepal length vs petal length
plt.subplot(2, 2, 4)
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="deep")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")

plt.tight_layout()
plt.show()
