'''Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.'''

metro = float(input('Digite o valor em metros: '))

c = metro * 100
m = metro * 1000

print(f'O valor em metros convertido para centimetros é igual a {c:.2f} e em milimetros é {m:.2f}')