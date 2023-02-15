'''48 - Faça um programa que calcure toda a soma dos
numeros impares que sao multiplos de três e se se encontram no intervalo
de 1 até 500.
'''
soma = 0
cont = 0
for i in range(1, 503, 2):
    if  i % 3 == 0:
        cont += 1
        soma += i
print('A soma de todos os valores solucitados é {} valores solicitados é {}'.format(cont, soma))