from random import randint
tentativas = 1
n = randint(0, 10)
t = int(input('Estou pensando em um número entre 0 e 10, tente acertar!: '))
while t != n:
    if t < n:
        print("Mais...")
    elif t > n:
        print("Menos...")
    t = int(input('Você errou! Tente novamente: '))
    tentativas +=1
    
print('Parabéns! Você acertou em {} tentativas! '.format(tentativas))
