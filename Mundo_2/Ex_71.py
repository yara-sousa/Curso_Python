'''71- Crie um programa que simule o funcionamento de um 
caixa eletronico. No inicio pergunte ao usuario, qual sera o 
valor a ser sacado (numero inteiro) e o programa ira informar quantas 
sedulas de cada valor sera entregue. 
'''
print('=' * 30)
print('{:^30}'.format('Banco Afrollecer'))
print('=' * 30)
valor = int(input('Qual o valor do saque? R$'))
total = valor 
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20 
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        if ced == 2:
            ced = 0
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco Afrollecer! ')

         