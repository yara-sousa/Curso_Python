cont = 1
while True:
    print(cont, '-> ', end='')
    cont += 1
    break
print('Acabou')

n = s = 0
while True:
    n = int(input('Digite um numero'))
    if n == 999:
        break
    s += n
#print('Soma vale {}'.format(s))
print(f'A soma vale {s}') #python 3 


nome = 'Yara'
idade = 22
salario = 5345.99
print(f'A {nome:^20} tem {idade} anos e seu salario é {salario:.2f}')

