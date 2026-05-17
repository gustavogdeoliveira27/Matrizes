import numpy as np

m = int(input("Digite o número de linhas: "))
n = int(input("Digite o número de colunas: "))
matriz = []

for i in range(m):
    linha = []
    for j in range(n):
        elemento = float(input(f"Digite o valor para a posião ({i},{j}): "))
        linha.append(elemento)
    matriz.append(linha)

matrix = np.array(matriz)

matriz_transporta = matrix.T
print("\nA matriz transporta é:")
print(matriz_transporta)
