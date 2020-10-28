def vacuna_comtra_el_covid19():
    str
años=float(input("digite sub edad  " ))
genero=input("digite sub genero " )
if años<=0:
    print("edad incorrecta ¿error al digitar la edad")
else:
    if años>=70:
        print("se le aplicara la vacuna de tipo c sin inportar el genero")
    else:
        if años>=16:
            print("se le aplicara la vacuna de tipo B si es mujer")
            print("se le aplicara la vacuna de tipo A si es hombre")

        else:
            print("Se le aplicara la vacuna de tipo A sin importar el genero ")
print("el genero es " ,genero)
vacuna_comtra_el_covid19()