import numpy as np

linhas = int(input("Digite a quantidade de linhas da matriz: "))
colunas = int(input("Digite a quantidade de colunas da matriz: "))
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        elemento = float(input(f"Digite o elemento  da posição ({i},{j}): "))
        linha.append(elemento)
    matriz.append(linha)

matrix = np.array(matriz)

if np.array_equal(matrix, matrix.T):
    print("É simétrica!")
else:
    print("Não é simétrica!")


