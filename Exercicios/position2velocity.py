import numpy as np
import matplotlib.pyplot as plt

s = float(np.loadtxt("pos.dat", usecols=0, max_rows=1))

xy_data = np.loadtxt("pos.dat", skiprows=1)

x = xy_data[:, 0]
y = xy_data[:, 1]

time = np.linspace(0, 15, len(x)-1)
time_k = time*s
v_x = (x[1:] - x[:-1]) / s
v_y = (y[1:] - y[:-1]) / s

plt.plot(x, y, "-or")
plt.show()
plt.close("all")

plt.plot(time_k, v_y, "-ob")
plt.xlabel("Time (s)")
plt.ylabel("Velocity in y (m/s)")

plt.twinx()
plt.plot(time_k, v_x, "-or")
plt.ylabel("Veloity in x (m/s)")
plt.show()
plt.close('all')
