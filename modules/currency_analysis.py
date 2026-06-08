#programa que analisa valor monetário
from utilidades import moeda
p = input('Digite o preço do produto: R$').replace(',' , '.')
p = float(p)

print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'Com um aumento de 25% de taxas, o valor de {moeda.moeda(p)} fica {moeda.aumentar(p, 25, True)} ')
print(f'Com uma diminuição de 25% de taxas, o valor de {moeda.moeda(p)} fica {moeda.diminuir(p, 25, True)}')
