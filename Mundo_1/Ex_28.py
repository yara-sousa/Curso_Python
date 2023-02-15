'''28 - Escreva um programa que 
faça o computador 'pensar' em 
um numero inteiro entre 0 e 5 e peça para o usiario tentar descobrir qual foi
o numero escolhido pelo computador. O programa deverá escrever na tela se o usuario venceu ou perdeu.
'''
from random import randint # sorteia numeros 

computador = randint(0, 5)
print('Pensei no numero {}'.format(computador))
print('-=-' * 10)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))

if jogador == computador:
    print('Parabens voce venceu!! ')
else:
    print('Ganhei eu pensei no {} e nao no {}!!'.format(computador, jogador))
    
