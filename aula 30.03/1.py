# cores = ["vermelho", "verde", "azul", "amarelo"]
# for cor in cores:
#     print("cor:", cor)
# print(cores[3])


# for c in range(0, 11, 2):
#     print(c)

# mensagem = 'Helo world!'
# for char in mensagem:
#     print(char)

# pessoa = {
#     "nome": "Ana",
#     "idade": 30,
#     "profissão": "engenheira"
# }

# print(pessoa["nome"])
# for chave, valor in pessoa.items():
#     print(f'{chave}: {valor}')

# animais = {'gato', 'cachorro', 'elefante', 'girafa'}
# for animal in animais:
#     print("Animal:", animal)

nome_arquivo = "LOPAL-Aula7-EstRepet-Arquivo.txt"
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())