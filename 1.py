from matplotlib import pyplot as plt
import numpy as np

dev_x = np.array([])
dev_y = np.array([])

data = open('/Users/anthony/Downloads/NVDA.csv', 'r')
for index, line in enumerate(data):
    if index == 0: continue

    line = line.split(',')
    date = line[0]
    closing_price = float(line[4])

    dev_x = np.append(dev_x, date)
    dev_y = np.append(dev_y, closing_price)

plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Nvidia")
plt.fill_between(dev_x, dev_y, 300, color='blue', alpha=0.1)

axis = plt.gca()
axis.set_xticks(np.arange(0, 365, 60))

plt.plot(dev_x, dev_y, "k")
plt.show()