import numpy as np

producao = np.random.randint(50, 201, size=(4, 3))
total_por_maquina = producao.sum(axis=1)
total_por_turno = producao.sum(axis=0)
maquina_destaque_idx = np.argmax(total_por_maquina)
print("=== Matriz de Produção (Peças) ===")
print(producao)
print("\n" + "="*30)
print(f"Total por Máquina: {total_por_maquina}")
print(f"Total por Turno:   {total_por_turno}")
print("-" * 30)
print(f"Máquina de Destaque: Índice {maquina_destaque_idx} "
      f"(Produção: {total_por_maquina[maquina_destaque_idx]} peças)")