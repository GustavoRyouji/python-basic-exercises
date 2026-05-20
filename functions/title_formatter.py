def titulo(txt):
    tam = len(txt) + 4
    print('~'* tam)
    print(f'{txt.center(tam)}')
    print('~'* tam)

while True:
    palavra = input('Qual é o título?: ')
    titulo(palavra)
    resp = input('Deseja continuar?[S/N]: ')
    if resp in 'Nn':
        break
titulo('Finalizando...')
