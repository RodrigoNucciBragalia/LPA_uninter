def calc_desc(quantidade, valor_unitario): #Função que verifica a quantidade de desconto e faz o calculo do desconto.
    if quantidade < 10:
        desconto_por_unidade = 0
    elif quantidade > 9 and quantidade < 100:
        desconto_por_unidade = 0.05
    elif quantidade > 99 and quantidade < 1000:
        desconto_por_unidade = 0.1
    else:
        desconto_por_unidade = 0.15

    valor_sem_desconto = quantidade * valor_unitario
    valor_desconto = valor_sem_desconto * desconto_por_unidade
    valor_com_desconto = valor_sem_desconto - valor_desconto

    return valor_sem_desconto, valor_com_desconto, desconto_por_unidade #retornos da função

#Programa Principal
print('Bem Vindo a Loja do Rodrigo Nucci Bragalia')

valor_unitario = float(input('Entre com o valor unitario do produto '))
quantidade = int(input('Entre com a quantidade do produto '))

valor_sem_desconto, valor_com_desconto, desconto_por_unidade = calc_desc(quantidade, valor_unitario) #recebe o valor sem desconto, com desconto e desconto por unidade calculado na função calc_desc

print('O valor total da sua compra sem desconto é R${:.2f}'.format(valor_sem_desconto)) #Exibe o valor total sem desconto
print('O valor total de sua compra com desconto é R${:.2f} total de desconto {}%'.format(valor_com_desconto, desconto_por_unidade*100)) #Exibe o total da compra com desconto e o total de desconto em %
