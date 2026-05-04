import numpy as np

dados_sensores = np.random.randint(1, 101, size=10)
x_min = dados_sensores.min()
x_max = dados_sensores.max()
dados_normalizados = (dados_sensores - x_min) / (x_max - x_min)
print(f"Dados Originais (Sensores): {dados_sensores}")
print(f"Dados Normalizados (0 a 1): {dados_normalizados}")
print(f"Valor Mínimo: {dados_normalizados.min()} | Valor Máximo: {dados_normalizados.max()}")