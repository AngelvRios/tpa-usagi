class adopcion:

    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

class TiendaMascotas:
    def __init__(self):
        self.perros_rescatados = []
        self.gatos_rescatados = []

    def adoptar_perro(self, nombre, edad, raza):
        perro = adopcion(nombre, edad, raza)
        self.perros_rescatados.append(perro)

    def adoptar_gato(self, nombre, edad, raza):
        gato = adopcion(nombre, edad, raza)
        self.gatos_rescatados.append(gato)

    def mostrar_perros_disponibles(self):
        print("Perros disponibles para adopción:")
        for perro in self.perros_rescatados:
            print(f"Nombre: {perro.nombre}, Edad: {perro.edad}, Raza: {perro.raza}")

    def mostrar_gatos_disponibles(self):
        print("Gatos disponibles para adopción:")
        for gato in self.gatos_rescatados:
            print(f"Nombre: {gato.nombre}, Edad: {gato.edad}, Raza: {gato.raza}")

# Ejemplo de uso
tienda = TiendaMascotas()

# Agregar algunos perros y gatos rescatados
tienda.adoptar_perro("corxea", 3, "Labrador Retriever")
tienda.adoptar_perro("perejil", 2, "desconocido")
tienda.adoptar_gato("wisin", 1, "negro")
tienda.adoptar_gato("yandel", 4, "naranjo")

# Mostrar los perros y gatos disponibles para adopción
tienda.mostrar_perros_disponibles()
print()
tienda.mostrar_gatos_disponibles()
