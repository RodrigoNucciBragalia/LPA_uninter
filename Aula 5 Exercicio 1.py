
def fatorial(numero):
    """
    inicialmente a função vai receber um valor numerico e salvar esse valor na variavel
    fat. depois vai verificar se o valor recebido é 0. Se for 0 vai salvar o valor 0 na variavel fat
    se o valor for 1 vai salvar o valor 1 na variavel fat
    se não vai calcular o fatorial.
    :param numero:
    :return:
    """
    fat = numero
    if numero == 0:
        fat = 1
    elif numero == 1:
        fat = 1
    else:
        while (numero > 0):
            numero -= 1
            if numero > 0:
                fat = fat * numero
            else:
                break
    return fat

def validacao(num):
    """
    Verifica se os valores digitados são maiores que zero
    :param num:
    :return:
    """
    if(num < 0):
        print('{} não é um valor valido'.format(num))
    else:
       print('{}! = {}'.format(num, fatorial(num)))


print('Programa de fatorial')

numero = int(input('Digite um numero para calcular o fatorial'))

validacao(numero)
