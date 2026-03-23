idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Não eleitor")
elif idade >= 16 and idade < 18:
    print("Voto facultativo")
elif idade >= 70:
    print("Voto facultativo")
else:
    print("Voto obrigatório")