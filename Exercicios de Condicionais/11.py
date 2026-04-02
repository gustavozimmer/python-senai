retangulo1_superior_x = int(input("Digite a coordenada x do canto superior esquerdo do retangulo 1: "))
retangulo1_superior_y = int(input("Digite a coordenada y do canto superior esquerdo do retangulo 1: "))
retangulo1_inferior_x = int(input("Digite a coordenada x do canto inferior direito do retangulo 1: "))
retangulo1_inferior_y = int(input("Digite a coordenada y do canto inferior direito do retangulo 1: "))

retangulo2_superior_x = int(input("Digite a coordenada x do canto superior esquerdo do retangulo 2: "))
retangulo2_superior_y = int(input("Digite a coordenada y do canto superior esquerdo do retangulo 2: "))
retangulo2_inferior_x = int(input("Digite a coordenada x do canto inferior direito do retangulo 2: "))
retangulo2_inferior_y = int(input("Digite a coordenada y do canto inferior direito do retangulo 2: "))

if (retangulo1_inferior_x < retangulo2_superior_x or retangulo1_superior_x > retangulo2_inferior_x or  retangulo1_inferior_y > retangulo2_superior_y or retangulo1_superior_y < retangulo2_inferior_y):
    print("Não se sobrepõem")
else:
    print("Se sobrepõem")

    
