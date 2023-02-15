'''46 - Faça um programa que mostre na tela uma contagem 
regressiva para estouro de fogos de artificios, 
indo de 10 até 0, com uma pausa de 1 segundo entre eles'''
from time import sleep

for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('BUMMM!!!')