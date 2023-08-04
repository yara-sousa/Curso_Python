'''77 - Crie um programa que tenha uma tupla com varias palavras
(não usar acentos). Depois disso, voce deve mostrar, para cada palavra, 
quais sao as suas vogais.'''


palavras = ('Coragem', 
            'Determinacao',
            'Conquistar',
            'Sonhos', 
            'Inteligencia',
            'Aprender',
            'Estudar',
            'Programar',
           )
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')



palavras = ('Estudar',
            'Amor',
            'Familia',
            'Conquistas',
            'Felicidade')

for p in palavras:
    print(f'\nNA palavra {p.upper()} temos')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            