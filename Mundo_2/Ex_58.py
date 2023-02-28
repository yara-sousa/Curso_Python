'''58 - Melhorar o desafio 28 onde o computador vai pensar 
em um numero entre 0 e 10. Só que agora p jpgador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessarios para vencer.'''
from random import randint

computador = randint(0, 10)
print('Sou seu computador... E acabei de pensar em um numero de 0 e 10.')
print('Sera que voce consegue adivinhar qual foi? ')
acertou = False
palpites = 0 
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True 
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou!! com {} tentativas! '.format(palpites))


