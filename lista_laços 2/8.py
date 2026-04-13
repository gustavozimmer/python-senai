candidatos = [[1, 0], [2, 0], [3, 0], ["nulo", 0]]
qtde_votos = 0
nulo = False
while True:
    voto = int(input("Digite seu voto (1, 2, 3) ou 0 para sair: "))
    if voto == 0:
        break
    qtde_votos += 1
    for c in range (0, len(candidatos) - 2):
        if voto == candidatos[c][0]:
            candidatos[c][1] += 1
            nulo = False
            break
        nulo = True
    if nulo:
        candidatos[len(candidatos) - 1][0] += 1
for i in range(0, len(candidatos) - 1):
    print(f"{candidatos[i]}: {candidatos[i][1]} votos")
