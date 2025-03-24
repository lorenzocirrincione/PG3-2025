class familia:
    def __init__(self,padre,madre,hijos):
        self.padre = padre
        self.madre = madre
        self.hijos = hijos

    def __str__(self):
        hijos_str = ", ".join(self.hijos) if self.hijos else "No tienen hijos"
        return f"Padre: {self.padre}, Madre: {self.madre}, Hijos: {hijos_str}"

familia1 = familia("Gaston", "Julieta", ["lautaro","simon","lucas"])
print(familia1)
