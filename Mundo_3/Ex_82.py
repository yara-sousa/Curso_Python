'''82 - Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente. Ao final, 
mostre o conteúdo das três listas geradas. '''

num = []
par = []
imp = []
while True:
    num.append(int(input('Digite um numero: ')))
    
    cont = str(input('Quer continuar? (S/N)'))
    if cont in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        imp.append(v)
print('~~' * 15)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista ded impares é {imp}')
