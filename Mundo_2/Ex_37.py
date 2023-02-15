'''37 - Escreva um programa que leia um numero 
inteiro qualquer e faça para o usuario escolher 
qual a base de conversao
1 para binario 
2 para octal 
3 para hexadecimal
'''
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para coversão: 
[1] Converter para BINARIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamnete!')