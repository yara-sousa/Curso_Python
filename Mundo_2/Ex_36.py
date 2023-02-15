'''36 -     Escreva um programa para aprovar um emprestimo bancario
para o compra de uma casa, pergunte o valor da casa,
o salario do comprador e em quantos anos ele vai pagar.
A prestação mensal nao pode exceder 30% do salario ou entao o emprestimo 
sera negado.
'''
casa = float(input('Qual é o valor do imovel? '))
salario = float(input('Qual é o valor da sua renda mensal? '))
anos = int(input('Quantos anos de pagamento? '))
prest = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos'.format(casa, anos),  end=' ')
print('A prestação sera de R${:.2f}'.format(prest))
if prest <= minimo:
    print('Emprestimo pode ser CONCEDIDO! ')
else:
    print('Emprestimo NEGADO!')
    
