'''47 - Crie um programa que mostre uma tabela com todos 
os numeros pares'''

for i in range(2, 51, 2):
    print('°', end='')
    if i % 2 == 0: 
        print(i, end=' ')
print('ACABOU!')