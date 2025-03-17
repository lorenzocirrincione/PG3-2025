palabra1= input("Ingrese la palabra: ")

def polindroma(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

print(polindroma(palabra1))