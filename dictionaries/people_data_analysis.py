ficha = {}
galera = []
soma = media = 0
while True:
    ficha.clear()
    ficha['nome'] = input('Nome: ')
    while True:
        ficha['Sexo'] = input('Sexo: ').upper()[0]
        if ficha['Sexo'] in 'MF':
           break
        print("Erro. Favor digite apenas F ou M. ")
    ficha['idade'] = int(input('Idade: '))
    soma += ficha['idade']
    galera.append(ficha.copy())
    while True:
        res = input('Quer continuar?[S/N]: ').upper()[0]
        if res in 'SN':
            break
        print('Digite apenas S ou N.')

    if res == 'N':
        break

media = soma / len(galera)
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-')
print(f'A) ao todo temos {len(galera)} pessoas cadastradas')
print(f'B) A média de idade é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas são ',end='' )
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média de idade: ')
for p in galera:
    if p['idade'] >= media:
        print('      ', end='')
        for k, v in p.items():
            print(f' {k} = {v}', end='')
        print()
print('<<<ENCERRADO>>>')
    