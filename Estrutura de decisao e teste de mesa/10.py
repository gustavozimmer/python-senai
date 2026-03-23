nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
menor_nota = min(nota1, nota2, nota3)

if nota1 == menor_nota:
    media = (nota2 + nota3) / 2
elif nota2 == menor_nota:
    media = (nota1 + nota3) / 2
else:
    media = (nota1 + nota2) / 2
print(f"A média é {media}")