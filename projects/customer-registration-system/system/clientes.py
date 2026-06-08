from .interface import*
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
        print('Arquivo criado com sucesso!')
    except Exception as error:
        print('Falha ao criar!', error)


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo! ')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for pos, linha in enumerate(a, start=1):
            dados = linha.strip().split(';')
            nome = dados[0]
            idade = dados[1]
            print(f'{pos} - {nome:<15} {idade:<3} anos')
        a.close()


def cadastroNovo(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao adicionar cadastro na lista')
        else:
            print(f'Cadastro: {nome}, {idade} anos adicionado com sucesso!')
            a.close()
            