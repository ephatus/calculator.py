import numpy as np

# Create array
arr = np.arange(1, 11)

# Calculate mean
mean_val = np.mean(arr)

print("Array:", arr)
print("Mean:", mean_val)


import pandas as pd

# Create small dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 28],
    "Score": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("\nDataset:\n", df)
print("\nSummary Statistics:\n", df.describe())


import requests

# Fetch JSON placeholder API (fake online API)
url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("\nFetched API Data:")
    print("Title:", data["title"])
else:
    print("Failed to fetch data, status code:", response.status_code)


import matplotlib.pyplot as plt

# List of numbers
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker="o")
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
