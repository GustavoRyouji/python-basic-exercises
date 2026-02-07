from random import randint 

n = randint(0, 5)
print('Em que número eu pensei? ')
c = int(input('Número: '))
if c == n:
    print('Você Acertou! ')
else:
    print('Você Errou. ')
    print('Pensei no número {}. '.format(n))
    
