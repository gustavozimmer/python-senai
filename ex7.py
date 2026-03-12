pecas = int(input("Digite quantas peças se~rao montadas por minuto: "))
tempo_operacao = int(input("Digite o tempo de operação em minutos: "))
total_pecas_produzidas = tempo_operacao * pecas
print(f"O total de peças produzidas são: {total_pecas_produzidas:.2f}")
