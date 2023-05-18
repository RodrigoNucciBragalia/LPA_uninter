kwh = float(input('Digite a quantidade de kWh consumido'))
instalacao = input('Qual o tipo de instalação,  Digite R para residência, I para Industria e C para comércio')

if instalacao == 'r':
    if kwh <= 500:
        res = kwh*0.40
        print('O preço do seu kWh é 0.40 e o total da sua conta é {}'.format(res))
    else:
        res = kwh*0.65
        print('O preço do seu kWh é 0.65 e o total da sua conta é {}'.format(res))
elif instalacao == 'c':
    if kwh <= 1000:
        res = kwh*0.55
        print('O preço do seu kWh é 0.55 e o total da sua conta é {}'.format(res))
    else:
        res = kwh*0.60
        print('O preço do seu kWh é 0.60 e o total da sua conta é {}'.format(res))
elif instalacao == 'i':
    if kwh <= 5000:
        res = kwh*0.55
        print('O preço do seu kWh é 0.55 e o total da sua conta é {}'.format(res))
    else:
        res = kwh*0.60
        print('O preço do seu kWh é 0.60 e o total da sua conta é {}'.format(res))
else:
    print('Valor invalido, digite I para industrial, C para comercial ou R para residencial')


