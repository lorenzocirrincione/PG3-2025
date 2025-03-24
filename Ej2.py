class alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_nombre(self):
        print(f"El nombre del alumno es {self.nombre}")

    def mostrar_nota(self):
        if self.nota>5:
            print("El alumno es regular ")

        else:
            print("El alumno no es regular ")

nombre1 = alumno("Lorenzo",7)
nombre1.mostrar_nombre()
nombre1.mostrar_nota()

nombre1 = alumno("Lautaro",3)
nombre1.mostrar_nombre()
nombre1.mostrar_nota()