populacao_a = 1000
taxa_a = 0.03

populacao_b = 5000
taxa_b = 0.015

anos = 0

while populacao_a < populacao_b:
    populacao_a = populacao_a + (populacao_a * taxa_a)

    populacao_b = populacao_b + (populacao_b * taxa_b)

    anos = anos + 1

print("--- RESULTADO DA SIMULAÇÃO ---")
print(f"Levará {anos} anos para a Cidade A ultrapassar a Cidade B.")
print(f"População final da Cidade A: {int(populacao_a)} habitantes")
print(f"População final da Cidade B: {int(populacao_b)} habitantes")