preco = float(input('Digite o preço do produto: '))
p = float(input('Digite o percentual de desconto (0-100)%'))

desconto = preco * (p / 100)

final = preco - desconto
print('O preco do produto é {}. Desconto de {}%'.format(preco, p))
print('Valor calculado de desconto: {}. Valor final do produto: {}'.format(desconto, final))

