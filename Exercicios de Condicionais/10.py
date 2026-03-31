import re
senha = str(input("Digite sua senha: "))
regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).+$'
if len(senha) < 8:
    print("Inválida")
elif re.match(regex, senha):
    print("Forte")
elif senha.isdigit() or senha.isalpha():
    print("Fraca")
elif (not senha.isalnum()):
    print("Média")
