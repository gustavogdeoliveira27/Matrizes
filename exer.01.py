import numpy as np

manha = np.array([[2, 4, 6],
         [8, 10, 12],
         [14, 16, 18]])

tarde = np.array([[1, 3, 5],
         [7, 9, 11],
         [13, 15, 17]])

mtotal = manha + tarde

print("\nMatriz da quantidade de chuvas na parte da manhã:") 
print(manha)
print("\nMatriz da quantidade de chuvas na parte da tarde:")
print(tarde)
print("\nMatriz total:")
print(mtotal)


