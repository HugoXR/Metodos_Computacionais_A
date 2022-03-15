import numpy as np
import matplotlib.pyplot as plt

# Funcao beta
def beta(E):
    return np.sqrt(2*(16 - E)/7.63)

# Funcao alpha
def alpha(E):
    return np.sqrt(2*E/7.63)

a = 4

# Solucao par, lado esquerdo
def par(alpha, a):
    return alpha*np.tan(alpha*a)

# Solucao impar, lado esquerdo
def impar(alpha, a):
    if(any(alpha*a) == 0):
        raise ZeroDivisionError("Divisao por zero")
    return alpha/np.tan(alpha*a)

# Valores de energia
E = np.linspace(0, 16, 100)

alpha_E = alpha(E)
par_l = par(alpha_E, a)
par_r = beta(E)

#Plotando grafico dos valores de energia para as solucoes impar e par
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


# Pontos de zero da funcao
p_1 = 11.23
i_1 = 15.45

p_2 = 4.19
i_2 = 7.35

p_3 = 0.48
i_3 = 1.87


# Derivada de alpha em relação a E
dalpha_dE = lambda e: 1/((7.63)*np.sqrt(2*e/7.63))

# Derivada de beta em relação a E
dbeta_dE = lambda e: -1/((7.63)*np.sqrt(2*(16-e)/7.63))

# Funcao par para a = 4
f_par = lambda e: alpha(e)*np.tan(alpha(e)*4) - beta(e)

# Funcao impar para a = 4
f_impar = lambda e: alpha(e) + np.tan(alpha(e)*4)*beta(e)

# Derivada da funcao par em relacao a E
df_par = lambda e: dalpha_dE(e)*np.tan(alpha(e)*4) + alpha(e)*dalpha_dE(e)*4/(np.cos(alpha(e*4))**2)

# Derivada da funcao impar em relacao a E
df_impar = lambda e: dalpha_dE(e)+np.tan(4*alpha(e))*dbeta_dE(e) + beta(e)*dalpha_dE(e)*4/(np.cos(alpha(e*4))**2)


erro = 1E-10
delta_x = 1E10

# Ponto inicial impar
p_i = i_2


# Encontrando zero de funcao mais proximo para funcao impar
while abs(delta_x) > erro:
    delta_x = -f_impar(p_i)/df_impar(p_i)
    p_i += delta_x
    print(f"{p_i} \t {f_impar(p_i):.10f} \t {abs(delta_x):.10f}")
print(f"{p_i} \n\n")

erro = 1E-10
delta_x = 1E10

# Ponto inicial par
p_p = p_1

# Encontrando zero de funcao mais proximo para funcao par
while abs(delta_x) > erro:
    delta_x = -f_par(p_p)/df_par(p_p)
    p_p += delta_x
    print(f"{p_p} \t {f_par(p_p):.10f} \t {abs(delta_x):.10f}")
print(f"{p_p}")


