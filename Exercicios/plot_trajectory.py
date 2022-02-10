import numpy as np
import matplotlib.pyplot as plt


G = 9.8
def f(x, theta, v_0, y_0):
    return x*np.tan(theta) - (G*x**2/(2*(np.cos(theta)**2)*v_0**2)) + y_0


print("Type the initial position y_0, angle theta with the x axis, and the size of the initial velocity v_0\n")

y_0 = float(input("y_0: ")) # Posicao inicial em y
theta = float(input("theta: ")) # Theta da velocidade inicial
v_0 = float(input("v_0: ")) # Modulo da velocidade inicial

vh_0 = v_0*np.cos(theta) # Velocidade inicial horizontal
vv_0 = v_0*np.sin(theta) # Velocidade inicial vertical

t_f = ((vv_0) + np.sqrt(vv_0**2 + 2*G*y_0))/G # tempo final (quando a posicao de y é igual a 0 => gt^2/2 - vv_0t - y_0 = 0)

x_f = vh_0*t_f # Posicao final na direcao de x

x = np.linspace(0, x_f, 2000)
y = f(x, theta, v_0, y_0)

ax = plt.subplot()
plt.plot(x, y)
plt.title("Trajectory of the ball")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Distance (m)")
plt.xlim([0, x[-1]])
plt.ylim([y_0, y.max()+10])
plt.text(0.75, 0.9, "$y(x) = x*\\tan{\\theta} - \\frac{%.2f*x^{2}}{2*\\cos^2{\\theta}*v_{0}^2} + y_0$"%(G), horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes)

plt.text(0.63, 0.85, "$\\theta = %.3f$ rad"%(theta), horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes)

plt.text(0.65, 0.8, "$v_{0} = %.3f$ m/s"%(v_0), horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes)

plt.text(0.63, 0.75, "$y_{0} = %.3f$ m"%(y_0), horizontalalignment='center',
         verticalalignment='center', transform=ax.transAxes)
plt.savefig("Trajectory.pdf")
plt.show()
