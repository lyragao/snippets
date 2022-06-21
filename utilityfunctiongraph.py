# i want to graph the 2-input utility function: 
# U(x,y) = x^{\eta}y^{\gamma} where x is leisure and y is income.
# given a set value for parameters eta and gamma.

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

# 3D GRAPH
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Define function.
feature_x = np.arange(0, 50, 2)
feature_y = np.arange(0, 50, 3)
  
# Create 2D grid of features.
[x, y] = np.meshgrid(feature_x, feature_y)
z = pow(y,0.5)*pow(x,0.3)

# Plot the surface.
ax.plot_surface(x, y, z)
ax.set_title('Utility Function Given η = 0.5, γ = 0.3')
ax.set_xlabel('Leisure')
ax.set_ylabel('Income')
ax.set_zlabel('Utility')

plt.show()

# CONTOUR PLOT
# make contour plot of utility function: 
feature_x = np.arange(0, 50, 2)
feature_y = np.arange(0, 50, 3)
  
# Create 2D grid of features.
[X, Y] = np.meshgrid(feature_x, feature_y)
  
fig, ax = plt.subplots(1, 1)
  
Z = pow(Y,0.5)*pow(X,0.3)
  
# Plot contour lines.
ax.contour(X, Y, Z)
  
ax.set_title('Contour Plot')
ax.set_xlabel('Leisure')
ax.set_ylabel('Income')
  
plt.show()
