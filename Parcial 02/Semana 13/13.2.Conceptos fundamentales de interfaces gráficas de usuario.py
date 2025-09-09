import tkinter as tk
from tkinter import ttk, messagebox

# -------------------------------
# Funciones de la aplicación
# -------------------------------

def agregar_item():
    item = entrada_dato.get()
    if item.strip() != "":
        tabla.insert('', 'end', values=(item,))
        entrada_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

def limpiar_seleccion():
    seleccion = tabla.selection()
    if seleccion:
        for item in seleccion:
            tabla.delete(item)
    entrada_dato.delete(0, tk.END)

# -------------------------------
# Configuración de la ventana
# -------------------------------

ventana = tk.Tk()
ventana.title("Aplicación de Registro de Datos")
ventana.geometry("500x350")
ventana.resizable(False, False)

# -------------------------------
# Widgets de la interfaz
# -------------------------------

# Título
titulo = tk.Label(ventana, text="Registro de Datos con Tkinter", font=("Arial", 14, "bold"))
titulo.pack(pady=10)

# Etiqueta y entrada
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack()

entrada_dato = tk.Entry(ventana, width=40)
entrada_dato.pack(pady=5)

# Botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar", width=15, command=agregar_item, bg="#4CAF50", fg="white")
btn_agregar.grid(row=0, column=0, padx=10)

btn_limpiar = tk.Button(frame_botones, text="Eliminar Seleccionado", width=20, command=limpiar_seleccion, bg="#F44336", fg="white")
btn_limpiar.grid(row=0, column=1, padx=10)

# Tabla de datos
tabla = ttk.Treeview(ventana, columns=("Dato"), show='headings')
tabla.heading("Dato", text="Dato Ingresado")
tabla.pack(pady=10, fill="x", padx=20)

# -------------------------------
# Ejecutar la aplicación
# -------------------------------

ventana.mainloop()
