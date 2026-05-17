import numpy as np

quaisquer = np.array([[23, 45, 12],
                      [67, 43, 23],
                      [78, 65, 34]])

print("\nMatriz inicial:")
print(quaisquer)

quaisquer[:] = 0

print("\nMatriz final:")
print(quaisquer)