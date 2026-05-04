import numpy as np

imagem_esteira = np.random.randint(0, 256, size=(8, 8))
regiao_central = imagem_esteira[2:6, 2:6]
media_intensidade = regiao_central.mean()
print("=== Imagem Completa da Esteira (8x8) ===")
print(imagem_esteira)
print("\n=== Região Central Recortada (4x4) ===")
print(regiao_central)
print(f"\nIntensidade Média Central: {media_intensidade:.2f}")
if media_intensidade > 120:
    print("Engrenagem centralizada e detectada")
else:
    print("Área vazia ou peça desalinhada")