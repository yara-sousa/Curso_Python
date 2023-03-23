'''67 - Faça um programa que mostre a tabuada de varios numeros, um de cada vez
para cada valor digitado pelo usuario. O programa sera interrompido quando o numero 
solicitado for negativo'''

print('TABUADA DE VALORES')
print('-'*30)
while True:
    num = int(input('Digite um numero para ver a tabuada '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
print('Opção invalida', 'Fim do jogo')
