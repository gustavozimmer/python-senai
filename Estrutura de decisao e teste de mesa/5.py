idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))
idade3 = int(input("Digite a terceira idade: "))
if idade1 <= idade2 and idade1 <= idade3:
    print(f"A menor idade é {idade1}")
elif idade2 <= idade1 and idade2 <= idade3:
    print(f"A menor idade é {idade2}")
else:
    print(f"A  menor idade é {idade3}")


if idade1 >= idade2 and idade1 >= idade3:
    print(f"A maior idade é {idade1}")
elif idade2 >= idade1 and idade2 >= idade3:
    print(f"A maior idade é {idade2}")
else:
    print(f"A maior idade é {idade3}")
print(max(idade1, idade2, idade3))
