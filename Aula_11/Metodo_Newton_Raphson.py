# Calculo de zero pelo metodo de newton vs metodo da bissecao
import numpy as np
import matplotlib.pyplot as plt
import time


x = np.arange(0, 0.7, 0.01)

f = lambda x: 4*np.sin(x) - np.tan(2*x)
erro = 1E-5

# Metodo da bissecao 
x1 = 0.10
x2 = 0.70
f1 = f(x1)
f2 = f(x2)


nPassos_B = 0
print("Metodo da bissecao \n")
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
    nPassos_B += 1
    print(f"{nPassos_B} \t {xb:.10f} \t {abs(x2 - x1)/2}")

x0 = (x1+x2)/2

# Metodo de newton raphson
dfdx = lambda x: 4*np.cos(x) - 2/(np.cos(2*x))**2
x0_NR = 0.6
delta_x = 1e10

Npassos_NR = 0
print("Metodo de Newton Raphson \n")
while abs(delta_x) > erro:
    delta_x = - f(x0_NR)/dfdx(x0_NR)
    x0_NR += delta_x
    Npassos_NR += 1
    print(f"{Npassos_NR} \t {x0_NR} \t {abs(delta_x)}")

x0NR = x0_NR

plt.plot(x, 4*np.sin(x), label="$4*\\sin{x}$")
plt.plot(x, np.tan(2*x), label="$\\tan{2x}$")
plt.plot(x, f(x), label="f(x)")
plt.plot(x, x*0, ':', color='gray')
plt.plot(x0, f(x0), 'o', label="Metodo da bissecao")
plt.plot(x0, 4*np.sin(x0), 'o', label="Metodo da bissecao")
plt.plot(x0NR, f(x0NR), 'o', label="Metodo de Newton Raphson")
plt.ylim(-4, 4)
plt.legend()
plt.savefig("Bissecao_vs_Newton_Raphson.pdf")
plt.close()
