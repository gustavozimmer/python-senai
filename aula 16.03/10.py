print("""1 - ABRIR ARQUIVO
2 - SALVAR ARQUIVO
3 - FECHAR ARQUIVOS
4 - COPIAR
5 - COLAR
6 - RECORTAR
7 - DESFAZER
8 - REFAZER
9 - IMPRIMIR
10 - SAIR DO PROGRAMA""")

n = int(input("Digite sua opção: "))
match n:
    case 1:
        print("ABRIR ARQUIVO...")
    case 2:
        print("SALVAR ARQUIVO...")
    case 3:
        print("FECHAR ARQUIVOS...")
    case 4:
        print("COPIAR...")
    case 5:
        print("COLAR...")
    case 6:
        print("RECORTAR...")
    case 7:
        print("DESFAZER...")
    case 8:
        print("REFAZER...")
    case 9:
        print("IMPRIMIR...")
    case 10:
        print("SAIR DO PROGRAMA...")
    case _:
        print("Invalido")