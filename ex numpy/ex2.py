import numpy as np

matriz = np.random.randint(-10, 10, size=(3, 3))
print(f"Soma diagonal principal: {matriz.diagonal().sum()}")
print(f"Soma diagonal secundária: {np.fliplr(matriz).diagonal().sum()}")
print("MATRIZ ORIGINAL")
print(matriz)
matriz[matriz < 0] = 0
print("MATRIZ FORMATADA")
print(matriz)