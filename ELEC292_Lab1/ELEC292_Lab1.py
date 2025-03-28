import numpy as np

# Question 6
my_3d_array = np.arange(27).reshape(3,3,3)

print("\n")
print(my_3d_array[[0, 1, 2], [1, 2, 0], [1, 2, 0]])
print(my_3d_array[[1, 1], [0, 2], [0, 2]])

