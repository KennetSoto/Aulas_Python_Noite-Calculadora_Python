#calculadora em python

while True:
    print('-----------------------------Calculadora---------------------------')
    #usuario informa numeros
    x = input('Informe o primeiro número: ').replace(',','.')
    y = input('Informe o segundo número: ').replace(',','.')

    #converte para os numeros decimais
    x = float(x)
    y = float(y)

    print('\nInforme a operação matematica que deseja fazer: ')
    print('"+" para somar.')
    print('"-" para subtrair. ')
    print('"*" para multiplicar. ')
    print('"/" para dividir. ')
    print('"%" para encontrar o resto da divisão. ')

    op = input('\nOperação desejada: ')

    match op:
        case '+':
            print(f'A soma dos valores {x} e {y} é: {x + y}.')
        case '-':
            print(f'A subtração dos valores {x} e {y} é: {x - y}.')
        case '*':
            print(f'A multiplicação dos valores {x} e {y} é: {x * y}.')
        case '/':
            print(f'A divisão dos valores {x} e {y} é: {x / y}.')
        case '%':
            print(f'O resto da divisão entre {x} e {y} é: {x % y:.2f}.')
        case _:
            print('Operação invalida')
            continue

