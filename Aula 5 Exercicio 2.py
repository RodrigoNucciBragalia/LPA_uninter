def valida_int(pergunta, min, max):
    x = int(input(pergunta))
    while ((x < min) or (x > max)):
        x = int(input(pergunta))
    return x


def cria_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print('Arquivo {} foi criado com sucesso\n'.format(nomeArquivo))


def existe_arquivo(nomeArquivo):
    try:
        a = open(nomeArquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def cadastrar_jogo(nomeArquivo, nomejogo, nomeVideogame):
    try:
        a = open(nomeArquivo, 'at')
    except:
        print('Erro ao abrir o arquivo')
    else:
        a.write('{};{}\n'.format(nomejogo, nomeVideogame))
    finally:
        a.close()


def listar_arquivo(nomeArquivo):
    try:
        a = open(arquivo, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print(a.read())
    finally:
        a.close()


# Programa principal
arquivo = 'games.txt'
if existe_arquivo(arquivo):
    print('Arquivo localizado no computador')
else:
    print('Arquivo inexistente')
    cria_arquivo(arquivo)
while True:
    print('MENU')
    print('1 - Cadastrar novo item')
    print('2 - Listar tudo o que foi cadastrado')
    print('3 - sair')

    op = valida_int('Digite a opção desejada ', 1, 3)
    if op == 1:
        print('Opção de cadastrar novo item selecionada...\n')
        nomeJogo = input('Nome do jogo: ')
        nomeVideogame = input('Nome do video game: ')
        cadastrar_jogo(arquivo, nomeJogo, nomeVideogame)
    elif op == 2:
        print('Opção de listar itens cadastrados selecionada...\n')
        listar_arquivo(arquivo)
    elif op == 3:
        print('Encerrando o programa...\n')
        break
