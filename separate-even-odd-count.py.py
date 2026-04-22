num = []
par = []
impar = []
while True:
    n = int(input('Digite um valor para adicionar na lista: '))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    r = input('Deseja continuar? [S/N]: ')
    if r in 'Nn':
        break
print(f'Todos os valores digitados foram {num}')
print('-----' * 10)
print(f'Os valores pares digitados foram {par}')
print('-----' * 10)
print(f'Os valores impares digitados foram {impar}')
