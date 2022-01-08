import numpy as np

# Create a vector as a row
vector_row = np.array([1, 2, 3])

# Create a vector as a column
vector_column = np.array([[1, 4],
                          [2, 5],
                          [3, 6]])


v = np.eye(10)
print(vector_row)
print(vector_column)
print(v)