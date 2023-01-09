'''anotacoes 
TIPOS PRIMITIVOS 
int = 7 -4 0 9875
float = 4.5 0.076 -15.223 7.0
bool = True False
string = 'Olá' '7.5' "bola" ''

comandos 
print
input 
valiaveis = 3

metodo 
.format() formata valores 
type() descobre o tipo do valor 

'''
print('Olá, Mundo!')

n1 = int(input('Digite um numero'))
n2 = int(input('Digite mais um numero:'))
s = n1 + n2 
#print('a soma vale', s)
#print('A soma entre', n1, 'e', n2, 'vale', s)
print('a soma entre {} e {} vale {}'.format(n1, n2, s)) 

