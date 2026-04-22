import time
try:
    r1 = float(input('Digite o valor da primeira reta: '))
    r2 = float(input('Digite o valor da segunda reta: '))
    r3 = float(input('Digite o valor da terceira reta: '))
except ValueError:
    print('Erro. Informe apenas números')


if r1 < r2+r3 and r2 < r1+r3 and r3< r1+r2: 
    print('Calculando...')
    time.sleep(4)
    print('Aplicando Fórmula...')
    time.sleep(5)
    print('Essas retas podem formar um triângulo! ')
else:
    print('Essas retas não pode virar um triângulo')
