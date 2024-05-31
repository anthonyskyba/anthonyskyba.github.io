from matplotlib import pyplot as plt
import numpy as np
import random

dev_x = np.array([])
dev_y = np.array([])

data = open('/Users/anthony/Downloads/Salary_Data.csv', 'r')
for index, data in enumerate(data):
    if index == 0:
        continue

    data = data.split(',')
    age = float(data[1])
    salary = float(data[2])

    dev_x = np.append(dev_x, age)
    dev_y = np.append(dev_y, salary)

    plt.xlim(0, 50)
    plt.ylim(0, 130000)
    plt.scatter(age, salary, color='lightgreen', edgecolors='black')

    b, a = np.polyfit(dev_x, dev_y, deg=1)
    xseq = np.linspace(0, 70, num=100)
    line = plt.plot(xseq, a + b * xseq, color='red', lw=3)[0]
    plt.xlabel('Age')
    plt.ylabel('Salary')
    plt.title('Age vs Salary')
    plt.grid(True)

    plt.pause(0.3)
    if index < 30: line.remove()

plt.show()
