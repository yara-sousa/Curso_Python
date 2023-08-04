'''78 - Faça um programa que leia 5 valores numericos 
e guarde-os em uma lista. No final mostre qual foi o 
maior e o menor valor digitado e as suas respectivas posições na lista.
'''

num = [] 
mai = 0
men = 0
for i in range(0, 5):
    num.append(int(input(f'Digite um numero para posição {i}:')))
    if i == 0:
        mai = men = num[i]
    else:
        if num[i] > mai:
            mai = num[i]
        if num[i] < men:
            men = num[i]
        
print('~'* 30)
print(f'Essa lista tem {num} numeros')
print(f'O maior valor é {mai}')
print(f'O menor valor é {men}')

