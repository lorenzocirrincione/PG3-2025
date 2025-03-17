lista1 = [int(input(f"Ingrese el valor {i+1}: ")) for i in range(5)]

def listaordenada(lista):
    lista.sort()
    return(print(lista))


listaordenada(lista1)