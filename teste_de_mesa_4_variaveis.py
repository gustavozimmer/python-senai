nota1 = float(input("Digite a primeiro nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
if media >= 9:
    resultado = "Excelente"
elif media >= 7:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"
print("Media", media)
print("Resultado", resultado)