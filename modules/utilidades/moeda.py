def aumentar(preco = 0, taxa = 0, formatado=False):
    res = preco + (preco*taxa/100)
    return res if formatado is False else moeda(res)

def diminuir(preco = 0, taxa = 0, formatado=False):
    res = preco - (preco*taxa/100)
    return res if formatado is False else moeda(res)


def dobro(preco = 0, formatado=False):
    res = preco*2
    return res if formatado is False else moeda(res)


def metade(preco = 0, formatado=False):
    res = preco/2
    return res if formatado is False else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.' , ',')


def resumo(preco=0, aumento=10, reducao=5):
    frase = "RESUMO DO VALOR"
    titulo = len(frase)
    linha = '-=' * titulo
    print(linha)
    print(frase.center(len(linha)))
    print(linha)
    print(f"{'Preço analisado':<15} {moeda(preco):^20}",
          f"{'Dobro do preço':<15} {dobro(preco, True):^20}",
          f"{'Metade do preço':<15} {metade(preco, True):^20}",
          f"{f'{aumento}% de aumento':<15} {aumentar(preco, aumento, True):^20}",
          f"{f'{reducao}% de redução':<15} {diminuir(preco, reducao, True):^20}",
          sep='\n')
    print(linha)

    