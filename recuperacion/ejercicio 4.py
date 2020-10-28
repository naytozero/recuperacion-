def Operacion_aritmetica():
    str
    operacion=float(input("ingrese que operacion quiere hacer (1) suma, (2) resta, (3) multiplicacion, (4) division, (5) potencia:"))
    num1=float(input("ingresar el primer numero: "))
    num2=float(input("ingresar el segundo numero: "))

    if (operacion==1) :
        suma=num1+num2
        print("el reultado es", suma)
    
    if (operacion==2) :
        resta=num1-num2
        print("el reultado es", resta)
    
    if (operacion==3) :
        multiplicacion=num1*num2
        print("el reultado es", multiplicacion)
    
    if (operacion==4) :
        division=num1/num2
        print("el reultado es", division)
    
    if (operacion==5) :
        potencia=num1**num2
        print("el reultado es", potencia)
Operacion_aritmetica()