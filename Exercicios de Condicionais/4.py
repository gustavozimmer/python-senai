salario_bruto = float(input("Digite seu slário bruto: "))
if (salario_bruto <= 2000.00):
    imposto = 0
elif (2000.01 <= salario_bruto <= 4000.0):
    imposto = (salario_bruto - 2000) * 0.1
elif (4000.01 <= salario_bruto <= 8000.0):
    imposto = ((salario_bruto - 4000) * 0.2) + 200
else:
    imposto = ((salario_bruto - 8000) * 0.3) + 1000

salario_liquido = salario_bruto - imposto

print(f"Salário bruto: {salario_bruto}, imposto total: {imposto:.2f}, salário líquido: {salario_liquido:.2f}")