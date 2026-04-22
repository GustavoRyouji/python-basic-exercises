valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado...')
    else:
        print('Valor repetido, não adicionado...')
    r = input('Quer continuar? [S/N]')
    if r in 'Nn':
        break 
valores.sort(reverse = True)
print(f'Os valores digitados foram: {valores}')
