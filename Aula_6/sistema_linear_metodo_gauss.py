import numpy as np

# A = np.array([[2., 1., 1.], [2., 1., 2.], [-3., 2., 1.]])
# C = np.array([[1.], [2.], [1.]])

# C = np.loadtxt("matriz.dat", max_rows=1)
# C = C.reshape([C.size, 1])
# A = np.loadtxt("matriz.dat", skiprows=1)
N = 20
A = np.random.uniform(size=[N, N])
C = np.random.uniform(size=[N, 1])


def resolveSL(A, C):
    """
    Resolve um sistema linear AB = C
    Parametros
    ------------
    A: Matriz de coeficientes NxN
    C: Matriz de constantes Nx1
    Retorna
    ------------
    A matriz B, solucao do sistema linear
    """

    B = np.zeros_like(C)
    M = np.concatenate([A, C], axis=1)
    if(A.shape[1] != C.shape[0]): 
        raise TypeError("Tamanhos das matrizes A e C distintos")
    N = A.shape[0]
    for i in range(N):
        j = np.argmax(abs(A[:, i])) # retorna o indice do maior elemento
        if(j > i):
            # Trocando as linhas
            linha_i = M[i, :].copy()
            M[i, :] = M[j, :]
            M[j, :] = linha_i
        for k in range(N):
            if(i != k and M[i, i] != 0):
                # Subtraindo linhas
                M[k, :] -= ((M[i, :]/M[i, i])*(M[k, i]))
        try:
            B = M[:, -1] / M.diagonal()
        except ZeroDivisionError:
            print("Sistema impossível")
    return B.reshape([N, 1])


B = resolveSL(A, C)
erro = np.abs(np.dot(A, B) - C) 
if(all(erro < 1e-10)):
    print("Solucao é: \nB=\n", B)
else:
    print("Erro no calculo da matriz B")

print(f"Erro médio: {np.mean(erro)}")
