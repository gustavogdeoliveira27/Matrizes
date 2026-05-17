import numpy as np

salarios = np.array([[5000, 10000, 3000],
                     [2000, 4000, 7000],
                     [3000, 5000, 10000]], dtype=float)

a = 1.10
aumento = a * salarios

print("\nMatriz dos salários:")
print(salarios)
print("\nMatriz do reajuste:")
print(aumento)