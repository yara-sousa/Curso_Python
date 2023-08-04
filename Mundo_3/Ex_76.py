'''76 - Crie um programa que tenha uma tupla unica
com nomes de produtos e seus respectivos preços, 
na sequencia. No final, mostre uma listagem de 
preços, organizando os dados de forma tabular.'''

#Minha solução
table_prod = ('Notebook', 'R$5980,00', 
              'Monitor', 'R$329,90', 
              'Iphone14', 'R$4500,00', 
              'Tablet', '1799,90',
              'Cabo USB', '229,90',
              'Haedset', '430,00')

print(f'Tabela de produtos\n {table_prod}')

#Solução do Guanabara
print('_'*40)
print(f'{"LISTA DE ITENS":^40}')
print('_'*40)
listagem = ('Notebook', 5980.00, 
              'Monitor', 329.90, 
              'Iphone14', 4500.00, 
              'Tablet', 1799.90,
              'Cabo USB', 229.90,
              'Haedset', 430.00)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]: >7.2f}')
print('_'*40)
