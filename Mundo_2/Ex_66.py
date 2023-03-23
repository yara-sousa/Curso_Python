''' 66 - Crie um programa que leia varios numeros interios pelo teclado 
o programa só vai parar quando o usuario digitar o numero 999, no final 
mostre quantos numeros foram digitados e mostre qual foi a soma entre eles 
desconsiderando o fleg'''

soma = cont = 0 
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    else:
        cont += 1
        soma += n
print(f'Voce digitou {cont} numeros')
print(f'A soma dos numeros digitados é {soma}')
    