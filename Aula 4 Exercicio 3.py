print('O valor do cinema é:')
print('Para crianças com menos de 3 anos. Ingresso é gratuito')
print('Para crianças de 3 até 12. R$ 15.00')
print('Para qualquer pessoa com mais de 12 anos. R$ 30.00')

valor = 0
pessoas = 0
m_idade = 0
repeticao = 0

while True:
    idade = int(input('Digite a sua idade '))
    repeticao += 1
    m_idade = idade / repeticao
    if idade < 3:
        valor += 0
        pessoas += 1
        print('O valor para esse ingresso é R$ 0.00')
        sair = input('Para encerrar digite SAIR, caso queira comprar outro ingresso digit N ')
        if sair == 'sair' or sair == 'SAIR':
            break
        else:
            continue
    if idade >= 3 and idade <= 12:
        valor += 15
        pessoas += 1
        print('O valor para esse ingresso é R$ 15.00')
        sair = input('Para encerrar digite SAIR, caso queira comprar outro ingresso digit N ')
        if sair == 'sair' or sair == 'SAIR':
            break
        else:
            continue
    if idade > 12:
        valor += 30
        pessoas += 1
        print('O valor para esse ingresso é R$ 30.00')
        sair = input('Para encerrar digite SAIR, caso queira comprar outro ingresso digit N ')
        if sair == 'sair' or sair == 'SAIR':
            break
        else:
            continue

print('O total da sua compra foi {}'.format(valor))
print('O número de ingressos comprados foi {}'.format(pessoas))
print('A média de idade das pessoas que vão assistir ao filme é {}'.format(m_idade))