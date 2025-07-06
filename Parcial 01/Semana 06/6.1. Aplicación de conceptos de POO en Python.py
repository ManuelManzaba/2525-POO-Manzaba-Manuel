# zoologico.py

# Clase base
class Animal:
    """
    Clase base que representa un animal genérico.
    """

    def _init_(self, nombre, edad):
        self._nombre = nombre        # Encapsulación
        self._edad = edad

    def hacer_sonido(self):
        """
        Método genérico que será sobrescrito por las clases hijas (polimorfismo).
        """
        return "Este animal hace un sonido."

    def describir(self):
        """
        Método que describe al animal.
        """
        return f"Nombre: {self._nombre}, Edad: {self._edad} años"


# Clase derivada: León
class Leon(Animal):
    """
    Clase derivada que representa un león.
    """

    def _init_(self, nombre, edad, fuerza):
        super()._init_(nombre, edad)
        self._fuerza = fuerza

    def hacer_sonido(self):
        return "¡Rugidooo!"  # Polimorfismo

    def describir(self):
        return f"{super().describir()}, Fuerza: {self._fuerza}"


# Clase derivada: Elefante
class Elefante(Animal):
    """
    Clase derivada que representa un elefante.
    """

    def _init_(self, nombre, edad, peso):
        super()._init_(nombre, edad)
        self._peso = peso

    def hacer_sonido(self):
        return "¡Pruuuuu!"  # Polimorfismo

    def describir(self):
        return f"{super().describir()}, Peso: {self._peso} kg"


# Clase derivada: Loro
class Loro(Animal):
    """
    Clase derivada que representa un loro.
    """

    def _init_(self, nombre, edad, vocabulario):
        super()._init_(nombre, edad)
        self._vocabulario = vocabulario

    def hacer_sonido(self):
        return f"¡{self._vocabulario}!"  # Polimorfismo

    def describir(self):
        return f"{super().describir()}, Vocabulario: '{self._vocabulario}'"


# Función principal
def main():
    # Crear instancias de animales
    simba = Leon("Simba", 7, "Alta")
    dumbo = Elefante("Dumbo", 10, 1200)
    polly = Loro("Polly", 2, "¡Hola amigo!")

    # Mostrar descripciones
    print("=== Descripciones de Animales ===")
    print(simba.describir())
    print(dumbo.describir())
    print(polly.describir())

    # Sonidos (polimorfismo)
    print("\n=== Sonidos de Animales (Polimorfismo) ===")
    animales = [simba, dumbo, polly]
    for animal in animales:
        print(f"{animal._class.name_} dice: {animal.hacer_sonido()}")


# Ejecutar programa
if _name_ == "_main_":
    main()
