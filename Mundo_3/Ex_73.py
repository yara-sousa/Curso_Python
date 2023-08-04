'''Crie uma tupla preenchida com os 20 primeiros
colocados da tabela do campeonato brasileiro de futbol, 
na ordem de colocação. Depois mostre.
A - Os 5 primeiros times
B - os ultimos 4 colocados 
C - times em ordem alfabetica
D - Em que posição esta o time do corinthis '''

#Minha Solução 

times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Internacional',
'Fluminence', 'Cruzeiro', 'Gremio', 'Sao Paulo', 'Vasco da Gama',
'Atletico - MG', 'Santos', 'Bragantino', 'Flamengo', 'Athletico - PR', 
'Bahia', 'Goias', 'Corinthians', 'Cuiaba', 'Curitiba', 'America - MG')

print('='*30)
print(f'Os 5 primeiros colocados sao os') 
for cont in range(0, 4):
    print(f'Time {times[cont]} na posição {cont+1}')
    
print('='*30)
print(f'Os ultimos 4 colocados sao os') 
for cont in range(16, 20):
    print(f'Time {times[cont]} na posição {cont+1}')

print('='*30)
print('Times em Ordem alfabetica', end='')
print(sorted(times))

print('='*30)
print(f'Posição em que o time do corinthias esta') 
for cont in range(16, 17):
    print(f'Time {times[cont]} na posição {cont}')


#Solução do Guanabara

times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Internacional',
         'Fluminence', 'Cruzeiro', 'Gremio', 'Sao Paulo', 'Vasco da Gama',
         'Atletico - MG', 'Santos', 'Bragantino', 'Flamengo', 'Athletico - PR', 
         'Bahia', 'Goias', 'Corinthians', 'Cuiaba', 'Curitiba', 'America - MG')
print('='*30)
print(f'Lista de times: {times}')
for t in times:
    print(t)
print('='*30)
print(f'Os 5 primeiros são: {times[0:5]}')

print('='*30)
print(f'Os 4 ultimos sao {times[-4:]} ')

print('='*30)
print(f'times em ordem alfabeticas: {sorted(times)}')

print('='*30)
print(f'O cotinthias esta na {times.index("Corinthians")+1}a posição')
