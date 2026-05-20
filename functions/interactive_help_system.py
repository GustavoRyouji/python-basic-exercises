def ajuda(com):
    help(com)


print('-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-')
print('MENU DE INFORMAÇÕES DO PYTHON')
print('-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-')
while True:
    comando = str(input('Função ou biblioteca: '))
    if comando.upper() in 'FIM':
        print('FINALIZANDO...')
        break
    else:
        ajuda(comando)