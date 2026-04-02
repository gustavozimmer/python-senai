# Entrada de dados
peso = float(input("Digite o peso da carga (kg): "))
print("Regiões disponíveis: Sudeste, Sul, Nordeste, Norte, Centro-Oeste")
regiao = input("Digite a região de destino: ")
is_premium = bool(input("O usuário é assinante Premium? (True/False): "))

valor_fixo = 0
valor_por_kg = 0

if regiao == "sudeste":
    valor_fixo = 10
    valor_por_kg = 2
elif regiao == "sul":
    valor_fixo = 15
    valor_por_kg = 3
elif regiao in ["nordeste", "norte"]:
    valor_fixo = 25
    valor_por_kg = 5
elif regiao == "centro-oeste":
    valor_fixo = 20
    valor_por_kg = 4
else:
    print("Região inválida!")
    exit()

valor_total = valor_fixo + (peso * valor_por_kg)

if peso > 20:
    valor_total += 30
    print("- Taxa de risco de R$ 30 aplicada (peso > 20kg).")

if is_premium:
    desconto = valor_total * 0.20
    valor_total -= desconto
    print(f"- Desconto Premium de 20% aplicado (- R$ {desconto:.2f}).")

print(f"Valor final do frete: R$ {valor_total:.2f}")
