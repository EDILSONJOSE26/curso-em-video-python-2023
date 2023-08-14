'''Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.'''

num = int(input('Digite um valor: '))

d = num * 2
t = num * 3
rq = num**(1/2)

print(f'O dobro é {d}')
print(f'O triplo é {t}')
print(f'A raiz quadrada é {rq:.2f}')