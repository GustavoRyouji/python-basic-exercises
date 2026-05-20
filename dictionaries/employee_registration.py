#programa de criação de registro de trabalhadores
from datetime import datetime
registro = {}
registro['nome'] = input('Nome: ')
nasc = int(input('Ano de Nascimento: '))
registro['idade'] = datetime.now().year - nasc
registro['ctps'] = int(input('Carteira de Trabalho (0 se não tem): '))
if registro['ctps'] != 0:
    registro['Ano_de_Contratação'] = int(input('Ano de Contratação: '))
    registro['salario'] = float(input('Salário: '))
    registro['aposentadoria'] = registro['idade'] + ((registro['Ano_de_Contratação'] + 35) - datetime.now().year)


print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
for k, v in registro.items():
    print(f' - {k.replace("_"," ").title()}: {v}')
