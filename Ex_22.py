"""
22 - Criar um programa que leia o nome completo de uma pessoa e mostra:
- O nome com todos as letras maiusculas e minusculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""

nome = str(input('  Yara Nunes de Sousa'))
print(nome.upper())
print(nome.lower())
print(nome.count('Yara Nunes de Sousa'.format(len(nome) - nome.count(' '))))
print(len('yara'))

