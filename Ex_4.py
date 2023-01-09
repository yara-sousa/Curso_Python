# ex 1
n = int(input('Digite um numero: '))
# a = n - 1
# s = n + 1
print('Analizando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))

# ex 2

n = int(input('Digite um numero '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}. '.format(n, d))
print('O tripolo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}'.format(n, t, n, r))

# ex 3

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2 
print('A media entre {} e {} é igual a {}'.format(n1, n2, média))

# ex 4
medida = float(input('Uma distancia em metros: '))
cm = medida * 100 
mm = medida * 1000
print('A distancia de {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))

# ex 5
num = int(input('Digite um numero para ver sua tabuada'))
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, num*4))
print('{} x {} = {}'.format(num, 5, num*5))
print('{} x {} = {}'.format(num, 6, num*6))
print('{} x {} = {}'.format(num, 7, num*7))
print('{} x {} = {}'.format(num, 8, num*8))
print('{} x {} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))
