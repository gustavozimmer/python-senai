# with open("meu_arquivo.txt", "w") as arquivo:
#     arquivo.write("Ola mundo\n")
#     arquivo.write("Aprendendo\n")

# with open("meu_arquivo.txt", "r") as arquivo:
#     print(arquivo.read())

# import csv

# with open("produtos.csv", "w", newline="") as f:
#     writer = csv.writer(f, delimiter=";")
#     writer.writerow(["Nome", "Preço"])
#     writer.writerow(["Livro 1", 20])
#     writer.writerow(["Livro 2", 21])
#     writer.writerow(["Livro 3", 22])
#     writer.writerow(["Livro 3", 23])
#     writer.writerow(["Livro 4", 24])
#     writer.writerow(["Livro 5", 25])
#     writer.writerow(["Livro 6", 26])

# with open("produtos.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# import json

# with open("dados.json", "w") as f:
#     json.dump({"nome":"João", "idade":25}, f)

# with open("dados.json", "r") as f:
#     data = json.load(f)
#     print(data)

# xml_str = """<?xml version="1.0" encoding="UTF-8"?>
# <config>
#     <versao>1.0</versao>
# </config>"""

# with open("config.xml", "w", encoding = "utf-8") as f:
#     f.write(xml_str)

try:
    with open("arquivo.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Arquivo não encontrado")