import numpy as np

matriz = np.array([[1, 2],
                  [3, 4]])

print(matriz)

matriz[0], matriz[1] = matriz[1], matriz[0]

print("\nMatriz inversa: ")
print(matriz)