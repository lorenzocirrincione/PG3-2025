ancho1 = int(input("Ingresa el ancho de la figura: "))
alto1 = int(input("Ingresa el alto de la figura: "))
caracter1 = input("Ingresa el caracter de la figura: ")

def figura(ancho,alto,caracter):
    for i in range(alto):
        print(caracter*ancho)
    

figura(ancho1,alto1,caracter1)