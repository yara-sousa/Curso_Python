'''35 - Desenvolva um programa que leia o cmprimento 
de três retas e diga ao usuario
se elas podem ou nao formar um triangulo.  
'''
def analise_triangulo():
    
    print('-=' *20)
    print('Analizador de Triangulos')
    r1 = float(input('Primeiro segmento: ')) 
    r2 = float(input('Segundo segmento: '))
    r3 = float(input('Terceiro segmento: '))
    if r1 < r3 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('Os segmentos assima PODEM formar um triangulo')
    else: 
        print('Os segmentos assima NAO PODEM formar um triangulo')