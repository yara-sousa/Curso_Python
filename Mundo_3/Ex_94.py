'''94 - Crie um programa que leia nome, sexo e idade de 
varias pessoas, guardando os dados de cada pessoa em 
um dicioario e todos os dicionarios em uma lista, No final, mostre:
A) Quantas pessoas foram cadastradas
B) A media de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da media'''
galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F. ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N ')
    if resp == 'N':
        break
print('_'*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas. ')
media = soma / len(galera)
print(f'A media de idade é de {media} anos. ')
print(f'As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()