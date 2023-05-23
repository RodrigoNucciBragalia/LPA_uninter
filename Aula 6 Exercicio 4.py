

def total_cadastros(lista):
    quantidade_elementos = len(lista)
    print('Você cadastrou {} pessoas'.format(quantidade_elementos))

def med_idade(lista):
    idade_real = []
    for idade in lista:
        idade = 2023 - idade
        idade_real.append(idade)
    soma = sum(idade_real)
    media = soma / len(idade_real)
    print('a média de idade das pessoas cadastradas é {}'.format(media))
    return media

def mulheres_menos_trinta(lista):
    mulheres_menos_30 = []
    for i in range(len(pessoas['sexo'])):
        if pessoas['sexo'][i] == 'F' and (2023 - pessoas['nascimento'][i]) < 30:
            mulheres_menos_30.append(pessoas['nome'][i])

    print('Essas são as mulheres com menos de 30'.format(mulheres_menos_30))

def homens_idade_acima_media(lista, media):
    homens_velhos = []

    for i in range(len(pessoas['sexo'])):
        if pessoas['sexo'][i] == 'M' and (2023 - pessoas['nascimento'][i] > media):
            homens_velhos.append((pessoas['nome'][i]))

    print('Esses são os homens com idade acima da media'.format(homens_velhos))


#programa principal
pessoas = {'nome': [], 'nascimento': [], 'sexo': []}

x = 1

while x == 1:
    print('Cadastro de pessoas ')
    pessoas['nome'].append(input('Digite o nome: '))
    pessoas['nascimento'].append(int(input('Digite o nascimento: ')))
    pessoas['sexo'].append(input('Digite o Sexo da pessoas M - masculino e F - feminino: '))

    x = int(input('deseja cadastrar outra pessoa? 0 - Sair, 1 - Ficar'))

total_cadastros(pessoas['nome'])
media = med_idade(pessoas['nascimento'])
mulheres_menos_trinta(pessoas)
homens_idade_acima_media(pessoas, media)


