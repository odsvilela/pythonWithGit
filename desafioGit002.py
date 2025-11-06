#Calculadora Simples
import math
print('-='*20)
print(f'{'CALCULADORA':^40}')
print('-='*20)

while True:
    n1 = float(input('Digite o valor: '))
    n2 = float(input('Digite o valor: '))
    print('DIGITE [1] PARA SOMAR')
    print('DIGITE [2] PARA SUBTRAIR')
    print('DIGITE [3] PARA MULTIPLICAR')
    print('DIGITE [4] PARA DIVIDIR')
    print('DIGITE [5] PARA ELEVAR O PRIMEIRO AO SEGUNDO')
    op = input('Digite qual operação você deseja realizar: ')

    if op == '1':
        soma = n1 + n2
        print(f'{n1} + {n2} é igual a {soma:.2f}')
    elif op == '2':
        subtrair = n1 - n2
        print(f' {n1} - {n2} é igual a {subtrair:.2f}')
    elif op == '3':
        multiplicar = n1 * n2
        print(f'{n1} * {n2} é igual a {multiplicar:.2f}')
    elif op == '4':
        dividir = n1 / n2
        print(f'{n1} / {n2} é igual a {dividir:.2f}')
    elif op == '5':
        elevar = pow(n1,n2)
        print(f'{n1} elevado a {n2} é igual a {elevar:.2f}')
    else:
        print('Comando Inválido')
    novamente = input('Deseja realizar novamente? [S/N] ').upper()
    if novamente == 'N':
        print('Obrigada')
        break




