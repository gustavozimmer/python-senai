tamanho_medio = int(input("Diigte o tamanho dos arquivos em MB: "))
numero_arquivos = int(input("Digite a quantidade de arquivos: "))
tamanho_total = numero_arquivos * tamanho_medio / 1000

print(f"O espaço ocupado em GB: {tamanho_total:.2f}")