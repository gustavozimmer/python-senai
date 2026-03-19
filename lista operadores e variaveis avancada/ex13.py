tamanho_log = float(input("Tamanho médio do log (MB): "))
quantidade_logs = int(input("Quantidade de logs por dia: "))
total = tamanho_log * quantidade_logs
print(f"Total de logs gerados: {total:.2f} MB")