'''31 - Desenvolva um programa que pergunte
a distancia de uma viagem em Km, 
Calcule o preço da passagem, cobrando R$0.50 por Km
para viagens de até 200km e R$0,45 para viagens mais longas.
'''
distancia = float(input('Qual é a distancia da sua viagem? '))
print('Voce esta prestes a começar uma viagem de {}Km. ')
#Composto
'''if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45'''
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
#Simplificado
print('E o preço da sua passagem sera de R${:.2f}'.format(preço))