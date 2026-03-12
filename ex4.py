velocidade_internet = int(input("Digite a valocidade da internet em Mbps: "))
tempo = int(input("Digite o tempo em segundos: "))
dados_transferidos = velocidade_internet * tempo
print(f"A quantidade de dados tranferidos é {dados_transferidos:.2f}Mb")
