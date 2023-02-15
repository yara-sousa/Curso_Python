"""23 - Faça um programa que leia um numero de 0 a 9999 e mostra na tela cada um dos digitos separados.
ex: Digite um numero: 1867
unidade: 4 dezena: 3 centena: 8 milhar: 1
"""

numero = int(input('Digite um numero'))
num = str(numero)
print('Analizando o numero {}'.format(num))
print('Unidade {}'.format(num[3]))
print('Dezena {}'.format(num[2]))
print('Centena {}'.format(num[1]))
print('Milhar {}'.format(num[0]))
