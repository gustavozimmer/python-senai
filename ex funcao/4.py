def calcular_troco(valor_compra, valor_pago):
    if valor_pago < valor_compra:
        print("Pagamento insuficiente")
        return 0
    troco = valor_pago - valor_compra
    return troco

valor_compra = float(input("Digite o valor compra: "))
valor_pago = float(input("Digite o valor pago: "))
print(f"O troco a receber é: {calcular_troco(valor_compra, valor_pago)}")
