'''70 - Crie um programa onde o usuario possa digitar
varios numeros e cadastre-os em uma lista. Caso o numero ja exista 
la dentro, ele nao sera adicionado. No final serao exibidos todos os valores
unicos digitados, em ordem crescente'''

numeros = list()
while 1:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    
    r = str(input('Quer Continuar? (S/N):'))
    if r in 'Nn':
        break
    
print('~' * 30)
numeros.sort()
print(f'Voce digitou {numeros} valores')


numeros = list()
while True:
    n = int(input('Digite um numero: '))
    if n not in numeros:
        numeros.append()
        print('Valor adicionado')
    else:
        print('Nao adicionamos valores duplicados ')
    r = str(input('Quer continuar? (N/S): '))
    if r in 'Nn':
        break
    
print('~' * 30)
numeros.sort()
print(f'Voce digitou {numeros} valores')

















