import numpy as np

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("\nMatriz inicial:")
print(matriz)

n = float(input("Digite um número real: "))

resultado = n * matriz
print("\nMatriz final:")
print(resultado)