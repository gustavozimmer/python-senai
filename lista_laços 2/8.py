candidatos = [[1, 0, 0], [2, 0, 0], [3, 0, 0], ["nulo", 0, 0]]
qtde_votos = 0
nulo = False
while True:
    voto = int(input("Digite seu voto (1, 2, 3) ou 0 para sair: "))
    if voto == 0:
        break
    qtde_votos += 1
    for c in range (0, len(candidatos)):
        if voto == candidatos[c][0]:
            candidatos[c][1] += 1
            nulo = False
            break
        nulo = True
    if nulo:
        candidatos[len(candidatos) - 1][1] += 1
if qtde_votos == 0:
    print("Nehum voto contabilizado")
else:       
    for p in range(len(candidatos)):
        candidatos[p][2] = candidatos[p][1] * 100 / qtde_votos

    for i in range(0, len(candidatos)):
        print(f"{candidatos[i][0]}: {candidatos[i][1]} votos {candidatos[i][2]:.2f}%")
    
    maior = candidatos[0][2]
    
    nome_maior = candidatos[0][0]
    for m in range(len(candidatos) - 1):
        
        if maior < candidatos[m][2]:
            maior = candidatos[m][2]
            nome_maior = candidatos[m][0]
    print(f"Ganhador: {nome_maior}")
    