"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
from repository.repositorio_padecimiento import RepositorioPadecimiento

#=======================================================================================================================
"""Se crean las importaciones"""
import tkinter as tk
from tkinter import ttk, messagebox
from utils.constantes import provincias
#=======================================================================================================================
class VistaPaciente(tk.Frame):
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
        titulo = tk.Label(self, text = "PACIENTES", bg = "#E8D9C5", fg = "#6B4F3A", font = ("Arial", 20, "bold"))
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
        """Se crea Cédula"""
        tk.Label(frame_form, text="Cédula:", bg="#F5EBDD",  font=('Arial', 11)).grid(row=0, column=0, padx=5, pady=5)
        self.entry_cedula = tk.Entry(frame_form,  font=('Arial', 11))
        self.entry_cedula.grid(row = 0, column = 1, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crea nombre"""
        tk.Label(frame_form, text="Nombre:", bg="#F5EBDD", font=('Arial', 11)).grid(row=0, column=2, padx=5, pady=5)
        self.entry_nombre = tk.Entry(frame_form, font=('Arial', 11))
        self.entry_nombre.grid(row=0, column=3, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crea teléfono"""
        tk.Label(frame_form, text="Teléfono:", bg="#F5EBDD", font=('Arial', 11)).grid(row=1, column=0, padx=5, pady=5)
        self.entry_telefono = tk.Entry(frame_form, font=('Arial', 11))
        self.entry_telefono.grid(row=1, column=1, padx=5, pady=5)
#=======================================================================================================================
        """Se crea correo"""
        tk.Label(frame_form, text="Correo:", bg="#F5EBDD", font=('Arial', 11)).grid(row=1, column=2, padx=5, pady=5)
        self.entry_correo = tk.Entry(frame_form, font=('Arial', 11))
        self.entry_correo.grid(row=1, column=3, padx=5, pady=5)
#=======================================================================================================================
        """Se crea provincia"""
        tk.Label(frame_form, text="Provincia:", bg="#F5EBDD", font=('Arial', 11)).grid(row=2, column=0, padx=5, pady=5)
        self.combo_provincia = ttk.Combobox(frame_form, state = "readonly", values = provincias, font=('Arial', 11))
        self.combo_provincia.grid(row=2, column = 1, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crea id_padecimiento"""
        tk.Label(frame_form, text="ID Padecimiento:", bg="#F5EBDD", font=('Arial', 11)).grid(row=2, column=2, padx=5, pady=5)
        self.entry_id_padecimiento= tk.Entry(frame_form, font=('Arial', 11))
        self.entry_id_padecimiento.grid(row=2, column=3, padx=5, pady=5)
#=======================================================================================================================
        """Se crean los botones"""
        # Registrar
        self.btn_registrar = tk.Button(frame_form,
                                       text="Registrar",
                                       bg="#C8A27A",
                                       fg="white",
                                       font=("Arial", 11, "bold"),
                                       width=15)
        self.btn_registrar.grid(row = 5, column = 0, pady = 10, padx=(15, 15))
        # Buscar
        self.btn_buscar = tk.Button(frame_form,
                                    text = "Buscar",
                                    bg = "#C8A27A",
                                    fg = "white",
                                    width = 15,
                                    font=('Arial', 11, 'bold'))
        self.btn_buscar.grid(row = 5, column = 1, pady = 10, padx=(15, 15))
        # Eliminar
        self.btn_eliminar = tk.Button(frame_form,
                                      text="Eliminar",
                                      bg="#C8A27A",
                                      fg="white",
                                      width=15,
                                      font=('Arial', 11, 'bold'))
        self.btn_eliminar.grid(row=5, column=2, pady=10, padx=(15, 15))
        # Listar
        self.btn_listar = tk.Button(frame_form,
                                    text="Listar",
                                    bg="#C8A27A",
                                    fg="white",
                                    width=15,
                                    font=('Arial', 11, 'bold'))
        self.btn_listar.grid(row=5, column=3, pady=10, padx=(15, 15))
#=======================================================================================================================
        """Se crea consultar por provincia y padecimientos"""
        frame_consultas = tk.Frame(self, bg = "#E8D9C5")
        frame_consultas.pack(pady = 5)
        # Provincias
        self.combo_provincias_consulta = ttk.Combobox(frame_consultas,
                                                      state="readonly",
                                                      values=provincias,
                                                      font=('Arial', 11))
        self.combo_provincias_consulta.pack(side="left", padx=5)
        self.btn_consulta_provincia = tk.Button(frame_consultas,
                                                text="Consultar por\nprovincia",
                                                bg="#C8A27A",
                                                fg="white",
                                                font=('Arial', 11, 'bold'))
        self.btn_consulta_provincia.pack(side="left", padx=5)
        tk.Label(frame_consultas, text="       ", bg="#E8D9C5", font=('Arial', 40)).pack(side = "left", padx = 5)
        # Padecimientos
        self.entry_id_padecimiento_consulta = tk.Entry(frame_consultas, font=('Arial', 11))
        self.entry_id_padecimiento_consulta.pack(side ="left", padx=5)
        self.btn_consulta_padecimientos = tk.Button(frame_consultas,
                                                    text="Consultar por\n ID Padecimiento",
                                                    bg="#C8A27A",
                                                    fg="white",
                                                    font=('Arial', 11, 'bold'))
        self.btn_consulta_padecimientos.pack(side ="left", padx=5)
        # =======================================================================================================================
        """Se crea la tabla"""
        columnas = ("cedula", "nombre", 'telefono', "correo", "provincia", 'padecimiento')
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=12)
        self.tabla.heading("cedula", text="Cédula")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.heading("telefono", text="Telefono")
        self.tabla.heading("correo", text = "Correo")
        self.tabla.heading("provincia", text = "Provincia")
        self.tabla.heading("padecimiento", text = "Padecimiento")

        self.tabla.column("cedula", width = 150)
        self.tabla.column("nombre", width = 150)
        self.tabla.column("telefono", width = 150)
        self.tabla.column("correo", width = 150)
        self.tabla.column("provincia", width = 150)
        self.tabla.column("padecimiento", width = 150)
        self.tabla.pack(fill = "both", expand = True, padx = 10, pady = 10)
        # Scrollbar
        self.scroll_y = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scroll_y.set)
        # Pack
        self.tabla.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
        self.scroll_y.pack(side="left", fill="y", pady=10)
#=======================================================================================================================
    def obtener_provincia(self):
        """Retorna la provincia seleccionada en el área de consulta por provincia"""
        return self.combo_provincias_consulta.get()
# =======================================================================================================================
    def obtener_padecimiento(self):
        """Retorna el padecimiento seleccionado en el área de consulta por padecimiento"""
        return self.entry_id_padecimiento_consulta.get()
# =======================================================================================================================
# =======================================================================================================================
    def obtener_datos(self):
        """Se muestran los datos del usuario"""
        return (
            self.entry_cedula.get(),
            self.entry_nombre.get(),
            self.entry_telefono.get(),
            self.entry_correo.get(),
            self.combo_provincia.get(),
            self.entry_id_padecimiento.get(),
        )
#=======================================================================================================================
    def cargar_tabla(self, lista):
        """Se muestra la tabla"""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for indice in lista:
            self.tabla.insert("", "end", values = (
                    indice.cedula_paciente,
                    indice.nombre,
                    indice.telefono,
                    indice.correo,
                    indice.provincia,
                    indice.padecimiento
                ))

    def cargar_tabla_solo_uno(self, paciente):
        """Carga la tabla con un solo paciente"""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        self.tabla.insert("", "end", values = (
                paciente.cedula_paciente,
                paciente.nombre,
                paciente.telefono,
                paciente.correo,
                paciente.provincia,
                paciente.padecimiento
            ))
#=======================================================================================================================
    def obtener_cedula(self):
        """Retorna la cédula ingresado"""
        return self.entry_cedula.get()
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