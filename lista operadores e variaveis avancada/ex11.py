tempo_tarefas = float(input("Digite o tempo da tarefa em segundos: "))
qtde_executada = int(input("Digite a quantidade de tarefas executadas: "))
min_total = (tempo_tarefas * qtde_executada) / 60
print(f"O tempo total em minutos é: {min_total:.2f}")