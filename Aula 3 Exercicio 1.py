lado1 = float(input('digite um lado de um triangulo'))
lado2 = float(input('digite um lado de um triangulo'))
lado3 = float(input('digite um lado de um triangulo'))

if lado1 == 0 or lado2 == 0 or lado3 == 0:
    print("Não é um triangulo")
elif lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
    print('Não é um triangulo')
elif lado1 == lado2 == lado3:
    print('Triangulo equilatero')
elif lado1 != lado2 != lado3 and lado1 != lado3:
    print('triangulo escaleno')
elif lado1 == lado2 and lado1 != lado3 or lado3 == lado2 and lado3 != lado1 or lado1 == lado3 and lado1 != lado2:
    print('triangulo isóceles')
else:
    ('Não é triangulo')
