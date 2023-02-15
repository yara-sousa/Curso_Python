'''39 - Faça um programa que leia o ano de nascimento de um jovem 
e informe. Se é a hora de se alistar ou se ja passou do tempo de alistamento.
Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

atual = date.today().year
nasc = int(input('Ano de nascimento: '))
sex = str(input('Qual seu genero sexual? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}. '.format(nasc, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento sera em {}'.format(ano))
else:
    idade > 18
    saldo = idade - 18
    print('Voce ja deveria ter se alstado ha {} anos. '.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
    
