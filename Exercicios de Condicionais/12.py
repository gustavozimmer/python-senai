linha_atual = int(input("Digite a linha atual do cavalo: "))
coluna_atual = int(input("Digite a coluna atual do cavalo: "))
if (not 1 <= linha_atual <= 8):
    print('ERRO')
else:
    linha_destino = int(input("Digite a linha de destino: "))
    coluna_destino = int(input("Digite a coluna de destino: "))
    if (not 1 <= linha_atual <= 8):
        print('ERRO')
    else:
        resultado_linha = abs(linha_destino - linha_atual)
        resultado_coluna = abs(coluna_destino - coluna_atual)
        if (resultado_coluna == 2 and resultado_linha == 1) or (resultado_linha == 2 and resultado_coluna == 1):
            print("Movimento válido")
        else:
            print("Movimento inválido")