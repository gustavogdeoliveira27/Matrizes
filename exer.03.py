import numpy as np

ingredientes = np.array([[5, 3, 8],
                        [4, 6, 3]])

pedidos = np.array([[2, 4],
                    [3, 1],
                    [4, 2]])

mult = np.dot(ingredientes, pedidos)

print("\nMatriz dos ingredientes:")
print(ingredientes)
print("\nMatriz dos pedidos:")
print(pedidos)
print("\nMatriz da multiplicação:")
print(mult)