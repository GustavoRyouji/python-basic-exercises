jogador = {}
time = []
partidas = []

while True:
    jogador.clear()
    partidas.clear()
    jogador['nome'] = input('Digite o nome do jogador: ')
    tot = int(input(f'quantas partidas {jogador["nome"]} jogou?: '))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols ele marcou no jogo {c+1}?: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        res = input('Deseja continuar?[S/N]: ').upper()[0]
        if res in 'SN':
            break
        print('Erro. Digite apenas S ou N.')    
    if res in 'Nn':
        break
print('Cod. ', end='')
for i in jogador.keys():
    print(f'{i:>15}', end='')
print()
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='*2)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):>15}', end='')
    print()
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-='*2)
while True:
    opc = int(input('buscar status de qual jogador? [999 para cancelar]: '))
    if opc == 999:
        break
    if opc >= len(time):
        print(f'Erro. Não existe jogador com o código {opc}')
    else:
        print(f'Levantamento do jogador {time[opc]["nome"]}:')
        for k, v in enumerate(time[opc]['gols']):
            print(f'- No jogo {k+1} fez {v} gols')
print('<<<<<VOLTE SEMPRE>>>>>')

