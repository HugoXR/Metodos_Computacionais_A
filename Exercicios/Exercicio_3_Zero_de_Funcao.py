import numpy as np
import matplotlib.pyplot as plt


def beta(E):
    return np.sqrt(2*(16 - E)/7.63)


def alpha(E):
    return np.sqrt(2*E/7.63)


a = 4


def par(alpha, a):
    return alpha*np.tan(alpha*a)


def impar(alpha, a):
    if(any(alpha*a) == 0):
        raise ZeroDivisionError("Divisao por zero")
    return alpha/np.tan(alpha*a)


E = np.linspace(0, 16, 100)
alpha_E = alpha(E)
par_l = par(alpha_E, a)
par_r = beta(E)

try:
    impar_l = impar(alpha_E, a)
    impar_r = -beta(E)
    plt.plot(E, par_l, 'r', label="$\\alpha\\tan{(\\alpha a)}$")
    plt.plot(E, par_r, '--r', label="$\\beta$")
    plt.plot(E, impar_l, 'b', label="$\\alpha\\cot{(\\alpha a)}$")
    plt.plot(E, impar_r, '--b', label="$-\\beta$")
    plt.legend()
    plt.xlim(0, 16)
    plt.ylim(-3, 3)
    plt.show()
except ZeroDivisionError:
    print("Divisao por zero")

p_1 = 11.23
i_1 = 15.42

p_2 = 4.19
i_2 = 7.35

p_3 = 0.48
i_3 = 1.87

dalpha_dE = lambda e: 1/((7.63)*np.sqrt(2*e/7.63))
dbeta_dE = lambda e: -1/((7.63)*np.sqrt(2*(16-e)/7.63))
f_par = lambda e: alpha(e)*np.tan(alpha(e)*4) - beta(e)
f_impar = lambda e: alpha(e) + np.tan(alpha(e)*4)*beta(e)

df_par = lambda e: dalpha_dE(e)*np.tan(alpha(e)*4) + alpha(e)*dalpha_dE(e)*4/(np.cos(alpha(e*4))**2)
df_impar = lambda e: dalpha_dE(e)+np.tan(4*alpha(e))*dbeta_dE(e) + beta(e)*dalpha_dE(e)*4/(np.cos(alpha(e*4))**2)
erro = 1E-10
delta_x = 1E10

p = 15.2
while abs(delta_x) > erro:
    delta_x = -f_impar(p)/df_impar(p)
    p += delta_x

print(f"{p}")

