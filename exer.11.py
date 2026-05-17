
matriz = ([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

lista = [0, 0, 0]

for j in range(3):
    for i in range(3):
        lista[j] += matriz[i][j]

print(lista)

