'''55 - Faça um programa que leia o peso de 5 pessoas
e no final mostre qual foi o maior e qual foi o menor'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}° pessoa'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O maior peso lindo foi de {}kg'.format(menor))
