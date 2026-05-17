import numpy as np

mA = np.array([[1, 2],
               [3, 4]])

mB = np.array([[4, 3],
               [2, 1]])

mult = np.dot(mA, mB)
print("\nO resultado da multiplicação é:")
print(mult)