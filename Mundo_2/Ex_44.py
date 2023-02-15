''' 44 - Elabore um programa que calcule o valor a ser pago por 
uma compra considerando o seu preço normal e a condição de pagamento 
- dinhero ou pix/vista: 10% de desconto - em ate 2x no cartao: preço normal
- a vista no cartao: 5% de descono      - 3x ou mais no cartao: 20% de juros 
'''
print('{:_^40}'.format('AFROLLECER'))
preço = float(input('Valor total R$'))
print('''FORMAS DE PAGAMENTO
[1] Á vista dinheito/pix
[2] Á vista cartao
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Escoplha a forma de pagamento: '))
if opção == 1:
    total = preço - (preço * 10 / 100 )
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço 
    parcelas = total / 2
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas?'))
    parcelas = total / totparc
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS!'.format(totparc, parcelas))
else:
    total = preço
    print('Opção invalida')
print('Sua compra de {:.2f} vai custar R${:.2f}'.format(preço, total))