'''Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''

entrada = input('Digite algo: ')

print(f'{entrada.isalnum()}')
print(f'{entrada.isalpha()}')
print(f'{entrada.isascii()}')
print(f'{entrada.isdecimal()}')
print(f'{entrada.isdigit()}')
print(f'{entrada.isidentifier()}')
print(f'{entrada.islower()}')
print(f'{entrada.istitle()}')
print(f'{entrada.isspace()}')
print(f'{entrada.isprintable()}')
print(f'{entrada.isupper()}')