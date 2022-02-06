import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('xy.dat', dtype=float)

x = data[:, 0]
y = data[:, 1]

y_max = y.max()
y_min = y.min()

y_mean = (y.sum()/len(y))

print(f" Max of y is {y_max:.2f}\n Min of y is {y_min:.2f}\n Mean of y is {y_mean:.2f}")

plt.plot(x, y, "-b")
plt.show()

