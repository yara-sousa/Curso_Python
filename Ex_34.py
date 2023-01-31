'''34 - Escreva um programa que pergunte o salario 
de um funcionario e calcule o valor do seu aumento. 
Para salarios superiores a R$1250,00. Calcule um aumento de 10%.
Para os inferiores ou iguais. o aumento sera de 15%.
'''
salario = float(input('Qual é o salario do funcionario do Itau? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))