#programa que mostra boletim de alunos, a média e as duas notas de cada aluno individualmente
ficha = []
while True:
    nome = input('Digite o nome do aluno: ')
    n1 = float(input('Digite a primeira nota do aluno: '))
    n2 = float(input('Digite a segunda nota do aluno: '))
    media = (n1 + n2)/2
    ficha.append([nome, [n1, n2], media])
    r = input('Deseja continuar? [S/N]: ')
    if r in 'Nn':
        break
print('----' * 30)
print(f'{"No. ":<5}{"NOME ":<10}{"MÉDIA ":<8}')
print('---' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<5} {a[0]:<10} {a[2]:<8}')
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 para finalizar): '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc<= len(ficha)-1:
        print(f'ALUNO: {ficha[opc] [0]} NOTAS: {ficha[opc] [1]}')
