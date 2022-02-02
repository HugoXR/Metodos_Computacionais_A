from fill_lists import h
import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-4, 4, 41)
hlist = h(xlist)


plt.plot(xlist, hlist, "--o")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.title("Gaussian graph")
plt.savefig("Gaussian graph.pdf")
plt.show()
plt.close()

