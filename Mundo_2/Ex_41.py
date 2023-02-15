'''41 - A Convederação Nacional da Natação precisa de um 
programa que leia o ano de nascimento de um atleta 
e mostre sua categoria de acordo com a idade:
- Ate 9 anos: MIRIM
-Ate 14 anos: INFANTIL
-Ate 19 anos: JUNIOR 
-Ate 25 anos: SENIOR 
-Acima de 25 anos: MASTER
'''
from datetime import date
atual = date.today().year
nascimento = int(input('Ano de Nacimento: '))
idade = atual - nascimento 
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SENIOR')
else:
    idade > 25
    print('Classificação: MASTER')
    