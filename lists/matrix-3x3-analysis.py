#programa que cria uma matriz de 3x3 com números digitados pelo usuário, mostra a soma dos valores pares, a soma os valores da terceira coluna e maior valor da segunda linha.
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('Digite um valor para colocar na matriz: '))
print()
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l] [c] % 2 == 0:
            spar += matriz [l][c]
        
    print()
print(f'os valores pares somados são {spar}')
for l in range (0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna são {scol}')
for c in range (0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'o maior valor da segunda linha é {mai}')
