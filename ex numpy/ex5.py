import numpy as np

drone_a = np.array([10.5, 20.0, 5.0])
drone_b = np.array([11.0, 21.5, 6.2])
distancia = np.linalg.norm(drone_a - drone_b)
print(f"Posição Drone A: {drone_a}")
print(f"Posição Drone B: {drone_b}")
print(f"Distância calculada: {distancia:.2f} metros")
if distancia < 2.5:
    print("\nALERTA DE COLISÃO! Proximidade perigosa detectada.")
else:
    print("\nOperação segura. Drones mantendo distância adequada.")