sexo = str(input('Digite o seu sexo [F/M]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Valor inválido. Digite novamente[F/M]: ')).strip().upper()[0]
print('Sexo registrado com sucesso! ')
