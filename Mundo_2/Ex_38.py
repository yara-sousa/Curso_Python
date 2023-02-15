'''38 -Escreva um programa que leia dois numeros inteiros 
e compare-os mostrando na tela uma mensagem:
O primeiro valor é o maior 
o segundo valor é o maior 
Nao existe vamor maior, os dois sao iguais 
'''
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1: 
    print('O segundo valor é maior ')
elif n1 == n2:
    print('Os dois valores são iguais')