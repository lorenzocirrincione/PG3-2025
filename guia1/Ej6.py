frase1 = input("Ingrese una frase: ")


def ordenar(palabra):
    vocales = "aeiou"
    return sorted(set(letra.lower() for letra in palabra if letra in vocales))


print(ordenar(frase1))
