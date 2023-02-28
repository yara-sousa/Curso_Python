'''59 - Crie um programa que leia dois valores                              
e mostre um menu como ilustrado abaixo, na tela: 
Seu programa devera realizar operação solicitada em cada caso.
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros 
[5] sair do programa'''
from time import sleep

opção = 0 
num1 = int(input('Digite um numero'))
num2 = int(input('Digite outro numero'))
while opção != 5:
    print('''_____Menu____
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros 
    [5] sair do programa''')
    opção = int(input('>>>>>>> Qual opção deseja escolher:'))
    if opção == 1:
        soma = num1 + num2
        print('A soma entre {} + {} é {}'.format(num1, num2, soma))
    elif opção == 2:
        produto = num1 * num2
        print('O resultado entre {} * {} é {}'.format(num1, num2, produto))
    elif opção == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior é {}'.format(num1, num2, maior))
    elif opção == 4:
        print('Informe os numeros novamente: ')
        num1 = int(input('Digite um numero'))
        num2 = int(input('Digite outro numero'))
    elif opção == 5:
        print('Finalizado... ')
    else:
        print('Opcção invalida, tente novamnete ')
    sleep(2)
print('Fim do programa! ')