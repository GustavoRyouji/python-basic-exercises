maioridadehomem = 0
nomevelho = ''
somaidade = 0
mulher20 = 0
for i in range(1, 5):
    print('-----Pessoa {}-----'.format(i))
    n = input('Digite o nome da passoa: ').strip()
    idade = int(input('Digite a idade da pessoa: '))
    sexo = input('Digite o sexo da pessoa (M/F): ').strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = n
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = n
    if sexo in 'Ff' and idade < 20:
        mulher20 +=1

print('a media de idade é {}.'.format(somaidade / 4))
print('O homem mais velho tem {} anos e se chama {}. '.format(maioridadehomem, nomevelho))
print('{} mulheres têm mais de 20 anos. '.format(mulher20))
