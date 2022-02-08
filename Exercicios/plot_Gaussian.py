from fill_lists import h
import numpy as np
import matplotlib.pyplot as plt

# Criando intervalo de -4 a 4
xlist = np.linspace(-4, 4, 41)
#Aplicando a funcao h em cada valor do intervalo
hlist = h(xlist)

#Plotando a curva gaussiana
plt.plot(xlist, hlist, "--o")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.title("Gaussian graph")
plt.savefig("Gaussian graph.pdf")
plt.show()
plt.close()

