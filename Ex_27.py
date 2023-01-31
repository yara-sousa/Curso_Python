'''27 - Faça um programa que leia
o nome completo de uma pessoa, mostrando o primeiro e 
o ultimo nome 
ex: Ana Maria Sousa
primeiro = Ana
ultimo = Sousa 
'''
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em conhece-lo! ')
print('O primeiro nome é {}'.format(nome[0]))
print('O ultimo nome é {}'.format(nome[-1]))
