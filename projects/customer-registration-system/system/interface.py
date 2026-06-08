from .dados import *
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for items in lista:
        print(f'{c} - {items}')
        c+=1
    print(linha())
    opc = leiaInt('Sua resposta: ')
    while opc<1 or opc > len(lista):
        print('Erro, digite um valor válido')
        opc = leiaInt('Sua resposta: ')
    return opc


def retornar(lista, texto):
    cabeçalho(texto)
    c = 1
    for items in lista:
        print(f'{c} - {items}')
        c+=1
    print(linha())
    opc = leiaInt('Sua resposta: ')
    while opc<1 or opc > len(lista):
        print('Erro, digite um valor válido')
        opc = leiaInt('Sua resposta: ')
    return opc


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
