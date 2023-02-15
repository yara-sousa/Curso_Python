'''54 - Crie um prigrama que leia o ano de 
nascimento de uma pessoa e mostre quantas pessoas ainda
não atingiram a maioridade e quantos ja sao maiores  
'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 1
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Total de maior de idade {}'.format(totmaior))
print('Total de menor de idade {}'.format(totmenor))