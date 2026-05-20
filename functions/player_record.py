def ficha(n='<desconhecido>', g=0):
    print(f'o jogador {n} fez {g} gols no campeonato')
    

nome = input('Digite o nome do jogador: ')
gols = str(input('Digite quantos gols foram feitos: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(g = gols)
else:
    ficha(nome, gols)