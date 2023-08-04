'''74 - Crie um programa que vai gerar cinco numeros 
aleartorios e colocar em uma tupla. Depois disso 
mostre a listagem de numeros gerados e tambem 
indique o menor e o maior valor que estao na tupla'''
#minha soluçao 
from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), 
           randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os numeros digitados foram {randint(0, 6)}')

#Solução do Guanabara 
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:\n ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\n O maior valor sorteado foi {max(numeros)}')
print(f'\n O menor valor sorteado foi {min(numeros)}')