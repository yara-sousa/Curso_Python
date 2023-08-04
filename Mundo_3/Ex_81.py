'''81 - Crie um programa que vai ler vários números e colocar em uma lista.                  
Depois disso, mostre:                                                                                                                                                
A) Quantos números foram digitados.                                                                                                                    
B) A lista de valores, ordenada de forma decrescente.                                                                                          
C) Se o valor 5 foi digitado e está ou não na lista. '''

numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    
    s = str(input('Quer continuar? (S/N)'))
    if s in 'Nn':
      break    
 
print(f'Foram digitados {len(numeros)} numeros')
numeros.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é {numeros}')
if 5 in numeros:
    print('O valor 5 esta na lista')
else:
    print('O numero 5 nao foi encontrado na lista')
