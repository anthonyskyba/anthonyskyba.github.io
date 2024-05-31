from matplotlib import pyplot as plt
import numpy as np

categories = np.array(['Price', 'MPG', 'Weight', 'Driving', 'Comfort', 'Price'])
labels = np.linspace(start=0, stop=2 * np.pi, num=len(categories))

v1 = np.array([3.93, 5.5, 6.36, 4.0, 5.0, 3.93])
v2 = np.array([8.399, 9.5, 6.05, 8.5, 9, 8.399])
v3 = np.array([4.7335, 6.5, 8.577, 9, 6.5, 4.7335])
v4 = np.array([2.555, 8.5, 3.935, 8.5, 7.5, 2.555])

plt.figure(figsize=(6, 6))
ax = plt.subplot(1, 1, 1, polar=True)

ax.plot(labels, v1, label='2023 Dodge Charger')
ax.fill(labels, v1, alpha=0.1)

ax.plot(labels, v2, label='2024 Tesla Model X')
ax.fill(labels, v2, alpha=0.1)

ax.plot(labels, v3, label='2023 Ford Bronco')
ax.fill(labels, v3, alpha=0.1)

ax.plot(labels, v4, label='2024 Honda Civic')
ax.fill(labels, v4, alpha=0.1)

plt.xticks(labels, categories)

plt.legend()
plt.show()