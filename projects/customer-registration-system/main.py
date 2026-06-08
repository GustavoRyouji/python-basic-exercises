from sistema.interface import *
from sistema.clientes import *
import time

arq = 'exer81/sistema/cadastro.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

cabeçalho('SISTEMA DE CADASTRO')
while True:
    escolha = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    
    if escolha == 1:
        lerArquivo(arq)
        print(linha())
        time.sleep(2)
        res = retornar(['Voltar ao início', 'Finalizar Sistema'],'Deseja voltar para o início?')
        if res == 1:
            continue
        
        if res == 2:
            cabeçalho('FINALIZANDO... VOLTE SEMPRE!')
            break
    elif escolha == 2:
        while True:  
            cabeçalho('NOVO CADASTRO')
            nome = str(input('Nome da pessoa: '))
            idade = leiaInt('Idade da pessoa: ')
            cadastroNovo(arq, nome, idade)
            time.sleep(2)
            res = retornar(['Criar novo cadastro', 'Voltar ao início'], 'Deseja criar novo cadastro? ')
            if res == 1:
                continue
            elif res == 2:
                break

    elif escolha == 3:
        cabeçalho('FINALIZANDO... VOLTE SEMPRE!')
        break

