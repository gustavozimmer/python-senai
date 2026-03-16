memoria_ram = int(input("Digite a quatidade de memória RAM em GB de cada computador: "))
qtde_computadores = int(input("Digite a quantidade de computadores: "))
memoria_disponivel = memoria_ram * qtde_computadores
print(f"A quantidade total de memória disponível é {memoria_disponivel:.2f}")