'''53 - Crie um programa que leia uma frase qualquer 
e diga se ela é um palindromo,
descosiderando os espaçoes 
EX: APOS A SOPA 
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO 
ANOTARAM A DATA DA MARATONA'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() #Separa as palavras 
juntos = ''.join(palavras) #Ajunta as palavras
inverso = ''
for letra in range(len(juntos) -1, -1, -1):
    inverso += juntos[letra]
print('O inverso {} é {} '.format(juntos, inverso))
if inverso == juntos:
    print('Temos um PALINDROMO!')
else:
    print('Nao é um Palindromo!')
