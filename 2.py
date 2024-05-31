from matplotlib import pyplot as plt
import numpy as np
import requests

plt.style.use('dark_background')

# UST31ENJNRXA6RYA
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDA&apikey=WE21XQHZJCRCJWF7'
r = requests.get(url)
data = r.json()
data = data['Time Series (Daily)']

dev_x = np.array([])
dev_y = np.array([])

for key in data:
    if int(key[6]) != 5: break
    closing_price = float(data[key]["4. close"])

    dev_x = np.append(dev_x, key)
    dev_y = np.append(dev_y, closing_price)

plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.title("Nvidia")
plt.grid(True)

axis = plt.gca()
axis.invert_xaxis()
axis.set_xticks(np.arange(0, 365, 4))

plt.plot(dev_x, dev_y, color="lightblue", marker="o", markersize=8, lw=3)
plt.show()
