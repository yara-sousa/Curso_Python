# EX 1 
real = float(input('Digite o valor que deseja converter? R$ '))
dolar = real / 5.22
euro = real / 5.61
print('Com R$ {:.2f} você pode comprar US$ {:.2f}. e você pode comprar €$ {:.2f}'.format(real, dolar, euro))


# EX 2
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt 
print('A parede tem a dimenssão de {}x{} e sua area é de {}m².'.format(larg, alt, área))
tinta = área / 2 
print('Para pintar essa parede, voce precisara de {}l de tinta '.format(tinta))

#EX 3 
preço = float(input('Qual é o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(preço, novo))

#EX 4
salario = float(input('Qual é o salario do funcionario? R$ '))
novo = salario + (salario * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15%, de aumento passa a receber R${:.2f}'.format(salario, novo))

#EX 5 
c = float(input('Informe a temperatura em C: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {0}°C corresponde a {1}°F!'.format(c, f))

#EX 5

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é ded R${:.2f}'.format(pago))
