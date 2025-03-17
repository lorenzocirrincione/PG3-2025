lista1= [2,4,6,8,10]
valor=int(input("Ingrese el valor buscado: "))
def elementobuscado(lista, elemento):
    if valor in lista:
        a= lista.index(valor)
        print(f"El numero {valor} se encuentra en la posicion {a}")

    else:
        print("El valor no se encuentra en la lista")

elementobuscado(lista1,valor)