#Condiçoes Simples, Compostas e simplificada 

#Simples
nome = str(input('Qual o seu nome? '))
if nome == 'Yara':
    print('Que nome lindo!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))   

#Compostas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('a sua media foi {:.1f}'.format(m))

if m >= 6.0:
    print('Sua media foi boa! PARABENS! ')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')

#Simplificada 
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('a sua media foi {:.1f}'.format(m))
print('PARABENS!!' if m >=6 else 'ESTUDE MAIS!')

