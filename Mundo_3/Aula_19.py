'''Nessa aula, vamos aprender o que são DICIONÁRIOS 
e como utilizar dicionários em Python. Os dicionários 
são variáveis compostas que permitem armazenar vários 
valores em uma mesma estrutura, acessíveis por chaves literais.
Tupla ()
Lista []
Dicionario {}


'''
dicionario = {}
dicionario = dict()
dicionario = {
    'nome': 'Yara',
    'idade': 21,
    'email': 'nunesyara441@gmail.com'
}
dicionario['sexo'] = 'F'
del dicionario['sexo']

filme = {
    'titulo': 'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values()) #Pegar todos os valores do dicionario
print(filme.keys()) #Pegar todas as chaves do dicionario
print(filme.items()) #Pegar todos os itens do dict

for k, v in filme.items():
    print(f'O {k} é {v}')

brasil = []
estado1 = {
    'uf': 'São Paulo',
    'sigla': 'SP',
}
estado2 = {
    'uf': 'Rio de Janeiro',
    'sigla': 'RJ',
}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])
