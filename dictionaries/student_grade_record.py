#programa que guarda nome, média e situação de um aluno em um dicionário.
aluno = {}
aluno['nome'] = input('Digite o nome do aluno: ')
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situacao'] = "Aprovado"
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = "Recuperação"
else:
    aluno['situacao'] = "Reprovado"

print('------=====------')
for k, v in aluno.items():
    print(f' - {k}: {v}')

