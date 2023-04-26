# Universidade Federal do Tocantins
# Aluno: Bruno Ferreira da Silva
# Multiplicação entre duas matrizes quadradas utilizando multi-threading

from threading import Thread

MAX = 4
MAX_THREAD = 4

matrizC = [[0 for i in range(MAX)] for j in range(MAX)]
passo_i = 0

# Em Python, uma matriz pode ser representada como uma lista de listas,
# onde um elemento da lista contém uma linha da matriz, 
# que por sua vez corresponde a uma lista com os elementos da coluna da matriz.

# Abaixo temos uma função para imprimir matrizes no console de forma legível:
def printMatrix(mat):
    for row in mat:
        print(row)

# Utilizemos matrizes quadradas A e B para a obtenção de C
# Abaixo temos a função para multiplicar uma linha da matriz A
# com todas as colunas de B obtendo, a cada chamada de multi(), UMA LINHA da matriz resultante C.

def multi():
    global passo_i, matrizC
    i = passo_i
    passo_i = passo_i + 1
    for j in range(MAX):
        for k in range(MAX):
            matrizC[i][j] = matrizC[i][j] + matrizA[i][k] * matrizB[k][j]

if __name__ == "__main__":
    # matriz A:
    matrizA = [[8, 2, 2, 5],
            [2, 3, 0, 3],
            [1, 0, 1, 5],
            [9, 7, 7, 8]]

    # matriz B:
    matrizB = [[3, 6, 5, 9],
            [7, 6, 2, 3],
            [8, 6, 4, 9],
            [8, 5, 3, 0]]

    # Criando uma lista de tamanho MAX_THREAD
    thread = list(range(MAX_THREAD))

    # Sempre podemos executar uma função (multi) em uma nova thread através do argumento "target" da classe threading.Thread
    # Como MAX_THREAD =  4, o SO criará 4 threads distintas para calcular cada linha de C

    for i in range(MAX_THREAD):
        thread[i] = Thread(target=multi)
        thread[i].start()
        # Mostramos as 4 threads criadas:
        print(thread[i])

    # Esperamos todas as threads terminarem:
    for i in range(MAX_THREAD):
        thread[i].join()

    # Mostramos C = A x B como resultado:
    printMatrix(matrizC)

'''
No exemplo, não conseguimos controlar quando uma thread executará com precisão ou qual núcleo da CPU o executará, uma vez que ambas são responsabilidades de baixo nível tratadas pelo sistema operacional subjacente.
'''