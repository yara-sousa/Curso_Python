'''62 - Melhorando o desafio 61, pergunttando se o usuario
quer mostrar mais  alguns termos. O programa incerra quando ele
disser que quer mostrar 0 termos.
'''
print('Gerador de PA')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos quer mostrar a mais? '))
print('progressao finalizada com {} termos'.format(total))