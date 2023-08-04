'''Crie um programa que tenha uma TUPLA totalmente preenchida com uma
contagem por extenção, de zero até vinte.
O programa devera ler um numero pelo teclado (entre 0 e 20) e
mostra-lo por extenso'''

       
numeros = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'outo', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeceis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
for cont in numeros:
    digite = int(input('Digite um numero: '))
    print(cont.index(digite))
    if digite > 20:
        break 
    
numeros = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'outo', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeceis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
while True:
    digite = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= digite <= 20:
        break
    print('tente novamente! \n', end='')
    
print(f'voce digitou o numero {numeros[digite]}')
    
        