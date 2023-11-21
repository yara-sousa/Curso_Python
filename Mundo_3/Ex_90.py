'''90 - Feaça um programa que leia o nome e a media de um aluno,
guardando tambem a sintuação em um dicionario. No final, mostre
o conteudo da estrutura na tela.'''

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recumperação'
else:
    aluno['situação']= 'Reprovado'
print('_'* 30)
for k, v in aluno.items():
    print(f'-  {k} é igual a {v}')
    