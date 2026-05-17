import numpy as np

quaisquer = np.array([[23, 45, 12, 22, 12],
                      [67, 43, 23, 56, 32],
                      [78, 65, 34, 23, 78],
                      [12, 23, 34, 45, 56],
                      [98, 87, 76, 65, 54]])

print("\nMatriz inicial:")
print(quaisquer)

quaisquer[1][2] = 1
quaisquer[3][4] = 2

print("\nMatriz atualizada")
print(quaisquer)
