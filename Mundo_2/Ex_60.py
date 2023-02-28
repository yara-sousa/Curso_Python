'''60 - Faça um programa que leia um numero qualquer 
e mostre o seu fatorial. 
ex:
5! = 5x4x3x2x1 = 120 '''
from math import factorial

n = int(input('Digite um numero para calcular o seu fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}'.format((n, f)))
 
#tradicional 
n = int(input('Digite um numero para calcular o seu fatorial: '))
c  = n 
f = 1
print('Calculando {}! ='.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
    
#Utilizando o for 
n = int(input('Digite um numero para calcular o seu fatorial: '))
f  = 1
for i in range(n, 0, -1):
    f *= n
print('Calculado {}!'.format(f), end='')
    


