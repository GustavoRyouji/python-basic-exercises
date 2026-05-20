from time import sleep

def contador(i, f, p):
    print()
    if p < 0:
        p*=-1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} em {p} em {p}: ')
    print('=-' * 25)
    sleep(1.5)
    
    if i < f:
        cont = i
        while cont<=f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont +=p
    else:
        cont = i
        while cont>= f:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont -=p


contador(1, 10, 1,)
contador(10, 0, 2)
print()
print('Personalize sua contagem! ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passos = int(input('Passos: '))
contador(inicio, fim, passos)
