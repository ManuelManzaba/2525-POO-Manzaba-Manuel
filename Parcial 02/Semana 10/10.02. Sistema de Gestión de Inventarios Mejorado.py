# Sistema de Inventario - Versión 2
# Archivo: almacen.txt
# Autor: [Tu Nombre]
# Fecha: [Fecha de entrega]
# Descripción: Sistema que administra productos de un inventario con manejo de archivos y errores.

import os

class Producto:
    def _init_(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad

    def _str_(self):
        return f"{self.codigo},{self.nombre},{self.cantidad}"

    @staticmethod
    def desde_linea(linea):
        try:
            codigo, nombre, cantidad = linea.strip().split(',')
            return Producto(codigo, nombre, int(cantidad))
        except ValueError:
            print("⚠ Error: línea inválida encontrada en el archivo.")
            return None

class Inventario:
    def _init_(self, archivo='almacen.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_archivo()

    def cargar_archivo(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    producto = Producto.desde_linea(linea)
                    if producto:
                        self.productos[producto.codigo] = producto
            print("✅ Inventario cargado desde el archivo correctamente.")
        except FileNotFoundError:
            print("📂 Archivo no encontrado. Se creará al guardar cambios.")
        except PermissionError:
            print("⛔ Permiso denegado para leer el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al cargar el archivo: {e}")

    def guardar_archivo(self):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for producto in self.productos.values():
                    f.write(str(producto) + '\n')
            print("💾 Inventario guardado correctamente en el archivo.")
        except PermissionError:
            print("⛔ No tienes permiso para escribir en el archivo.")
        except Exception as e:
            print(f"❌ Error al guardar el archivo: {e}")

    def agregar_producto(self, codigo, nombre, cantidad):
        if codigo in self.productos:
            print("⚠ Ya existe un producto con ese código.")
            return
        self.productos[codigo] = Producto(codigo, nombre, cantidad)
        self.guardar_archivo()
        print("✅ Producto agregado al inventario.")

    def actualizar_producto(self, codigo, cantidad):
        if codigo not in self.productos:
            print("❌ No se encontró el producto con ese código.")
            return
        self.productos[codigo].cantidad = cantidad
        self.guardar_archivo()
        print("✅ Cantidad actualizada correctamente.")

    def eliminar_producto(self, codigo):
        if codigo in self.productos:
            del self.productos[codigo]
            self.guardar_archivo()
            print("🗑 Producto eliminado del inventario.")
        else:
            print("❌ Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📭 Inventario vacío.")
        else:
            print("\n📦 Listado actual de productos:")
            for p in self.productos.values():
                print(f"➡ Código: {p.codigo} | Nombre: {p.nombre} | Cantidad: {p.cantidad}")

def menu():
    inventario = Inventario()

    while True:
        print("\n========= SISTEMA DE INVENTARIO =========")
        print("1. Ver productos")
        print("2. Agregar nuevo producto")
        print("3. Actualizar cantidad de un producto")
        print("4. Eliminar producto")
        print("5. Salir del sistema")
        print("=========================================")

        opcion = input("Elige una opción (1-5): ")

        if opcion == '1':
            inventario.mostrar_inventario()
        elif opcion == '2':
            codigo = input("Código del producto: ").strip()
            nombre = input("Nombre del producto: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                inventario.agregar_producto(codigo, nombre, cantidad)
            except ValueError:
                print("⚠ Error: La cantidad debe ser un número entero.")
        elif opcion == '3':
            codigo = input("Código del producto a actualizar: ").strip()
            try:
                cantidad = int(input("Nueva cantidad: "))
                inventario.actualizar_producto(codigo, cantidad)
            except ValueError:
                print("⚠ Error: La cantidad debe ser un número entero.")
        elif opcion == '4':
            codigo = input("Código del producto a eliminar: ").strip()
            inventario.eliminar_producto(codigo)
        elif opcion == '5':
            print("👋 ¡Gracias por usar el sistema!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

if _name_ == "_main_":
    menu()
