nota = float(input("Digite a nota do aluno: "))
nota_letra = ''
if nota > 10 or nota < 0:
    print("Nota inválida")
elif nota >= 9:
    nota_letra = 'A'
elif nota >= 7:
    nota_letra = 'B'
elif nota >= 5:
    nota_letra = 'C'
elif nota >= 3:
    nota_letra = 'D'
else:
    nota_letra = 'E'

print(nota, nota_letra)