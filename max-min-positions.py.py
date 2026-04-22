# programa que pede 5 números e mostra o maior e menor número digitado e suas respectivas posições.
lista = []
mai = 0
men = 0
for i in range (0, 5):
    lista.append(int(input(f'escreva um valor para a posição {i+1}: ')))
    if i == 0:
        mai = men = lista[i]
    else:
        if lista[i] > mai:
            mai = lista[i]
        if lista[i] < men:
            men = lista[i]
print(f'Você digitou os valores {lista}.')
print(f'O maior numero digitado é {mai}, nas posições ', end='')
for c, v in enumerate(lista):
    if v == mai:
        print(f'{c+1}... ', end='')
print()
print(f'O menor numero digitado é {men}, nas posições ', end='')
for c, v in enumerate(lista):
    if v == men:
        print(f'{c+1}... ', end='')