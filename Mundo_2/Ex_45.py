''' 45 - Crie um programa que faça o computador jogar 
jokenpo com voce.
'''
from random import randint
from time import sleep  
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opçoes:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
       print('EMPATE') 
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALID! ')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')    
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALID! ')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALID! ')