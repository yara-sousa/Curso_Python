'''25 - Crie um programa que leia 
o nome de uma pessoa e diga se ela 
tem "NUNES" no nome.
'''
nome = str(input('Qual é seu nome? ')).strip()
print('Seu nome tem Nunes? {}'.format('nunes' in nome.lower()))