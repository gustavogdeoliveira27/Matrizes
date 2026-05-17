import numpy as np

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

linha1 = np.mean(matriz[0])
linha2 = np.mean(matriz[1])
linha3 = np.mean(matriz[2])

print(f"A média da 1° linha é {linha1}")
print(f"A média da 2° linha é {linha2}")
print(f"A média da 3° linha é {linha3}")