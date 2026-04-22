try:
    n = int(input('Digite um número: '))
    print('1 - Binário \n2 - Octal \n3 - Hexadecimal')
except ValueError:
    print('Erro. Coloque um número inteiro. ')

opcao = int(input('Qual será a base de conversão?: '))

if opcao == 1:
    print('O número {} convertido para binário é {:b}.'.format(n, n))
elif opcao == 2:
    print('O número {} convertido para Octal é {:o}.'.format(n, n))
elif opcao == 3:
    print('O número {} convertido para Hexadecimal é {:x}.'.format(n, n))
else:
    print('Valor Inválido.')
