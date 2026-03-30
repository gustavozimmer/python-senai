nome_arquivo = "C:/Users/39052943893/Documents/python-senai/aula 30.03/teste.txt"
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())