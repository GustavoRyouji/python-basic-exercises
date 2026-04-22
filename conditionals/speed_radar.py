km = float(input('Qual a velocidade do veículo?: '))
if km <= 80:
    print('Dentro do limite. Dirija com Segurança! ')
else:
    print('multado por excesso de velocidade.')
    print('Total à Pagar: {:.2f}.'.format((km-80)*7))

