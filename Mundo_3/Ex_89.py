'''89 - Crie um programa que leia nome e 
duas notas de vários alunos e guarde tudo 
em uma lista composta. No final, mostre um 
boletim contendo a média de cada um e permita 
que o usuário possa mostrar as notas de cada 
aluno individualmente.'''

ficha = []
while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Deseja continuar? [S/N]"))
    if resp in 'Nn':
        break      
print('__'*30)
print(f'{"N° ":<4}{"NOME":<10}{"MÉDIA":>8}')
print("__"*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print("__"*30)
    opc = int(input("Mostrar notas de qual aluno? [Digite (111) para interromper]"))
    if opc == 111:
        print("Finalizado...")
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]}são {ficha[opc][1]}")
print('>>> Volte sempre!! <<<')