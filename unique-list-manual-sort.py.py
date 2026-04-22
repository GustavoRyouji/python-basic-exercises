valores = []

for i in range(0, 5):
    n = int(input('escreva um valor para adicioná-lo á lista: '))
    if i == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos +=1
print (f'os valores digitados em ordem crescente foram: {valores}')
