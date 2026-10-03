col_dict = {
            "zoponcio" : "Tener malestar general",
            "cucayo" : "La parte quemeda del arroz",
            "veri veri" : "Mareo",
            }

palabra = input("Escribe la palabra que no entiendas: ").lower()

if palabra in col_dict.keys():
    print("El significado de la palabra es: ")
    print(col_dict[palabra])

else:
    print("La palabra no esta")
