# Ultilizando os Modulos
import math 
from math import sqrt, floor
import random
import emoji

 
#EX 1
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))

#EX 2
num = random.randint(1, 10)
print(num)

#emoji
print(emoji.emojize("Olá, Mundo :sunglasses:"))

#EX 3
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.trunc(num)))

#EX 4
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adiacente: '))
hi = (co ** ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}')