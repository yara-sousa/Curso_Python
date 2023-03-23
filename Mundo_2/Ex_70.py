'''70 - Crie um programa que leia o nome e o preço de varios produtos.
O programa devera perguntar se o usuario quer continuar ou nao, e no final mostre 
a) qual é o total de gasto da compra. b) quantos produtos custam mais de R$1000
c) qual é o nome do produto mais barato.
'''
total = prod = menor = cont = 0 
barato = ''
while 1:
    produto = str(input('Qual é o produto: '))
    preço = float(input('Qual o valor: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        prod += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total gasto de compras: {total:10.2f}')
print(f'Total de produtos acima de R$1000: {prod}')
print(f'Produto mais barato: {barato} de R${menor:.2f}')
