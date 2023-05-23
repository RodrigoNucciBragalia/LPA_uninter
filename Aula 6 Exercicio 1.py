
notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print(notas.count(7))

notas[-1] = 4
print(notas)

maior_valor = max(notas)

print('O maior valor da lista notas é {}'.format(maior_valor))

lista_ordenada = sorted(notas)

print('Essa é a lista de notas ordenada{}'.format(lista_ordenada))

soma_lista = sum(notas)
media_lista = soma_lista / len(notas)

print('A média de notas da lista é {}'.format(media_lista))