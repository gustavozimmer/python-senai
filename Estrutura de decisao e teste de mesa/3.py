qtde_produto = int(input("Digite a quantidade de produto: "))
valor = valor_desconto = float(input("Digite o valor de cada unidade: "))
if qtde_produto > 100:
    valor_desconto -= valor * 0.1
else:
    valor_desconto -= valor * 0.05
    
desconto_unidade = valor - valor_desconto
total = valor_desconto * qtde_produto
print(f"Valor inicial: {valor}, Quantidade Solicitada {qtde_produto}, Desconto por unidade: {desconto_unidade}, Total a pagar: {total}")