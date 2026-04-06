from random import choice
lista_palavras = ["jipe", "almofada", "pentagono", "oculos", "garrafa", "mouse", "monitor", "cadeira", "lousa", "ventilador"]
palavra = choice(lista_palavras)
lista_str = []
print("-----FORCA-----")
print("_" * len(palavra))
print()
erros = 0
lista_acertos = []
lista_erros = []
for c in range(len(palavra)):
    lista_str.append("_")
while erros < 6:
    while True:
        letra = str(input("Digite uma letra: ")).lower().strip()
        if (letra not in lista_acertos) and (letra not in lista_erros):
            break
        print("Digite uma letra ")
    for let in palavra:
        if letra in palavra:
            lista_acertos.append(letra)
            break
        else:
            lista_erros.append(letra)
            erros += 1
            break
    print()
    for c in range(len(palavra)):
        for l in range(len(lista_acertos)):
            if lista_acertos[l] == palavra[c]:
                lista_str[c] = lista_acertos[l]
    print(f"{"".join(lista_str)}")
    if "_" not in lista_str:
        break
    print()
    print(f"ERRADAS: {" ".join(lista_erros)}")
    print(f"Seus erros: {erros}")
if erros < 6:
    print("Você ganhou!")
    print(f"A palavra era {palavra}")
else:
    print("Você perdeu!")
    print(f"A palavra era {palavra}")