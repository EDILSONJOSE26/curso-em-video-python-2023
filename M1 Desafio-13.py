'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''

salario_funcionario = float(input('Digite o valor do salário do funcionario: '))

aumento = (salario_funcionario * 15) / 100

salariocomalmento = salario_funcionario + aumento

print(f'o salario do funcionario atual é de R${salario_funcionario:.2f} com o aumento de 15% ficara no valor de R${salariocomalmento:.2f}')