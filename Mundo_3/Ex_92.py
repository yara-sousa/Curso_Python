'''92 -  Crie um programa que leia nome, ano de nascimento 
e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá 
também o ano de contratação e o salário. Calcule e acrescente, 
além da idade, com quantos anos a pessoa vai se aposentar. '''
from datetime import datetime
dados = dict()
dados['nome']  = str(input('Nome: '))
nacs = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nacs
dados['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salario: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 30) - datetime.now().year)
print('_'* 30)
for k, v in dados.items():
    print(f'  - {k} é de {v}')
