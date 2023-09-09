''' Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''


num = float(input('Digite o valor do produto: '))

desconto = (num * 5) / 100

novo_preco = num - desconto

print(f'O produto teve desconto de 5%. Valor do desconto: R${desconto:.2f}. Total a pagar: R${novo_preco:.2f}')
