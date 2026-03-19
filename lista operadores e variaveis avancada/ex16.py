consumo_servidor = float(input("Consumo do servidor (Watts): "))
qtd_servidores = int(input("Quantidade de servidores: "))
total = consumo_servidor * qtd_servidores
print(f"Consumo total: {total:.2f} Watts")