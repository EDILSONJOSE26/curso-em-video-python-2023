'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.'''

carteira = float(input('Digite o seu valor R$ para converter em Dolar $: '))

cotacao = 4.98

s = carteira / cotacao

print(f'voçe possui ${s:.2f}')
