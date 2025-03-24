class Persona:
    def __init__(self):
        self.nombre = input("Ingrese un nombre: ")
        self.edad = int(input("Ingrese la edad: "))

    def mostrar_datos(self):
        print(f"El nombre es {self.nombre} y la edad es {self.edad}...")

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = int(input("Ingrese el sueldo: "))

    def mostrar_datos(self):
        super().mostrar_datos()
        if self.sueldo > 3000:
            print(f"Su sueldo es de {self.sueldo}, deberá pagar impuestos...")
        else:
            print(f"Su sueldo es de {self.sueldo}, no deberá pagar impuestos...")


datosempleado = Empleado()
datosempleado.mostrar_datos()