"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
#=======================================================================================================================
"""Se crean las importaciones"""
import tkinter as tk
from tkinter import ttk, messagebox
from utils.constantes import tipos_atencion
#=======================================================================================================================
class VistaEspecialidad(tk.Frame):
    """Se crea la clase VistaEspecialidad"""
#=======================================================================================================================
    def __init__(self, notebook):
        """Constructor que inicializa las instancias"""
        super().__init__(notebook)
        self.config(bg = "#E8D9C5")
#=======================================================================================================================
        """Se configuran estilos"""
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#F5F0E6", foreground="black", fieldbackground="#F5F0E6", rowheight=25)
        style.configure("Treeview.Heading", background="#C8A27A", foreground="black", font=("Arial", 10, "bold"))
#=======================================================================================================================
        """Se crea el titulo"""
        titulo = tk.Label(self, text = "ESPECIALIDADES", bg = "#E8D9C5", fg = "#6B4F3A", font = ("Arial", 20, "bold"))
        titulo.pack(pady = 10)
#=======================================================================================================================
        """Se crea formulario"""
        frame_form = tk.Frame(self, bg = "#F5EBDD", bd = 2, relief = "solid")
        frame_form.pack(padx = 10, pady = 10, fill = "x")
        # Hace que las columnas del frame_form se expandan
        frame_form.columnconfigure(0, weight=1)
        frame_form.columnconfigure(1, weight=1)
        frame_form.columnconfigure(2, weight=1)
        frame_form.columnconfigure(3, weight=1)
#=======================================================================================================================
        """Se crea ID"""
        tk.Label(frame_form, text="ID:", bg="#F5EBDD",  font=('Arial', 11)).grid(row=0, column=0, padx=5, pady=5)
        self.entry_id = tk.Entry(frame_form,  font=('Arial', 11))
        self.entry_id.grid(row = 0, column = 1, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crea nombre"""
        tk.Label(frame_form, text="Nombre:", bg="#F5EBDD", font=('Arial', 11)).grid(row=1, column=0, padx=5, pady=5)
        self.entry_nombre = tk.Entry(frame_form, font=('Arial', 11))
        self.entry_nombre.grid(row = 1, column = 1, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crea area médica"""
        tk.Label(frame_form, text="Área Médica:", bg="#F5EBDD", font=('Arial', 11)).grid(row=2, column=0, padx=5, pady=5)
        self.entry_area = tk.Entry(frame_form, font=('Arial', 11))
        self.entry_area.grid(row = 2, column = 1, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crea tipo atención"""
        tk.Label(frame_form,
                 text = "Tipo de atención:",
                 bg = "#F5EBDD",
                 font=('Arial', 11)
                 ).grid(row = 3, column = 0, padx = 5, pady = 5)
        self.combo_tipo = ttk.Combobox(frame_form, state = "readonly", values = tipos_atencion, font=('Arial', 11))
        self.combo_tipo.grid(row = 3, column = 1, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crean los botones"""
        self.btn_registrar = tk.Button(frame_form,
                                       text = "Registrar",
                                       bg = "#C8A27A",
                                       fg = "white",
                                       font = ("Arial", 11, "bold"),
                                       width = 15)
        self.btn_registrar.grid(row = 5, column = 0, pady = 10, padx=(15, 15))
        self.btn_reporte = tk.Button(frame_form,
                                     text = "Cantidad por tipo",
                                     bg = "#C8A27A",
                                     fg = "white",
                                     width = 17,
                                     font=('Arial', 11, 'bold'))
        self.btn_reporte.grid(row = 5, column = 1, pady = 10, padx=(15, 15))
        self.btn_eliminar = tk.Button(frame_form,
                                      text="Eliminar",
                                      bg="#C8A27A",
                                      fg="white",
                                      width=15,
                                      font=('Arial', 11, 'bold'))
        self.btn_eliminar.grid(row=5, column=2, pady=10, padx=(15, 15))
        self.btn_listar = tk.Button(frame_form,
                                    text="Listar",
                                    bg="#C8A27A",
                                    fg="white",
                                    width=15,
                                    font=('Arial', 11, 'bold'))
        self.btn_listar.grid(row=5, column=3, pady=10, padx=(15, 15))
#=======================================================================================================================
        """Se crea buscar"""
        frame_busqueda = tk.Frame(self, bg = "#E8D9C5")
        frame_busqueda.pack(pady = 5)
        tk.Label(frame_busqueda, text = "Buscar por tipo:", bg = "#E8D9C5", font=('Arial', 11)).pack(side = "left")
        self.combo_buscar = ttk.Combobox(frame_busqueda, state="readonly", values=tipos_atencion, font=('Arial', 11))
        self.combo_buscar.pack(side = "left", padx = 5)
        self.btn_buscar = tk.Button(frame_busqueda, text="Buscar", bg="#C8A27A", fg="white", font=('Arial', 11, 'bold'))
        self.btn_buscar.pack(side = "left")
#=======================================================================================================================
        """Se crea la tabla"""
        columnas = ("id", "nombre", "area", "tipo" )
        self.tabla = ttk.Treeview(self, columns = columnas, show = "headings", height = 12)
        self.tabla.heading("id", text = "ID")
        self.tabla.heading("nombre", text = "Nombre")
        self.tabla.heading("area", text = "Área Médica")
        self.tabla.heading("tipo", text = "Tipo Atención")

        self.tabla.column("id", width = 120)
        self.tabla.column("nombre", width = 220)
        self.tabla.column("area", width = 220)
        self.tabla.column("tipo", width = 180)
        self.tabla.pack(fill = "both", expand = True, padx = 10, pady = 10)
        # Scrollbar
        self.scroll_y = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scroll_y.set)
        # Pack
        self.tabla.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
        self.scroll_y.pack(side="left", fill="y", pady=10)
#=======================================================================================================================
    def obtener_datos(self):
        """Se muestran los datos del usuario"""
        return (
            self.entry_id.get(),
            self.entry_nombre.get(),
            self.entry_area.get(),
            self.combo_tipo.get()
        )
#=======================================================================================================================
    def cargar_tabla(self, lista):
        """Se muestra la tabla"""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for indice in lista:
            self.tabla.insert("", "end", values = (
                    indice.id_especialidad,
                    indice.nombre,
                    indice.area_medica,
                    indice.tipo_atencion
                ))
#=======================================================================================================================
    def obtener_id(self):
        """Retorna el id ingresado"""
        return self.entry_id.get()
#=======================================================================================================================
    @staticmethod
    def mostrar_info(tipo: str, mensaje: str):
        """
        Muestra información al usuario
        :param tipo: tipo de información(error o info)
        :param mensaje: mensaje a mostrar
        """
        if tipo == 'error':
            messagebox.showerror('Error', mensaje)
        else:
            messagebox.showinfo('Información', mensaje)

    def limpiar_campos(self):
        """Limpia los campos del formulario"""
        self.entry_id.delete(0, "end")
        self.entry_nombre.delete(0, "end")
        self.entry_area.delete(0, "end")
        self.combo_tipo.set("")