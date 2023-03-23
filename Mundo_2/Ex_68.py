''' 68 - Faça um programa que jogue par ou impar 
com o computador. O jogo sera interrompido quando o 
jogador PERDER, mostrando o total de vitorias 
concecutivas que ele conquistou ao final do jogo'''
from random import randint #Tras numeros aleartorios
v = 0
while 1:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador 
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador jogou {computador}, Total de {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce Venceuu!! ')
            v += 1
        else:
            print('Voce Perdeuu!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce Venceuu!!')
            v += 1 
        else:
            print('Voce Perdeuu!!')
            break
    print(f'GAME OVER! Voce venceu {v} vezes. ')
print('Vamoos jogar novamente? ')