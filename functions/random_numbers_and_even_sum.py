from random import randint

def sorteio(lista):
    for i in range(0, 5):
        lista.append(randint(0, 100))


def somar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    return soma


numeros = []
sorteio(numeros)
print(f'Os Números sorteados foram {numeros}')
print(f"A soma dos valores pares de {numeros}, é igual a {somar(numeros)}")

