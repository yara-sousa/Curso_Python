'''49 - Refaça o desafio 9 usando a 
tabuada que o usuario escolher, só que agora ultilizando 
o laço for
'''
num = int(input('Digite um numero para ver a tabuada: '))
for i in range(1, 11):
    print('{} x {:2} = {}'.format(num, i, num*i))