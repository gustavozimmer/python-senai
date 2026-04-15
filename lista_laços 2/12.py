historico = []
saldo = 0
print("=== BEM-VINDO AO CAIXA ELETRÔNICO ===")
while True:
    print("\nOPÇÕES:")
    print("a. Depositar")
    print("b. Sacar")
    print("c. Ver saldo")
    print("d. Sair")
    
    opcao = input("Escolha uma opção: ").lower()

    if opcao == 'a':
        valor_deposito = float(input("Quanto deseja depositar? R$ "))
        if valor_deposito > 0:
            saldo = saldo + valor_deposito
            historico.append(f"Depósito: R$ {valor_deposito}")
            print("Depósito realizado com sucesso!")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    elif opcao == 'b':
        valor_saque = int(input("Quanto deseja sacar? R$ "))
        
        if valor_saque > saldo:
            print("Erro: Saldo insuficiente!")
        elif valor_saque % 2 != 0:
            print("Erro: Só permitimos saques de valores múltiplos de 2.")
        elif valor_saque <= 0:
            print("Erro: Valor inválido.")
        else:
            valor_restante = valor_saque
            n100 = valor_restante // 100
            valor_restante = valor_restante % 100
            
            n50 = valor_restante // 50
            valor_restante = valor_restante % 50
            
            n20 = valor_restante // 20
            valor_restante = valor_restante % 20
            
            n10 = valor_restante // 10
            valor_restante = valor_restante % 10
            
            n5 = valor_restante // 5
            valor_restante = valor_restante % 5
            
            n2 = valor_restante // 2
            valor_restante = valor_restante % 2

            if valor_restante != 0:
                print("Erro: Não há notas disponíveis para este valor exato.")
            else:
                saldo = saldo - valor_saque
                historico.append(f"Saque: R$ {valor_saque}")
                print(f"Saque realizado! Notas entregues:")
                if n100 > 0:
                    print(f"- {n100} nota(s) de R$ 100")
                if n50 > 0: print(f"- {n50} nota(s) de R$ 50")
                if n20 > 0: print(f"- {n20} nota(s) de R$ 20")
                if n10 > 0: print(f"- {n10} nota(s) de R$ 10")
                if n5 > 0: print(f"- {n5} nota(s) de R$ 5")
                if n2 > 0: print(f"- {n2} nota(s) de R$ 2")

    elif opcao == 'c':
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == 'd':
        print("\n--- RESUMO DA SESSÃO ---")
        print(f"Saldo final: R$ {saldo:.2f}")
        print("Histórico de operações:")
        for item in historico:
            print(f"- {item}")
        print("Obrigado por usar nosso caixa!")
        break
    else:
        print("Opção inválida! Tente novamente.")