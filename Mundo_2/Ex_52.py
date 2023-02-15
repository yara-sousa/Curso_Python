'''53 - Faça um programa que leia um numero 
interio e diga se ele é ou nao um numero primo.'''
num = int(input('Digite um numero: '))
tot = 0
for i in range(1, num + 1):
    if num % i == 0:
      print('\033[33m', end='')
      tot += 1   
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
    
print('\n\033[mO numero {} foi divisivel {} veses'.format(num, tot))
if tot == 2:
    print('Por isso o numero é PRIMO!')
else:
    print('E por isso ele nao é PRIMO!')