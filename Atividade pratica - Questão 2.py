#Gera o cardapio de acordo com o que possuí no dicionário cardápio que fica
#no programa principal
def gerar_cardapio():
    largura_codigo = 10
    largura_nome = 22
    largura_valor = 10

    largura_total = largura_codigo + largura_nome + largura_valor
    meia_largura = largura_total/2

    print('*' * int(meia_largura) + 'Cardápio' + '*' * int(meia_largura))
    #utilizei o prefixo f para ajudar a gerar o cabeçalho da interface. (formatted string)
    print(f'|{"Código":<{largura_codigo}}| {"Descrição":<{largura_nome}}| {"Valor":<{largura_valor}}|')

    #Esse for vai ler o dicionário cardapio e gerar a interface para nós com a
    #largura dos campos fixada
    for codigo, dados in cardapio.items():
        nome = str(dados['nome'])
        valor = str(dados['valor'])
        print(f'|{codigo:<{largura_codigo}}| {nome:<{largura_nome}}| {valor:<{largura_valor}}|')

#função utilizada para escolher os produtos
def escolher_produto():
    produtos_escolhidos = {'nome': [], 'valor': []}

    #vai ficar dentro do while até o usuário escolher sair
    while True:
        cod_prod = int(input('Qual o produto desejado? '))

        # Se o num escolhido não estiver no cardápio volta a mensagem do print e pede novamente o produto
        if (cod_prod < 100 or cod_prod > 201) or (cod_prod > 105 and cod_prod < 200):
            print('Opção inválida')
            continue
        #Se o numero estiver no cardápio ele vai percorrer o cardápio e comparar os códigos com o
        #código digitado pelo usuário, quando o código dor encontrado no cardápio
        #o produto escolhido será salvo no dicionário produtos_escolhidos
        else:
            for codigo, dados in cardapio.items():
                if cod_prod == codigo:
                    produtos_escolhidos['nome'].append(dados['nome'])
                    produtos_escolhidos['valor'].append(dados['valor'])
                else:
                    continue
        #Se a função verifica_saida retornar n ou N a função é finalizada e retorna o dicionário
        #produtos escolhidos
        if verifica_saida() == 'n' or verifica_saida() == 'N':
            break
        else:
            continue

    return produtos_escolhidos

#função criada para evitar que o usuário digite algo diferente de N ou S e o programa continue
def verifica_saida():
    x = 's'
    while x == 's' or x == 'S' or x == 'n' or x == 'N':
        x = input('Deseja escolher mais um produto? S/N')
        if x == 'n' or x == 'N':
            return x
            break
        elif x == 's' or x == 'S':
            return x
            break
        else:
            print('Opção inválida Digite S para continuar ou N para sair')
            continue

#vai exibir todos os produtos selecionados e o valor final do produto
def exibe_valor_final():
    print('Os produtos escolhidos são:')
    valor_total = 0

    #Esse for vai percorrer prod_escolhidos e vai salvar todos os nomes e valores
    #nas variaveis nome e valores para que seja exibido os produtos com valores separados
    for i in range(len(prod_escolhidos['nome'])):
        nome = prod_escolhidos['nome'][i]
        valor = prod_escolhidos['valor'][i]
        print('{} - {}'.format(nome, valor))
        #após exibir os produtos o valor_final será incrementada com um dos produtos escolhidos de acordo com o indice
        valor_total = valor_total + valor
    #Por fim o valor total da compra é exibido para o usuário
    print('O valor total da compra deu {}'.format(valor_total))


#Programa principal
print('Lanchonete do Rodrigo Nucci Bragalia')

#dicionário com as informações do produto
cardapio = {100: {'nome': 'Cachorro Quente', 'valor': 9.00},
            101: {'nome': 'Cachorro Quente Duplo', 'valor': 11.00},
            102: {'nome': 'X-Egg', 'valor': 12.00},
            103: {'nome': 'X-Salada', 'valor': 13.00},
            104: {'nome': 'X-Bacon', 'valor': 14.00},
            105: {'nome': 'X-Tudo', 'valor': 17.00},
            200: {'nome': 'Refrigerante Lata', 'valor': 5.00},
            201: {'nome': 'Chá Gelado', 'valor': 4.00},
            }

#Função feita para gerar o cardápio
gerar_cardapio()

#vai receber o retorno da função escolher produtos
prod_escolhidos = escolher_produto()

#exibe todos os produtos selecionados e o valor final da compra
exibe_valor_final()




