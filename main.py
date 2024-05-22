while True:  # O loop infinito permite que a calculadora continue funcionando até que o usuário decida parar
    print('-----------------------------Calculadora---------------------------')
    
    # O usuário informa os números. A função replace é usada para permitir que o usuário insira números decimais usando vírgulas ou pontos
    x = input('Informe o primeiro número: ').replace(',','.')
    y = input('Informe o segundo número: ').replace(',','.')
    
    # Os números são convertidos para float para permitir operações matemáticas
    x = float(x)
    y = float(y)
    
    # O usuário é solicitado a escolher a operação matemática que deseja realizar
    print('\nInforme a operação matematica que deseja fazer: ')
    print('"+" para somar.')
    print('"-" para subtrair. ')
    print('"*" para multiplicar. ')
    print('"/" para dividir. ')
    print('"%" para encontrar o resto da divisão. ')
    op = input('\nOperação desejada: ')
    
    # Dependendo da operação escolhida pelo usuário, o programa realiza a operação correspondente
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
            print('Operação invalida')  # Se a operação inserida não for válida reinicia o programa
            continue
    
    
    # O usuário é perguntado se deseja continuar usando a calculadora, a função upper é para deixar maiusculo caso seja minusculo
    continuar = input('\nDeseja continuar (S/N)? ').upper()
    
    # Dependendo da resposta do usuário, o programa termina
    if continuar == 'S':
        continue
    elif continuar == 'N':
        print('Programa finalizado')
        break
    else:
        print('Opcão invalida')  # Se a resposta do usuário não for valida, o programa reinicia
        continue
