#EX 1
import math
import random 

angulo = float(input('Digite o angulo que voce deseja:'))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

#EX 2
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

#EX 3
import random 

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentaçao será ')
print(lista)

#EX 4 

import pygame

pygame.init()
music = pygame.mixer.music.load('ex7.mp3')
pygame.mixer.music.play(loops=-1)
pygame.event.wait()

#EX 5
preço = float(input('Qual o preço do produto? R$'))
valor_descontado = (preço * 35 / 100)
print('O produto que custava R${}, teve R${} de desconto'.format(preço, valor_descontado))

#EX 6 

frase = 'Curso em Video Python'
print(frase.replace('Python', 'Andro', new))



