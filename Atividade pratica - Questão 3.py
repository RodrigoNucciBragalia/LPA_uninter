print('Bem Vindo a companhia de Logistica Rodrigo Nucci Bragalia')
RU = 4473087

def dimensoesObjeto():
    while True:
        try:
            # Solicita as dimensões do objeto
            altura = float(input('Digite a altura do Objeto em cm '))
            comprimento = float(input('Digite o comprimento do Objeto em cm '))
            largura = float(input('Digite a largura do objeto em cm '))

            volume = altura * comprimento * largura  # Calcula o volume do objeto

            # Define o valor com base no volume
            if volume < 1000:
                valor = 10
            elif 1000 <= volume < 10000:
                valor = 20
            elif 10000 <= volume < 30000:
                valor = 30
            elif 30000 <= volume < 100000:
                valor = 50
            else:
                # Se o volume for muito alto, imprime uma mensagem de erro e retorna ao início do loop
                print('O volume desse objeto é muito alto para o nosso transporte')
                print('Entre novamente com as dimensões')
                continue

            # Imprime o volume e o preço para o objeto
            print('O volume desse objeto é {:.2f} cm³'.format(volume))
            print('O preço para esse objeto é R${:.2f}'.format((valor)))
            return valor
        except ValueError:
            # Se um valor inválido for digitado, imprime uma mensagem de erro e retorna ao início do loop
            print('Digite um valor valido para as dimensões do objeto')

def pesoObjeto():
    multiplicador = 0
    while True:
        try:
            # Solicita o peso do objeto
            peso = float(input('Digite o peso do objeto em Kg '))

            # Define o multiplicador com base no peso
            if peso <= 0.1:
                multiplicador = 1
            elif 0.1 <= peso < 1:
                multiplicador = 1.5
            elif 1 <= peso < 10:
                multiplicador = 2
            elif 10 <= peso < 30:
                multiplicador = 3
            else:
                # Se o peso for muito alto, imprime uma mensagem de erro e retorna ao início do loop
                print('Objeto muito pesado')
                print('Entre novamente com o peso do objeto')
                continue
            break
        except ValueError:
            # Se um valor inválido for digitado, imprime uma mensagem de erro e retorna ao início do loop
            print('Valor inválido, tente novamente')

    # Imprime o peso e o multiplicador para o objeto
    print('O peso do seu objeto é {:.2f}Kg'.format(peso))
    print('O multiplicador para esse peso é {}'.format(multiplicador))
    return multiplicador

def rotaObjeto():
    multiplicador = 0
    desenhar_rotas()
    while True:
        # Solicita a sigla da rota desejada
        rota = input('Insira a sigla da rota desejada ').upper()

        # Define o multiplicador com base na rota
        if rota == 'RS' or rota == 'SR':
            multiplicador = 1
        elif rota == 'BS' or rota == 'SB':
            multiplicador = 1.2
        elif rota == 'BR' or rota == 'RB':
            multiplicador = 1.5
        else:
            # Se uma sigla inválida for digitada, imprime uma mensagem de erro e retorna ao início do loop
            print('Insira uma sigla valida')
            continue
        break

    # Imprime a rota selecionada e o multiplicador
    print('A rota selecionada foi {} com multiplicador {}'.format(rota, multiplicador))
    return multiplicador

def desenhar_rotas():
    largura_sigla = 10
    largura_descricao = 32
    largura_multiplocador = 14
    largura_total = largura_multiplocador + largura_descricao + largura_sigla

    # Imprime o cabeçalho das rotas
    meia_largura = largura_total/2
    print('*' * int(meia_largura) + 'Rotas' + '*' * int(meia_largura))
    print(f'|{"sigla":<{largura_sigla}}|{"Rota":<{largura_descricao}}|{"Multiplicador":<{largura_multiplocador}}|')

    # Imprime as informações de cada rota
    for sigla, (descricao, multiplicador) in rotas.items():
        print(f'|{sigla:<{largura_sigla}}|{descricao:<{largura_descricao}}|{multiplicador:<{largura_multiplocador}}|')

    print('*' * (largura_total + 5))

# Programa Principal

# Dicionário das rotas com suas descrições e multiplicadores
rotas = {'RS': ['De Rio de Janeiro até São Paulo', 1],
         'SR': ['De São Paulo até Rio de Janeiro', 1],
         'BS': ['De Brasília até São Paulo', 1.2],
         'SB': ['De São Paulo até Brasília', 1.2],
         'BR': ['De Brasília até Rio de Janeiro', 1.5],
         'RB': ['Rio de Janeiro até Brasília',1.5],
         }

print('_' * 60)

# Solicita e calcula as dimensões do objeto
dimensoes = dimensoesObjeto()
print('_' * 60)

# Solicita e calcula o peso do objeto
peso = pesoObjeto()
print('_' * 60)

# Solicita e define a rota do objeto
rota = rotaObjeto()
print('_' * 60)

# Calcula o valor final com base nas dimensões, peso e rota
valor_final = dimensoes * peso * rota

# Imprime o valor final a ser pago, juntamente com as informações do objeto
print('O total a pagar é: R${} (Volume: {}cm³ * Multiplicador do Peso: {} * Multiplicador da Rota: {})'.format(valor_final, dimensoes, peso, rota))
