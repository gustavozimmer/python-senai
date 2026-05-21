def contar_vogais(texto):
    return len(texto)

texto = str(input("Digite uma palavra: "))
print(f"A palavra {texto} possui {contar_vogais(texto)} letras")