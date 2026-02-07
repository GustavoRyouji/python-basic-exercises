try: 
    km = float(input('qual a distância da viagem?:km '))
except ValueError:
    print('Erro. Digite Apenas Números.')

if km <= 0:
    print('Erro. Digite um número positivo.')
elif km <= 200:
    print('o custo de viagem é:R$ {:.2f}'.format(km * 0.50))
else:
    print('o custo de viagem é:R$ {:.2f}'.format(km * 0.45))


