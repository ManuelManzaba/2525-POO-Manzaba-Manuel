import json
import os


class Producto:
    def _init_(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            id_producto=data['id_producto'],
            nombre=data['nombre'],
            cantidad=data['cantidad'],
            precio=data['precio']
        )

    def _str_(self):
        return f"[{self.id_producto}] {self.nombre} - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


class Inventario:
    def _init_(self):
        self.productos = {}  # Usamos un diccionario para búsquedas rápidas por ID

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("⚠ Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            print("✅ Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("✅ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
            print("✅ Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        if encontrados:
            for p in encontrados:
                print(p)
        else:
            print("🔍 No se encontró ningún producto con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("📭 Inventario vacío.")
        else:
            print("📋 Productos en inventario:")
            for p in self.productos.values():
                print(p)

    def guardar_en_archivo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)
        print("💾 Inventario guardado en archivo.")

    def cargar_desde_archivo(self, archivo):
        if not os.path.exists(archivo):
            print("📁 Archivo no encontrado. Se cargarán productos de ejemplo.")
            self.cargar_productos_de_ejemplo()
            return
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                for item in data:
                    producto = Producto.from_dict(item)
                    self.productos[producto.id_producto] = producto
            print("📂 Inventario cargado desde archivo.")
        except json.JSONDecodeError:
            print("❌ Error al leer el archivo. Está dañado o vacío.")

    def cargar_productos_de_ejemplo(self):
        ejemplo = [
            Producto("A100", "Silla de oficina", 20, 89.99),
            Producto("A101", "Escritorio de madera", 10, 159.50),
            Producto("A102", "Lámpara LED", 35, 22.75),
            Producto("A103", "Archivador metálico", 5, 120.00),
            Producto("A104", "Pizarra blanca", 12, 45.90),
        ]
        for producto in ejemplo:
            self.agregar_producto(producto)


def mostrar_menu():
    print("""
📦 MENÚ DE INVENTARIO
1. Agregar producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto por nombre
5. Mostrar todos los productos
6. Guardar inventario
7. Cargar inventario
8. Salir
""")


def main():
    inventario = Inventario()
    archivo = "inventario2.json"
    inventario.cargar_desde_archivo(archivo)

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                nuevo = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo)
            except ValueError:
                print("❌ Error: La cantidad y el precio deben ser números.")

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no modificar): ")
            precio = input("Nuevo precio (dejar vacío para no modificar): ")
            inventario.actualizar_producto(
                id_producto,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == '5':
            inventario.mostrar_todos()

        elif opcion == '6':
            inventario.guardar_en_archivo(archivo)

        elif opcion == '7':
            inventario.cargar_desde_archivo(archivo)

        elif opcion == '8':
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.")


if _name_ == "_main_":
    main()
