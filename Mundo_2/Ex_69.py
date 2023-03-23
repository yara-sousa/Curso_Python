'''69 - Crie um programa que leia a idade e o sexo de varias pessoas, a cada pessoa cadastrada, o programa devera
perguntar se o usuario quer ou nao continuar. No final mostre: 
a) quantas pessoas tem mais de 18 anos. b) quantos homens foram cadastrados. c) quantas mulheres 
tem menos de 20 anos.
'''
tot18 = totH = totM20 = 0
while 1:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1 
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1          
    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if res == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens cadastrados: {totH}')
print(f'Total de Mulheres com menos de 20 anos: {totM20}')