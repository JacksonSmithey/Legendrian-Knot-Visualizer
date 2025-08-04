# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:00:45 2024

@author: Jackson
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Generate random data
num_points = 100
x = np.random.rand(num_points)
y = np.random.rand(num_points)
z = np.random.rand(num_points)

# Create a figure for the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Use a for loop to plot each point
for i in range(num_points):
    ax.scatter(x[i], y[i], z[i], c='b', marker='o')  # You can change color and marker as needed

# Set labels
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# Show the plot
plt.show()
