'''Variaveis compostas (listas) sao mutaveis
'''
num = (1, 2, 3, 4) > ("tupla")
num = [2, 4, 5, 6] > ["lista"]
num = {3, 5, 1, 6} > {"dicionario"}

num = [2, 4, 6, 8]
num[2] = 3
num.append(7) #Adiciona o elemento ao final da lista
num.sort(reverse=True) #Organiza ou reverte a ordem
num.insert(2, 0)
num.pop()
print(f'Essa lista tem {len(num)} elementos')
