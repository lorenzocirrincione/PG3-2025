class Triangulo:
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2 
        self.lado3 = lado3

    def lado_mayor(self):
        if self.lado1>self.lado2 > self.lado3:
            print(f"El lado mayor es {self.lado1}")
        elif self.lado2> self.lado1 > self.lado3:
            print(f"El lado mayor es {self.lado2}")
        elif self.lado3> self.lado2 > self.lado1:
            print(f"El lado mayor es {self.lado3}")
        elif self.lado1 == self.lado2 == self.lado3:
            print("Todos los lados son iguales")

    def mostrar_equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("El triangulo es equilatero ")

        else:
            print("El triangulo no es equilatero ")

primerlado = 5
segundolado = 4
tercerlado = 2

lados= Triangulo(primerlado,segundolado,tercerlado)
lados.lado_mayor()
lados.mostrar_equilatero()

primerlado1 = 3
segundolado1 = 3
tercerlado1 = 3

lados1= Triangulo(primerlado1,segundolado1,tercerlado1)
lados1.lado_mayor()
lados1.mostrar_equilatero()


        
