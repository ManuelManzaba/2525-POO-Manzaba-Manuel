# tienda.py

# Clase Producto representa un artículo de la tienda
class Producto:
    def _init_(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def _str_(self):
        return f"{self.nombre} - ${self.precio:.2f}"


# Clase Cliente representa a una persona que compra productos
class Cliente:
    def _init_(self, nombre):
        self.nombre = nombre
        self.carrito = []  # Lista de productos

    # Agregar producto al carrito
    def agregar_al_carrito(self, producto):
        self.carrito.append(producto)
        print(f"{producto.nombre} agregado al carrito.")

    # Mostrar los productos del carrito
    def mostrar_carrito(self):
        print(f"\nCarrito de {self.nombre}:")
        for p in self.carrito:
            print(f"- {p}")
        print(f"Total a pagar: ${self.total_compra():.2f}")

    # Calcular total
    def total_compra(self):
        return sum(p.precio for p in self.carrito)

    # Pagar
    def pagar(self):
        total = self.total_compra()
        print(f"\n{self.nombre} ha pagado ${total:.2f}. Gracias por su compra.")
        self.carrito.clear()


# Ejemplo de uso
if _name_ == "_main_":
    # Crear productos
    pan = Producto("Pan", 0.50)
    leche = Producto("Leche", 1.20)
    arroz = Producto("Arroz", 1.00)

    # Crear cliente
    cliente1 = Cliente("María")

    # Agregar productos al carrito
    cliente1.agregar_al_carrito(pan)
    cliente1.agregar_al_carrito(leche)
    cliente1.agregar_al_carrito(arroz)

    # Mostrar carrito y total
    cliente1.mostrar_carrito()

    # Pagar
    cliente1.pagar()
