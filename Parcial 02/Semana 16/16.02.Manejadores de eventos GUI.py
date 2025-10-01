import tkinter as tk
from tkinter import font, messagebox

class TaskApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("420x450")
        self.root.resizable(False, False)

        # Fuente tachada para tareas completadas
        self.default_font = font.Font(family="Helvetica", size=12)
        self.strike_font = font.Font(family="Helvetica", size=12, overstrike=1)

        # Entrada de nueva tarea
        self.entry = tk.Entry(root, font=("Helvetica", 12), width=30)
        self.entry.pack(pady=15)
        self.entry.focus()

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Añadir", width=10, command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Completar", width=10, command=self.complete_task).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar", width=10, command=self.delete_task).grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=45, height=15, font=self.default_font, selectmode=tk.SINGLE)
        self.listbox.pack(pady=15)

        # Estado de las tareas
        self.task_status = {}  # {task_text: is_completed}

        # Atajos de teclado
        root.bind("<Return>", lambda event: self.add_task())
        root.bind("<c>", lambda event: self.complete_task())
        root.bind("<d>", lambda event: self.delete_task())
        root.bind("<Delete>", lambda event: self.delete_task())
        root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            if task not in self.task_status:
                self.listbox.insert(tk.END, task)
                self.task_status[task] = False
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Duplicado", "Esta tarea ya existe.")
        else:
            messagebox.showwarning("Campo vacío", "Escribe una tarea antes de añadir.")

    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            task_text = self.listbox.get(index)

            # Si ya estaba completada, no hacer nada
            if self.task_status.get(task_text, False):
                return

            # Actualizar estado y aspecto visual
            self.task_status[task_text] = True
            self.listbox.delete(index)
            self.listbox.insert(index, task_text)
            self.listbox.itemconfig(index, fg="gray", font=self.strike_font)
        except IndexError:
            messagebox.showwarning("Selecciona una tarea", "No hay tarea seleccionada.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            task_text = self.listbox.get(index)
            self.listbox.delete(index)
            self.task_status.pop(task_text, None)
        except IndexError:
            messagebox.showwarning("Selecciona una tarea", "No hay tarea seleccionada.")

# Ejecutar aplicación
if _name_ == "_main_":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
