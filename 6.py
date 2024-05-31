import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = np.arange(15)
y = np.arange(15)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

x, y = np.meshgrid(x, y)

z = np.sin(np.sqrt(x**2 + y**2))
z = np.sin(x) * np.sin(y)
z = np.sqrt(x) - np.sqrt(y)

ax.plot_surface(x, y, z, cmap='inferno')

plt.show()
