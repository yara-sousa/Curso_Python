'''50 - Desenvolva um porgrama que mostre 6 numeros inteiros
e mostre a soma apenas dos que forem pares. se o valor for 
impar desconsidere-o.'''
soma = 0 
cont = 0
for i in range(1, 7):
    num = int(input('Digite 0 {}° numero: '.format(i)))
    if num % 2 == 0:
        soma += num
        cont += 1
print("Voce informou {} numeros e a soma foi {}".format(cont, soma))