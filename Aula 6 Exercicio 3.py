import random

jokenpo = ('sair', 'pedra', 'papel', 'tesoura')
indice_aleatorio_pc = 0
indice_jogador = 0

pontos_jogador = 0
pontos_pc = 0

vencedores = []

print('Digite 1 para: Pedra')
print('Digite 2 para: Papel')
print('Digite 3 para Tesoura')
print('Digite 0 para Sair')

while True:
    indice_jogador = int(input('Digite o número da sua jogada'))

    if indice_jogador == 0:
        break
    elif indice_jogador >= 4:
        print('Escolha inválida')
        continue

    mao_jogador = jokenpo[indice_jogador]
    indice_aleatorio_pc = random.randint(1, len(jokenpo) -1)
    mao_pc = jokenpo[indice_aleatorio_pc]

    print('você escolheu {}'. format(jokenpo[indice_jogador]))
    print('PC escolheu {}'. format(jokenpo[indice_aleatorio_pc]))

    if mao_jogador == 'pedra' and mao_pc == 'papel':
        print('Pc ganhou!')
        vencedores.append('Pc ganhou!')
        pontos_pc += 1
    elif mao_jogador == 'pedra' and mao_pc == 'pedra':
        print('Empatou!')
        vencedores.append('Empate')
    elif mao_jogador == 'pedra' and mao_pc == 'tesoura':
        print('Jogador venceu!')
        vencedores.append('Jogador venceu')
        pontos_jogador += 1
    elif mao_jogador == 'papel' and mao_pc == 'pedra':
        print('Jogador venceu!')
        vencedores.append('Jogador venceu')
        pontos_jogador += 1
    elif mao_jogador == 'papel' and mao_pc == 'papel':
        print('Empatou!')
        vencedores.append('Empate')
    elif mao_jogador == 'papel' and mao_pc == 'tesoura':
        print('Pc ganhou!')
        vencedores.append('Pc ganhou!')
        pontos_pc += 1
    elif mao_jogador == 'tesoura' and mao_pc == 'pedra':
        print('Pc ganhou!')
        vencedores.append('Pc ganhou!')
        pontos_pc += 1
    elif mao_jogador == 'tesoura' and mao_pc == 'papel':
        print('Jogador venceu!')
        vencedores.append('Jogador venceu')
        pontos_jogador += 1
    elif mao_jogador == 'tesoura' and mao_pc == 'tesoura':
        print('Empatou!')
        vencedores.append('Empate')

print('O jogador fez: {}'.format(pontos_jogador))
print('O Pc fez: {}'.format(pontos_pc))
print('A ordem de vencedores por rodada foi: \n {}'.format(vencedores))
