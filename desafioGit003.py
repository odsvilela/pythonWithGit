print('='*40)
print(f'{"PAR OU ÍMPAR":^40}')
print('='*40)

while True:
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        print(f'{n} é PAR!')
    else:
        print(f'{n} é ÍMPAR')
    novamente = input('Deseja realizar a operação novamente? [S/N] ').upper()
    if novamente == 'N':
        print('Até a próxima!')
        break