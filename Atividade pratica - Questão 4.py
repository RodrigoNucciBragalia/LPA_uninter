print('Bem-vindo ao Controle de Estoque da Bicicletaria do Rodrigo Nucci Bragalia')
RU = 4473087

def cadastrarPeca():
    # Função para cadastrar uma nova peça no estoque
    peca = {
        'nome': input('Insira o nome da peça a ser cadastrada: '),
        'fabricante': input('Insira o fabricante da peça: '),
        'valor': float(input('Insira o valor da peça: ')),
    }
    return peca


def consultarPeca(pecas):
    # Função para consultar peças no estoque
    while True:
        print('\n*** Consultar Peças ***')
        print('1. Visualizar todas as peças cadastradas')
        print('2. Pesquisar peças por código')
        print('3. Pesquisar peças por fabricante')
        print('4. Voltar')

        opcao = input('Escolha uma opção de acordo com o menu acima: ')

        if opcao == '1':
            consultarTodasPecas(pecas)
        elif opcao == '2':
            consultarPecasPorCodigo(pecas)
        elif opcao == '3':
            consultarPecasPorFabricante(pecas)
        elif opcao == '4':
            break
        else:
            print('Opção inválida! Por favor, escolha uma opção válida.')


def consultarTodasPecas(pecas):
    # Função para exibir todas as peças cadastradas no estoque
    print('\n*** Consultar Todas as Peças Cadastradas ***')
    if pecas:
        for i in range(len(pecas)):
            peca = pecas[i]
            print(f'Peça {i+1}:')
            print(f'Nome: {peca["nome"]}')
            print(f'Fabricante: {peca["fabricante"]}')
            print(f'Valor: R$ {peca["valor"]:.2f}')
            print('*' * 60)
    else:
        print('Não há peças cadastradas no estoque.')


def consultarPecasPorCodigo(pecas):
    # Função para pesquisar peças por código no estoque
    print('\n*** Consultar Peças por Código ***')
    codigo = input('\nDigite o código da peça desejada: ')
    for peca in pecas:
        if peca['codigo'] == codigo:
            print(f'Código: {peca["codigo"]}')
            print(f'Nome: {peca["nome"]}')
            print(f'Fabricante: {peca["fabricante"]}')
            print(f'Valor: R$ {peca["valor"]:.2f}')
            break
    else:
        print('Não existe peça cadastrada com esse código')


def consultarPecasPorFabricante(pecas):
    # Função para pesquisar peças por fabricante no estoque
    print('\n*** Consultar Peças Por Fabricante ***')
    fabricante = input('\nDigite o fabricante da peça: ')
    for peca in pecas:
        if peca['fabricante'] == fabricante:
            print(f'Código: {peca["codigo"]}')
            print(f'Nome: {peca["nome"]}')
            print(f'Fabricante: {peca["fabricante"]}')
            print(f'Valor: R$ {peca["valor"]:.2f}')
            print('*' * 60)


def removerPeca(pecas):
    # Função para remover uma peça do estoque
    codigo = input('Insira o código da peça que você deseja excluir: ')
    for i in range(len(pecas)):
        if pecas[i]['codigo'] == codigo:
            del pecas[i]
            print('Peça excluída com sucesso do estoque.')
            break
    else:
        print('Peça não localizada.')


pecas = []  # Lista para armazenar as peças do estoque
contador = 1  # Variável para controlar o código das peças

while True:
    print('\n--- Menu ---')
    print('1. Adicionar Peça ao Estoque')
    print('2. Consultar Peças no Estoque')
    print('3. Remover Peça do Estoque')
    print('4. Sair')

    opcao = input('Digite o número da opção desejada: ')

    if opcao == '1':
        print('\n--- Adicionar Peça ao Estoque ---')
        peca = cadastrarPeca()
        peca['codigo'] = str(contador)  # Atribui um código à peça
        pecas.append(peca)  # Adiciona a peça à lista de peças
        contador += 1  # Incrementa o contador de código
        print('Peça cadastrada com sucesso no estoque.')
    elif opcao == '2':
        consultarPeca(pecas)
    elif opcao == '3':
        print('\n--- Remover Peça do Estoque ---')
        removerPeca(pecas)
    elif opcao == '4':
        break
    else:
        print('Opção inválida! Por favor, escolha uma opção válida.')

print('Fim do programa.')
