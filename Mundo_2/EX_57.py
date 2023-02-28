'''57 - Faça um programa que leia o sexo de uma pessoa, 
mas só aceita os valores 'm' ou 'f'. Caso esteja errado,
peça a digitação novamente'''

sexo = str(input('Informa o seu sexo [F/M]: ')).strip().upper()[0]
print(sexo)
while sexo not in 'MnFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo:')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))