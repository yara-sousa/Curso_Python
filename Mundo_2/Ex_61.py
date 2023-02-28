'''61 - Refaça o desafio 51, lendo o primeiro termo
e a razão de uma PA, mostrando os 10 primeiros termos da progressao 
usando a extrutura while.'''

print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Acabou')