import numpy as np
import matplotlib.pyplot as plt
import time


x = np.arange(0, 0.7, 0.01)

f = lambda x: 4*np.sin(x) - np.tan(2*x)

erro = 1E-10
x1 = 0.10
x2 = 0.70
f1 = f(x1)
f2 = f(x2)

nPassos = 0
while (x2 - x1)/2 > erro:
    xb = (x1+x2)/2
    fb = f(xb)
    if(fb*f2 > 0):
        x2 = xb
        f2 = fb
    elif(fb*f1 > 0):
        x1 = xb
        f1 = fb
    else:
        x1 = xb
        x2 = xb
    nPassos += 1

x0 = (x1+x2)/2

plt.plot(x, 4*np.sin(x), label="$4*\\sin{x}$")
plt.plot(x, np.tan(2*x), label="$\\tan{2x}$")
plt.plot(x, f(x), label="f(x)")
plt.plot(x, x*0, ':', color='gray')
plt.plot(x0, f(x0), 'o')
plt.plot(x0, 4*np.sin(x0), 'o')
plt.ylim(-4, 4)
plt.legend()
plt.savefig("Zero_de_funcao.pdf")
plt.close()
