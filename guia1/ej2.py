año_ingresado= int(input("Ingrese un año numericamente:  "))

def calculadora(año):
    if (año%4 == 0 and año %100 !=0) or (año%400 == 0):
        return(print(f"tu año ingresado {año_ingresado} es bisiesto"))

    else:
        print("El año ingresado no es bisiesto...")

calculadora(año_ingresado)