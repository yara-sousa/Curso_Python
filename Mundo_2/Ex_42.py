'''42 - Refaça o desafio 35, acresentando o recurso de mostrar
qual triangulo sera formado:
- EQUILATERO: Todos os lados iguais 
- ISÓSCALES: dois lados iguais 
- ESCALENO: Todos os lados diferentes
'''
r1 = float(input('Primeiro segmento: ')) 
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r3 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos assima PODEM formar um triangulo')
    if r1 == r2 == r3:
        print('HEQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO! ')
    else:
        print('ISOSCELES! ')
else: 
    print('Os segmentos assima NAO PODEM formar um triangulo')