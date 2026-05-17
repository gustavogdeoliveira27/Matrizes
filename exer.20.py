import numpy as np

matriz = np.array([[23, 45, 12, 22],
                    [67, 43, 23, 56],
                    [78, 65, 34, 23],
                    [12, 23, 34, 45],])

n = int(input("Digite um número: "))

if n in matriz:
    print("O número está na matriz")
else:
    print("O número não está na matriz")
