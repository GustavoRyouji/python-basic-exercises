def leiaDinheiro(valor):
    ok = False
    while not ok:
        n = str(input(valor)).replace(',', '.').strip()
        if n.isalpha() or n == '':
            print(f'ERRO,{n} NÃO É UM PREÇO VÁLIDO.')
        else:
            ok = True
            return float(n)


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




