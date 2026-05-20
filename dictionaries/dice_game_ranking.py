#programa que roda um dado 4 vezes e marca a posição dos jogadores
from random import randint
from time import sleep
from operator import itemgetter
jogos = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}
ranking = {}
print('-----------==============--------------')
print( 'Jogos sorteados: ')
for k, v in jogos.items():
    print(f' - {k}: {v}')
    sleep(1)
print('---------==========-----------')
print('VENCEDOR: ')
ranking = sorted(jogos.items(), key=itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f' - {i+1}: {v[0]} tirou: {v[1]}')
    sleep(1)
