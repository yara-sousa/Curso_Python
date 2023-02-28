''' 64 - crie um programa que leia varios numeros inteiros pelo techado.
o programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada 
no final mostre quantos numeros foram digitados e qual foi a soma entre eles 
(desconsiderando o flog)'''
num = 0
cont = 0
while num != 999:
    num = int(input('Digite um numero: [ou 999 - para parar o programa]'))
    cont += 1
print('Acabou')