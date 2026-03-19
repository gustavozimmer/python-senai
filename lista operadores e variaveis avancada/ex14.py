paginas_por_minuto = int(input("Páginas por minuto: "))
tempo_impressao = float(input("Tempo de impressão (min): "))
total = paginas_por_minuto * tempo_impressao
print(f"Total de páginas impressas: {total:.2f}")