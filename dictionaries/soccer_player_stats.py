jogador = {}
partidas = []
jogador['nome'] = input('Digite o nome do jogador: ')
tot = int(input(f'quantas partidas {jogador["nome"]} jogou?: '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos gols ele marcou no jogo {c+1}?: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(jogador)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
for k, v in jogador.items():
    print(f'o campo {k} tem o valor {v}')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
for k, v in enumerate(jogador['gols']):
    print(f'--> Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

