import numpy as np
import matplotlib.pyplot as plt
import math as m

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n - 1)

def S(x, n):
    sin_x = 0
    for i in range(n+1):
        sin_x = sin_x + (((-1)**i)*(x**((2*i)+1))/(factorial(2*i + 1)))
    return sin_x

x = np.linspace(0, 4*np.pi, 1001)

plt.plot(x, np.sin(x),"-ob", label="sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
for n in [1, 2, 3, 6, 12]:
    plt.plot(x, S(x, n), label="n = %d"%(n))
plt.legend()
plt.ylim(-1-0.5, 1+0.5)
plt.show()
plt.close('all')

