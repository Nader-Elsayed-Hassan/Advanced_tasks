# Problem 1: NumPy Operations
import numpy as np
arr = np.arange(1, 11)
mean_val = np.mean(arr)
median_val = np.median(arr)
std_dev_val = np.std(arr)
print(f"Array of nums: {arr}")
print(f"Mean value: {mean_val}")
print(f"Median value: {median_val}")
print(f"Standard Deviation value: {std_dev_val}")



# Problem 2: Pandas Filtering
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [20, 21, 22, 20, 21],
        'Score': [85, 78, 92, 65, 88]}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("\nStudents with Score > 80:")
filtered_df = df[df['Score'] > 80]
print(filtered_df)



# Problem 3: Visualization with Matplotlib
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.xlabel("X Axis (Input)")
plt.ylabel("Y Axis (X-squared)")
plt.title("Line Graph of y = x^2")
plt.grid(True)
plt.show() 




# Problem 4: Flask Application
from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello_advanced_python():
    return "Hello, Advanced Python!"