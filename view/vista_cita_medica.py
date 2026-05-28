"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
from utils.constantes import meses, years

#=======================================================================================================================
"""Se crean las importaciones"""
import tkinter as tk
from tkinter import ttk, messagebox
from utils.constantes import provincias
#=======================================================================================================================
class VistaCitaMedica(tk.Frame):
    """Se crea la clase VistaCitaMedica"""
#=======================================================================================================================
    def __init__(self, notebook):
        """Constructor que inicializa las instancias"""
        super().__init__(notebook)
        self.config(bg = "#E8D9C5")
#=======================================================================================================================
        """Se configuran estilos"""
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#F5F0E6", foreground="black", fieldbackground="#F5F0E6",
                        rowheight=25)
        style.configure("Treeview.Heading", background="#C8A27A", foreground="black", font=("Arial", 10, "bold"))
#=======================================================================================================================
        """Se crea el titulo"""
        titulo = tk.Label(self, text = "CITAS MÉDICAS", bg = "#E8D9C5", fg = "#6B4F3A", font = ("Arial", 20, "bold"))
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
        """Se crea id"""
        tk.Label(frame_form, text="ID de cita:", bg="#F5EBDD",  font=('Arial', 11)).grid(row=0, column=0, padx=5,
                                                                                         pady=5)
        self.entry_id = tk.Entry(frame_form,  font=('Arial', 11))
        self.entry_id.grid(row = 0, column = 1, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crea cédula paciente"""
        tk.Label(frame_form, text="Cédula del paciente:", bg="#F5EBDD", font=('Arial', 11)).grid(row=0, column=2,
                                                                                                 padx=5, pady=5)
        self.entry_cedula_paciente = tk.Entry(frame_form, font=('Arial', 11))
        self.entry_cedula_paciente.grid(row=0, column=3, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crea motivo"""
        tk.Label(frame_form, text="Motivo:", bg="#F5EBDD", font=('Arial', 11)).grid(row=1, column=0, padx=5, pady=5)
        self.entry_motivo = tk.Entry(frame_form, font=('Arial', 11))
        self.entry_motivo.grid(row=1, column=1, padx=5, pady=5)
#=======================================================================================================================
        """Se crea cédula médico"""
        tk.Label(frame_form, text="Cédula del médico:", bg="#F5EBDD", font=('Arial', 11)).grid(row=1, column=2, padx=5,
                                                                                               pady=5)
        self.entry_cedula_medico = tk.Entry(frame_form, font=('Arial', 11))
        self.entry_cedula_medico.grid(row=1, column=3, padx=5, pady=5)
#=======================================================================================================================
        """Se crea fecha"""
        frame_fecha = tk.Frame(frame_form, bg="#F5EBDD", bd=2)
        frame_fecha.grid(row=2, rowspan=2, column=0, columnspan=4, padx=5, pady=5, sticky='ew')
        # Hace que las columnas del frame_form se expandan
        for i in range(6):
            frame_fecha.columnconfigure(i, weight=1)
        tk.Label(frame_fecha, text="Fecha de la cita:", bg="#F5EBDD", font=('Arial', 11, 'bold')).grid(row=0, column=2,
                                                                                              columnspan=2, padx=2,
                                                                                              pady=2, sticky='ew')
        # Día
        tk.Label(frame_fecha, text="Día:", bg="#F5EBDD", font=('Arial', 11)).grid(row=1, column=0, padx=2, pady=2)
        self.entry_dia = tk.Entry(frame_fecha, font=('Arial', 11))
        self.entry_dia.grid(row=1, column=1, padx=2, pady=2)
        # Mes
        tk.Label(frame_fecha, text="Mes:", bg="#F5EBDD", font=('Arial', 11)).grid(row=1, column=2, padx=2, pady=2)
        self.combo_meses = ttk.Combobox(frame_fecha, state="readonly", values=meses, font=('Arial', 11))
        self.combo_meses.grid(row=1, column=3, padx=2, pady=2)
        # Año
        tk.Label(frame_fecha, text="Año:", bg="#F5EBDD", font=('Arial', 11)).grid(row=1, column=4, padx=2, pady=2)
        self.combo_years = ttk.Combobox(frame_fecha, state="readonly", values=years, font=('Arial', 11))
        self.combo_years.grid(row=1, column=5, padx=2, pady=2)
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
        """Se crea consultar por médico"""
        frame_consultas = tk.Frame(self, bg = "#E8D9C5")
        frame_consultas.pack(pady = 5)
        tk.Label(frame_consultas, text="Cédula del médico a consultar:", bg="#E8D9C5", font=('Arial', 11)).pack(side ="left", padx=5)
        self.entry_cedula_medico_consulta = tk.Entry(frame_consultas, font=('Arial', 11))
        self.entry_cedula_medico_consulta.pack(side ="left", padx=5)
        self.btn_consulta_medico = tk.Button(frame_consultas,
                                                    text="Consultar por\n médicos",
                                                    bg="#C8A27A",
                                                    fg="white",
                                                    font=('Arial', 11, 'bold'))
        self.btn_consulta_medico.pack(side ="left", padx=5)
        # =======================================================================================================================
        """Se crea la tabla"""
        columnas = ("id_cita", "paciente", 'medico', "fecha", "motivo")
        self.tabla = ttk.Treeview(self, columns=columnas, show="headings", height=12)
        self.tabla.heading("id_cita", text="ID Cita")
        self.tabla.heading("paciente", text="Paciente")
        self.tabla.heading("medico", text="Médico")
        self.tabla.heading("fecha", text = "Fecha")
        self.tabla.heading("motivo", text = "Motivo")

        self.tabla.column("id_cita", width = 165)
        self.tabla.column("paciente", width = 165)
        self.tabla.column("medico", width = 165)
        self.tabla.column("fecha", width = 165)
        self.tabla.column("motivo", width = 165)
        self.tabla.pack(fill = "both", expand = True, padx = 10, pady = 10)
        # Scrollbar
        self.scroll_y = ttk.Scrollbar(self, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=self.scroll_y.set)
        # Pack
        self.tabla.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
        self.scroll_y.pack(side="left", fill="y", pady=10)
# ======================================================================================================================
    def obtener_cedula_medico(self):
        """Retorna la cédula ingresada en el ahora de consultas"""
        return self.entry_cedula_medico_consulta.get()

    def cargar_tabla_solo_uno(self, cita_medica_dto):
        """Carga la tabla con un solo paciente"""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        self.tabla.insert("", "end", values = (
                cita_medica_dto.id_cita,
                cita_medica_dto.paciente,
                cita_medica_dto.medico,
                cita_medica_dto.fecha,
                cita_medica_dto.motivo,
            ))
#=======================================================================================================================
    def obtener_datos(self):
        """Se muestran los datos del usuario"""
        return (
            self.entry_id.get(),
            self.entry_cedula_paciente.get(),
            self.entry_cedula_medico.get(),
            self.entry_dia.get(),
            self.combo_meses.get(),
            self.combo_years.get(),
            self.entry_motivo.get()
        )
#=======================================================================================================================
    def cargar_tabla(self, lista):
        """Se muestra la tabla, la lista debe contener solo objetos tipo CitaMedicaDTO"""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for indice in lista:
            self.tabla.insert("", "end", values = (
                    indice.id_cita,
                    indice.paciente,
                    indice.medico,
                    indice.fecha,
                    indice.motivo,
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
        self.entry_cedula_paciente.delete(0, "end")
        self.entry_cedula_medico.delete(0, "end")
        self.entry_dia.delete(0, "end")
        self.entry_motivo.delete(0, "end")
        self.combo_meses.set("")
        self.combo_years.set("")