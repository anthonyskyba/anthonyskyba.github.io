from matplotlib import pyplot as plt
import numpy as np

height = np.array([])
weight = np.array([])

data = open('/Users/anthony/Downloads/data2.csv', 'r')
for index, line in enumerate(data):
    if index == 0: continue

    line = line.split(',')
    height = np.append(height, float(line[0]))
    weight = np.append(weight, float(line[1]))

x = weight
y = height

plt.figure(figsize=(8, 6))
hb = plt.hexbin(x, y, gridsize=50, cmap='inferno')

cb = plt.colorbar(hb)
cb.set_label('Counts')

plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Weight vs Height')

plt.show()