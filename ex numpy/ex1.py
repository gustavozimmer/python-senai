import numpy as np

temperaturas = np.random.uniform(20, 80.01, 30)
filtro = temperaturas[temperaturas > 75]
print(f"A maior temperatura: {temperaturas.max():.2f}| menor temperatura: {temperaturas.min():.2f} | média: {temperaturas.mean():.2f}")
print(f"Acima de 75: {len(filtro)}")
