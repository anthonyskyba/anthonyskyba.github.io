from matplotlib import pyplot as plt
import numpy as np
import random

dev_x = np.array([])
dev_y = np.array([])

for i in range(1000):
    dev_x = np.append(dev_x, random.randint(0, 100))
    dev_y = np.append(dev_y, random.randint(0, 100))

    plt.xlim(0, 100)
    plt.ylim(0, 100)
    plt.scatter(dev_x, dev_y, color='lightgreen', edgecolors='black')
    plt.grid(True)

    b, a = np.polyfit(dev_x, dev_y, deg=1)
    xseq = np.linspace(0, 100, num=100)
    line = plt.plot(xseq, a + b * xseq, color='red', lw=3)[0]
    
    plt.pause(0.009)
    line.set_color('blue')
    line.set_linewidth(0.3)
    line.set_alpha(0.8)
        

plt.show()