# programa_completo.py

# =========================
# Clases del sistema
# =========================

class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        """Inicializa la cuenta con un titular y saldo inicial."""
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"✅ Cuenta creada para {self.titular} con saldo de ${self.saldo:.2f}")

    def depositar(self, monto):
        """Deposita dinero en la cuenta."""
        if monto > 0:
            self.saldo += monto
            print(f"💰 Depósito de ${monto:.2f} realizado. Saldo actual: ${self.saldo:.2f}")
        else:
            print("❌ Monto no válido para depósito.")

    def retirar(self, monto):
        """Retira dinero si hay suficiente saldo."""
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"🏧 Retiro de ${monto:.2f} realizado. Saldo restante: ${self.saldo:.2f}")
        else:
            print("❌ Fondos insuficientes o monto inválido.")

    def consultar_saldo(self):
        """Consulta el saldo actual de la cuenta."""
        print(f"🔍 Saldo de {self.titular}: ${self.saldo:.2f}")

    def __del__(self):
        """Cierra la cuenta al eliminar el objeto."""
        print(f"🔒 Cuenta de {self.titular} cerrada.")


class Estudiante:
    def __init__(self, nombre, matricula):
        """Inicializa un estudiante con nombre y matrícula."""
        self.nombre = nombre
        self.matricula = matricula
        self.cursos = []
        print(f"🎓 Estudiante '{self.nombre}' (Matrícula: {self.matricula}) registrado.")

    def inscribir_curso(self, curso):
        """Inscribe al estudiante en un curso."""
        self.cursos.append(curso)
        print(f"📚 {self.nombre} inscrito en el curso: {curso.nombre}")

    def mostrar_cursos(self):
        """Muestra los cursos en los que el estudiante está inscrito."""
        print(f"📖 Cursos inscritos de {self.nombre}:")
        for curso in self.cursos:
            print(f"  - {curso.nombre}")

    def __del__(self):
        """Elimina al estudiante del sistema."""
        print(f"🗑️ Registro del estudiante {self.nombre} eliminado.")


class Curso:
    def __init__(self, nombre, codigo):
        """Crea un curso con nombre y código único."""
        self.nombre = nombre
        self.codigo = codigo
        print(f"📘 Curso creado: {self.nombre} ({self.codigo})")

    def __del__(self):
        """Destruye el curso del sistema."""
        print(f"🧹 Curso {self.nombre} eliminado del sistema.")


class Profesor:
    def __init__(self, nombre, id_profesor):
        """Crea un profesor con su ID."""
        self.nombre = nombre
        self.id_profesor = id_profesor
        self.cursos = []
        print(f"👨‍🏫 Profesor {self.nombre} (ID: {self.id_profesor}) registrado.")

    def asignar_curso(self, curso):
        """Asigna un curso al profesor."""
        self.cursos.append(curso)
        print(f"🧾 {self.nombre} asignado al curso: {curso.nombre}")

    def mostrar_cursos(self):
        """Muestra cursos asignados al profesor."""
        print(f"📄 Cursos de {self.nombre}:")
        for curso in self.cursos:
            print(f"  - {curso.nombre}")

    def __del__(self):
        """Elimina al profesor del sistema."""
        print(f"📤 Profesor {self.nombre} eliminado del sistema.")


class Biblioteca:
    def __init__(self, nombre):
        """Inicializa la biblioteca con un nombre."""
        self.nombre = nombre
        self.libros_prestados = []
        print(f"🏛️ Biblioteca '{self.nombre}' activa.")

    def prestar_libro(self, estudiante, libro):
        """Presta un libro a un estudiante."""
        self.libros_prestados.append((estudiante.nombre, libro))
        print(f"📕 Libro '{libro}' prestado a {estudiante.nombre}")

    def devolver_libro(self, estudiante, libro):
        """Devuelve un libro prestado."""
        if (estudiante.nombre, libro) in self.libros_prestados:
            self.libros_prestados.remove((estudiante.nombre, libro))
            print(f"📗 Libro '{libro}' devuelto por {estudiante.nombre}")
        else:
            print("❌ Este libro no estaba prestado.")

    def __del__(self):
        """Cierra la biblioteca."""
        print(f"📚 Biblioteca '{self.nombre}' cerrada.")


# =========================
# Ejecución del programa
# =========================

# Crear cuenta bancaria
cuenta = CuentaBancaria("Luis Herrera", 1000)
cuenta.depositar(300)
cuenta.retirar(200)
cuenta.consultar_saldo()

print("\n----------------------------------\n")

# Crear cursos
curso1 = Curso("Matemáticas", "MAT101")
curso2 = Curso("Programación", "PRG202")

# Crear estudiante e inscribirlo en cursos
estudiante = Estudiante("Ana Torres", "A2025001")
estudiante.inscribir_curso(curso1)
estudiante.inscribir_curso(curso2)
estudiante.mostrar_cursos()

print("\n----------------------------------\n")

# Crear profesor y asignar cursos
profesor = Profesor("Dra. Mariana Ruiz", "P98765")
profesor.asignar_curso(curso1)
profesor.asignar_curso(curso2)
profesor.mostrar_cursos()

print("\n----------------------------------\n")

# Biblioteca: prestar y devolver libros
biblioteca = Biblioteca("Central")
biblioteca.prestar_libro(estudiante, "Estructura de Datos")
biblioteca.devolver_libro(estudiante, "Estructura de Datos")

print("\n✅ Programa finalizado. Los destructores se llamarán automáticamente al cerrar.")
