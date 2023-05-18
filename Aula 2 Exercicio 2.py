km = float(input('Digite a quantidade de kilometros rodados: '))
dias = int(input('Digite a quantidade de dias em que o carro foi alugado: '))

print('A quantidade de dias em que o carro foi alugado é: {} e a quantidade de kilometros rodados é: {}'.format(dias, km))

precoTotal = dias * 60 + km * 0.15

print('O valor total do aluguel é: {}'.format(precoTotal))

