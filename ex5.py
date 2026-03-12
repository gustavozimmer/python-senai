preco = float(input("Digite o preço da licença "))
qtde_devs = int(input("Digite a quantidade de desenvolvedores: "))
custo_total = preco * qtde_devs

print(f"O custo total é: R${custo_total:.2f}")