'''40 -Crie um programa que leia duas notas de um aluno 
e calcule sua media.
mostrando uma mensagem no final, de acordo com a media atingida:
- Media abaixo de 5.0: Reprovado
- Media entre 5.0 e 6.9: Recumperação
- Media 7.0 ou superior: Aprovado
'''
nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Segunda nota'))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(nota1, nota2, media))
if 7 > media <= 5:
    print('O aluno esta em RECUMPERAÇÃO. ')
elif media > 5:
    print('O aluno esta REPROVADO. ')
else: 
    media >= 7
    print('O aluno esta APROVADO')
        

