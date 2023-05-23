tupla = ('Python', 'OpenAI', 'Inteligência', 'Artificial', 'Aprendizado', 'Máquina', 'Linguagem', 'Programação', 'Dados', 'Algoritmo')

vogais = []  # Lista para armazenar as vogais encontradas

for palavra in tupla:
    for caractere in palavra:
        if caractere.lower() in 'aeiou':
            vogais.append(caractere)

print("Vogais encontradas na tupla:", vogais)
