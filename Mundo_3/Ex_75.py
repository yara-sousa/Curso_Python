'''75 - Desenvolva um programa que leia 4 valores 
pelo teclado e guarde-os em uma tupla, no final, mostre:
A - Quantas veseds apareceu o valor 9
B - Em que posição foi digitado o primeiro valor 3
C - Quais foram os numeros pares.'''

#Minha solução
numero = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), 
          int(input('Digite um numero: ')), int(input('Digite um numero: ')))

print(f'O valor 9 aparece {numero.count(9)} veses')
if 3 in numero:
    print(f'O primeiro valor 3 esta na posição {numero.index(3)}° ')
else:
    print('O valor 3 nao foi digitado em nenhuma posição')

for i in range(8):
    if(i%2==0):
        print('Os numeros pares foram', i)

#Solução do Guanabara
 
numero = (int(input('Digite um numero: ')), int(input('Digite um numero: ')), 
          int(input('Digite um numero: ')), int(input('Digite um numero: ')))

print(f'O valor 9 aparece {numero.count(9)} veses')
if 3 in numero:
    print(f'O primeiro valor 3 esta na posição {numero.index(3)}° ')
else:
    print('O valor 3 nao foi digitado em nenhuma posição')

for i in range(8):
    if(i%2==0):
        print('Os numeros pares foram', i)

 
 

