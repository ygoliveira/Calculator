
def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def radiciacao(x , y):
    return x ** y

def divisao(x, y):
    return x / y

print('\nSelecione a operação desejada: \n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Radiciação')
print('5 - Divisão')

escolhido = str(input('\nDigite sua opção (1/2/3/4/5): '))

numero1 = int(input('\nDigite o primeiro número: '))
numero2 = int(input('\nDigite o segundo número: '))

if escolhido == '1':
    print('\n')
    print(f'{numero1} + {numero2} = {soma(numero1, numero2)}')
    print('\n')

elif escolhido == '2':
    print('\n')
    print(f'{numero1} - {numero2} = {subtracao(numero1, numero2)}')
    print('\n')

elif escolhido == '3':
    print('\n')
    print(f'{numero1} * {numero2} = {multiplicacao(numero1, numero2)}')
    print('\n')

elif escolhido == '4':
    print('\n')
    print(f'{numero1} ^ {numero2} = {radiciacao(numero1, numero2)}')
    print('\n')

elif escolhido == '5':
    print('\n')
    print(f'{numero1} / {numero2} = {divisao(numero1, numero2)}')
    print('\n')
else:
    print('Opção Inválida!!')

