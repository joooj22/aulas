matriz = [
    [1,2],
    [3,4],
]
k = 2
for linha in range(len(matriz)):
    for coluna in range(len(matriz[linha])):
        matriz[linha][coluna] *= k

for i in matriz:
    print(i)
