print(2 + 2 < 4)

print(7 // 3 == 1 + 1)

print(3**2 + 4**2 == 25)

print(2 + 4 + 6 > 12)

print(1387 % 3 == 0)

print(31 % 2 == 0)

valores = [34, 29, 31]

menor_valor = min(valores)

print(menor_valor < 30)

idade = int(input('digite a idade'))
if idade > 60:
    print('você tem direito aos beneficios')



dano = int(input('Digite o valor do dano'))
escudo = int(input('Digite o valor do escudo'))
if dano > 10 and escudo == 0:
    print('Você está morto')

ano = int(input('Digite o ano'))
if ano % 4 == 0:
    print('pode ser um ano bissexto')
else:
    print('claramente não é um ano bissexto')

cima = True
baixo = True

if cima == True and baixo == True:
    print("Decida-se")
else:
    print("Escolha um caminho")






