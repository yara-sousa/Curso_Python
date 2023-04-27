'''PRATICA'''

lanche = ('Hamburguer', 'suco', 'pizza', 'pudim', 'milk')

print(sorted(lanche))

# print(len(lanche))

# for comida in lanche:
#     print(f'Eu vou comer {comida}\n')

for cont in range(0, len(lanche)):
    print(f'eu vou comer {lanche[cont]} na posição {cont}')

for pos, comida in enumerate(lanche):
    print(f'{pos} Eu vou comer {comida}\n')
print('Comi pra caramba!')

a = (1, 3, 7,)
b = (2, 4, 6, 8)
c = a + b
print(c.index(1, 1))


pessoa = ('Yara', 21, 'm', 66.65)
del(pessoa)
print(pessoa)
