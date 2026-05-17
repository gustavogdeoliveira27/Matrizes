import numpy as np

m = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

soma = np.trace(m)
print(f"A soma dos elementos é {soma}")