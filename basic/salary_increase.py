import time
try:
    n = float(input('Salários acima de R$1250,00 recebem aumento de 10%. Abaixo ou iguais a R$1250,00 recebem aumento de 15%' 
'\nInforme seu salário: R$ '))
    print('por favor, aguarde...')
except ValueError:
    print('Erro. Informe um valor válido.') 
time.sleep(3)
if n <= 0:
    print('Erro. Informe um valor positivo.')
elif n > 1250:
    a = (n * 0.1)
    x = n + a
else:
    a = (n * 0.15)
    x = n + a

print('O salário de R${:.2f}, somado com o valor de R${:.2f} de aumento, resultam em R${:.2f}'.format(n, a, x))

