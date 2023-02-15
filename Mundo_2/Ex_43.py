''' 43 - Desenvolva uma logica que leia o peso e a altura de uma pessoa,
calcule seu IMB e mostre seu status de acordo com a tabela abaixo: 
- Abaixo de 18.5: abaixo do peso   - 25 até 30:Sobrepeso
- Entre 18.5 e 25: Peso ideal      - 30 até 40:Obesidade
                                   - Acima de 40: Obesidade morbita 
'''

peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura?'))
imc = peso / (altura ** 2)
result = imc
if result < 18.5:
    print('Esta abaixo do peso')
elif result >= 18.5 and result < 25:
    print('Esta no peso ideal')
elif result >= 25 and result < 30:
    print('Esta sobrepeso')
elif result >= 30 and result < 40:
    print('Esta cim obesidade')
else:
    result > 40
    print('Obesidade morbita')
print('E seu IMC é de {:.1f}'.format(imc))