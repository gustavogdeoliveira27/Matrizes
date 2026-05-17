import numpy as np

estoque_inicial = np.array([[5, 7, 9,],
                           [8, 10, 6],
                           [6, 5, 10]])

vendidos = np.array([[2, 4, 1],
                     [3, 5, 2],
                     [4, 4, 8]])

total = estoque_inicial - vendidos

print("\nMatriz do estoque inicial:")
print(estoque_inicial)
print("\nMatriz de vendidos:")
print(vendidos)
print("\nTotal:")
print(total)