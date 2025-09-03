# ----------------------------------------
# Sistema de Gestión de Biblioteca Digital
# ----------------------------------------

# Clase Libro
class Libro:
    def _init_(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)  # Tupla inmutable: (autor, título)
        self.categoria = categoria
        self.isbn = isbn

    def _str_(self):
        autor, titulo = self.info
        return f"'{titulo}' por {autor} (ISBN: {self.isbn}, Categoría: {self.categoria})"


# Clase Usuario
class Usuario:
    def _init_(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de objetos Libro

    def _str_(self):
        return f"{self.nombre} (ID: {self.id_usuario})"


# Clase Biblioteca
class Biblioteca:
    def _init_(self):
        self.libros_disponibles = {}  # ISBN -> Libro
        self.usuarios = {}            # ID -> Usuario
        self.ids_usuarios = set()     # Para asegurar unicidad de IDs

    # Añadir libro
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print(f"El libro con ISBN {libro.isbn} ya existe.")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            libro = self.libros_disponibles.pop(isbn)
            print(f"Libro quitado: {libro}")
        else:
            print("Libro no encontrado en la biblioteca.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")
        else:
            print(f"ID de usuario '{usuario.id_usuario}' ya registrado.")

    # Dar de baja usuario
    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario dado de baja: {usuario}")
        else:
            print("Usuario no encontrado.")

    # Prestar libro
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros_disponibles:
            print("Libro no disponible.")
            return

        libro = self.libros_disponibles.pop(isbn)
        self.usuarios[id_usuario].libros_prestados.append(libro)
        print(f"Libro prestado: {libro} a {self.usuarios[id_usuario].nombre}")

    # Devolver libro
    def devolver_libro(self, id_usuario, isbn):
        usuario = self.usuarios.get(id_usuario)
        if not usuario:
            print("Usuario no registrado.")
            return

        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print(f"Libro devuelto: {libro}")
                return
        print("Libro no encontrado en préstamos del usuario.")

    # Buscar libros por título, autor o categoría
    def buscar_libros(self, *, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros_disponibles.values():
            autor_libro, titulo_libro = libro.info
            if (
                (titulo and titulo.lower() in titulo_libro.lower()) or
                (autor and autor.lower() in autor_libro.lower()) or
                (categoria and categoria.lower() == libro.categoria.lower())
            ):
                resultados.append(libro)

        if resultados:
            print("Resultados de la búsqueda:")
            for l in resultados:
                print(" -", l)
        else:
            print("No se encontraron libros que coincidan.")

    # Listar libros prestados a un usuario
    def listar_libros_prestados(self, id_usuario):
        usuario = self.usuarios.get(id_usuario)
        if not usuario:
            print("Usuario no registrado.")
            return

        if not usuario.libros_prestados:
            print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"Libros prestados a {usuario.nombre}:")
            for libro in usuario.libros_prestados:
                print(" -", libro)


# -----------------------------
# PRUEBA DEL SISTEMA
# -----------------------------
if _name_ == "_main_":
    # Crear instancia de Biblioteca
    biblio = Biblioteca()

    # Crear libros
    libro1 = Libro("1984", "George Orwell", "Ficción", "123456")
    libro2 = Libro("Python Básico", "Juan Pérez", "Educativo", "654321")
    libro3 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "111111")

    # Agregar libros
    biblio.agregar_libro(libro1)
    biblio.agregar_libro(libro2)
    biblio.agregar_libro(libro3)

    print("\n-----------------------------\n")

    # Crear usuarios
    usuario1 = Usuario("Ana", "U001")
    usuario2 = Usuario("Luis", "U002")

    # Registrar usuarios
    biblio.registrar_usuario(usuario1)
    biblio.registrar_usuario(usuario2)

    print("\n-----------------------------\n")

    # Prestar libros
    biblio.prestar_libro("U001", "123456")  # Ana presta "1984"
    biblio.prestar_libro("U002", "654321")  # Luis presta "Python Básico"

    print("\n-----------------------------\n")

    # Listar libros prestados
    biblio.listar_libros_prestados("U001")
    biblio.listar_libros_prestados("U002")

    print("\n-----------------------------\n")

    # Buscar libros
    biblio.buscar_libros(autor="Gabriel")  # Buscar por autor
    biblio.buscar_libros(categoria="Ficción")  # Buscar por categoría

    print("\n-----------------------------\n")

    # Devolver libro
    biblio.devolver_libro("U001", "123456")

    print("\n-----------------------------\n")

    # Dar de baja a un usuario
    biblio.dar_de_baja_usuario("U002")

    print("\n-----------------------------\n")

    # Quitar un libro
    biblio.quitar_libro("111111")

    print("\n--- Fin de la prueba ---")
