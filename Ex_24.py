''' 24 - Crie um programa que leia 
o nome de uma cidade e diga se 
ela começa ou nao com o nome 
'SANTO'.
'''
cid = str(input('Digite o nome de uma cidade: ')).strip()
print(cid[:6] == 'Santos')