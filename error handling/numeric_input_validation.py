def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except ValueError as erro:
            print(f'Erro. Digite apenas números inteiros. erro: {erro.__class__.__name__} ')
        else:
            return n
            
    
def leiafloat(msg):
    while True:
        try:
            n = input(msg).replace(',', '.')
            n = float(n)
        except ValueError as erro:
            print(f'ERRO. Digite apenas números reais. Erro: {erro.__class__.__name__}')
        else:
            return n


num = leiaInt('Digite um número: ')
n = leiafloat('Digite outro numero: ')
print(f'Você acabou de digitar o número inteiro {num}.')
print(f'Você acabou de digitar o número real {n}')