class persona:
    def __init__(self,nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print(f"El nombre es {self.nombre}")

nombre1= persona("Lorenzo")
nombre2= persona("Lautaro")

nombre1.mostrar_nombre()
nombre2.mostrar_nombre()