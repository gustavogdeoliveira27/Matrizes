
def rotacionar_90(matriz):
    n = len(matriz)

    nova = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            nova[j][n - 1 - i] = matriz[i][j]
    return nova
    
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
rotacionada = rotacionar_90(matriz)
for linha in rotacionada:
    print(rotacionada)
