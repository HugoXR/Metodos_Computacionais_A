import numpy as np
import matplotlib.pyplot as plt
import time

t0 = time.time()

N = 10000
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)

Nc = sum(((x**2 + y**2) < 1))

# Nc = 0
# for i in range(N):
#     if np.sqrt(x[i]**2+y[i]**2) < 1:
#         Nc += 1

t = time.time() - t0
print(f"tempo para execucao do laco: {t}s")

print(4*Nc/N, 4*Nc/N - np.pi)

plt.plot(x, y, "o")
plt.savefig("Square.pdf")
plt.close('all')
