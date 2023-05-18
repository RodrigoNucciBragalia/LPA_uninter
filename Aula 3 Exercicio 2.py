v1 = float(input('digite um lado de um valor'))
v2 = float(input('digite um lado de um valor'))

operacao = input('digite a operação que voce deseja realizar, + ou - ou * ou /')

if operacao == '+':
    print('A soma de {} e {} é: {}'.format(v1, v2, v1+v2))
elif operacao == '-':
    print('A subtração de {} e {} é: {}'.format(v1, v2, v1-v2))
elif operacao == '*':
    print('A multiplicação de {} e {} é: {}'.format(v1, v2, v1*v2))
elif operacao == '/':
    print('A divisão de {} e {} é: {}'.format(v1, v2, v1/v2))
else:
    print('Operação invalida')

print('Encerrando o programa')
