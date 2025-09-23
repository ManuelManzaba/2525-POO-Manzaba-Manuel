import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Mi Lista de Tareas")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Lista interna para almacenar tareas
        self.tareas = []

        # ------------------ WIDGETS ------------------ #

        # Etiqueta del título
        self.lbl_titulo = tk.Label(root, text="Lista de Tareas", font=("Arial", 16, "bold"))
        self.lbl_titulo.pack(pady=10)

        # Entrada para escribir tarea
        self.entry_tarea = tk.Entry(root, font=("Arial", 12))
        self.entry_tarea.pack(pady=5, padx=10, fill=tk.X)
        self.entry_tarea.bind("<Return>", self.agregar_tarea_evento)

        # Botón para agregar tarea
        self.btn_agregar = tk.Button(root, text="Añadir Tarea", bg="#4CAF50", fg="white", command=self.agregar_tarea)
        self.btn_agregar.pack(pady=5)

        # Listbox para mostrar tareas
        self.listbox_tareas = tk.Listbox(root, font=("Arial", 12), selectbackground="gray")
        self.listbox_tareas.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Botones adicionales
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(pady=10)

        self.btn_completar = tk.Button(self.frame_botones, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_completar.grid(row=0, column=0, padx=5)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=0, column=1, padx=5)

        # Doble clic para completar
        self.listbox_tareas.bind("<Double-Button-1>", self.marcar_completada_evento)

    # ------------------ FUNCIONES ------------------ #

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def agregar_tarea(self):
        texto = self.entry_tarea.get().strip()
        if not texto:
            messagebox.showwarning("Campo vacío", "Por favor, escribe una tarea.")
            return
        self.tareas.append({"texto": texto, "completada": False})
        self.entry_tarea.delete(0, tk.END)
        self.actualizar_listbox()

    def marcar_completada(self):
        seleccion = self.listbox_tareas.curselection()
        if not seleccion:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para marcarla.")
            return
        index = seleccion[0]
        self.tareas[index]["completada"] = not self.tareas[index]["completada"]
        self.actualizar_listbox()

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        seleccion = self.listbox_tareas.curselection()
        if not seleccion:
            messagebox.showinfo("Sin selección", "Selecciona una tarea para eliminarla.")
            return
        index = seleccion[0]
        del self.tareas[index]
        self.actualizar_listbox()

    def actualizar_listbox(self):
        self.listbox_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            if tarea["completada"]:
                texto = "✔ " + texto
            self.listbox_tareas.insert(tk.END, texto)

# ------------------ EJECUCIÓN ------------------ #

if _name_ == "_main_":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
