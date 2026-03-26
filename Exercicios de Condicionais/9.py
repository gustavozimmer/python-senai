hora_inicial = int(input("Digite a hora inicial: "))
minuto_inicial = int(input("Digite o minuto inicial: "))
hora_final = int(input("Digite a hora final: "))
minuto_final = int(input("Digite o minuto final: "))

inicio_em_minutos = (hora_inicial * 60) + minuto_inicial
final_em_minutos = (hora_final * 60) + minuto_final
if final_em_minutos <= inicio_em_minutos:
    duracao_total = (24 * 60 - inicio_em_minutos) + final_em_minutos
else:
    duracao_total = final_em_minutos - inicio_em_minutos

quantidade_de_horas = duracao_total // 60
quantidade_de_minutos = duracao_total % 60

if duracao_total > 1440:
    print("O jogo não pode durar mais de 24H")
else:
    print(f"Duração total: {quantidade_de_horas}H {quantidade_de_minutos}M")