while True:
    print('Escolha qual operação você deseja realizar.')
    print('Para Adição digite +.')
    print('Para Subtração digite -.')
    print('Para Divisão digite /.')
    print('Para Multiplicação digite *.')
    print('Para SAIR digite S')

    operador = input("Digite a operação")
    if(operador == 's' or operador == 'S'):
        print('Você escolheu sair')
        break
    valor1 = float(input('Digite o primeiro valor para realizar sua operação'))
    valor2 = float(input('Digite o segundo valor para realizar a operação'))

    if(operador == '+'):
        res = valor1 + valor2
        print('{} + {} = {}'.format(valor1, valor2, res))
    elif(operador == '-'):
        res = valor1 - valor2
        print('{} - {} = {}'.format(valor1, valor2, res))
    elif(operador == '*'):
        res = valor1 * valor2
        print('{} x {} = {}'.format(valor1, valor2, res))
    elif(operador == '/'):
        res = valor1 / valor2
        print('{} / {} = {}'.format(valor1, valor2, res))
    else:
        print('Operação invalida')
        continue

