lista = []
while True:
    n = int(input("digite um valor para adicionar na lista: "))
    lista.append(n)
    r = input("deseja continuar? [S/N]: ")
    if r in "Nn":
        break
print(f"Foram digitados {len(lista)} números")
lista.sort(reverse = True)
print(f"a lista em forma decrescente é: {lista}")
if 5 in lista:
    print("o 5 faz parte da lista!")
else:
    print("o 5 não faz parte da lista.")
