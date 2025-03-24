class Operaciones:
    def __init__(self):
        
        self.valor1 = int(input("Ingrese el primer valor: "))
        self.valor2 = int(input("Ingrese el segundo valor: "))

        
        self.mostrar_suma()
        self.mostrar_resta()
        self.mostrar_multiplicacion()
        self.mostrar_division()

    def mostrar_suma(self):
        print(f"La suma de los valores es: {self.valor1 + self.valor2}")

    def mostrar_resta(self):
        print(f"La resta de los valores es: {self.valor1 - self.valor2}")

    def mostrar_multiplicacion(self):
        print(f"La multiplicación de los valores es: {self.valor1 * self.valor2}")

    def mostrar_division(self):
        
        if self.valor2 != 0:
            print(f"La división de los valores es: {self.valor1 / self.valor2:.2f}")
        else:
            print("Error: No se puede dividir por cero.")


operacion = Operaciones()
