import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import datetime

class AgendaPersonalApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("640x420")
        self.root.resizable(False, False)

        # === FRAME DE EVENTOS ===
        frame_eventos = tk.Frame(root)
        frame_eventos.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings", height=12)
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.column("Fecha", width=100, anchor="center")
        self.tree.column("Hora", width=80, anchor="center")
        self.tree.column("Descripción", width=400, anchor="w")

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame_eventos, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # === FRAME DE ENTRADA ===
        frame_entrada = tk.LabelFrame(root, text="Nuevo Evento")
        frame_entrada.pack(pady=10, padx=10, fill="x")

        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.fecha_entry = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern="yyyy-mm-dd")
        self.fecha_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5)
        self.hora_entry = tk.Entry(frame_entrada, width=10)
        self.hora_entry.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame_entrada, width=50)
        self.desc_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        # === FRAME DE BOTONES ===
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento, bg="#d0f0c0", width=18)
        btn_agregar.grid(row=0, column=0, padx=10)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Seleccionado", command=self.eliminar_evento, bg="#f4cccc", width=18)
        btn_eliminar.grid(row=0, column=1, padx=10)

        btn_salir = tk.Button(frame_botones, text="Salir", command=self.root.quit, bg="#cfe2f3", width=10)
        btn_salir.grid(row=0, column=2, padx=10)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get().strip()
        descripcion = self.desc_entry.get().strip()

        if not hora or not descripcion:
            messagebox.showwarning("Campos vacíos", "Todos los campos deben estar completos.")
            return

        try:
            datetime.strptime(hora, "%H:%M")
        except ValueError:
            messagebox.showerror("Hora inválida", "Introduce la hora en formato HH:MM (24h).")
            return

        self.tree.insert("", "end", values=(fecha, hora, descripcion))
        self.hora_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)

    def eliminar_evento(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showinfo("Sin selección", "Selecciona un evento para eliminar.")
            return

        confirmar = messagebox.askyesno("Confirmar eliminación", "¿Eliminar el evento seleccionado?")
        if confirmar:
            self.tree.delete(seleccionado)

# === EJECUTAR APP ===
if _name_ == "_main_":
    root = tk.Tk()
    app = AgendaPersonalApp(root)
    root.mainloop()
