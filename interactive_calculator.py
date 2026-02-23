import time

n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
opcao = 0
while opcao != 5:
    print('========<<<<>>>>========')
    menu = '''informe uma operação:
[1] soma
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
>>>>>>>'''
    opcao = int(input(menu))
    if opcao == 1:
        print('{} + {} = {} '.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('{} x {} = {} '.format(n1, n2, n1*n2))
    elif opcao == 3:
        if n1 < n2:
            print('O segundo valor é maior.')
        elif n1 == n2:
            print('Valores iguais.')
        else:
            print('O primeiro valor é maior. ')
    elif opcao == 4:
        print('Digite os novos valores:')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('opção inválida. ')
    time.sleep(1)
print('Fim do programa.')    
