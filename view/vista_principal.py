import tkinter as tk
from tkinter import ttk
from view.vista_especialidad import VistaEspecialidad
from view.vista_padecimiento import VistaPadecimiento

class VistaPrincipal:
    """Vista principal del sistema, contiene el notebook con todas las pestañas"""

    def __init__(self, root, vista_especialidad, vista_padecimiento, vista_paciente, vista_medico, vista_cita_medica, vista_reporte):
        """Constructor que inicializa la ventana principal y sus componentes"""
        self.root = root
        self.centrar_ventana(950, 750)

        # Se configura la ventana principal
        self.root.title("Sistema Médico")
        self.root.geometry("950x750")
        self.root.config(bg="#E8D9C5")

        # Se configura el estilo del notebook
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TNotebook", background="#E8D9C5")
        style.configure("TNotebook.Tab",
                        background="#C8A27A",
                        foreground="white",
                        font=("Arial", 11, "bold"),
                        padding=(10, 5))
        style.map("TNotebook.Tab",
                  background=[("selected", "#6B4F3A")],
                  foreground=[("selected", "white")])

        # Se crea el notebook que contendrá todas las vistas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Se instancian las vistas pasando el notebook como master
        self.vista_especialidad = vista_especialidad(self.notebook)
        self.vista_padecimiento = vista_padecimiento(self.notebook)
        self.vista_paciente = vista_paciente(self.notebook)
        self.vista_medico = vista_medico(self.notebook)
        self.vista_cita_medica = vista_cita_medica(self.notebook)
        self.vista_reporte = vista_reporte(self.notebook)

        # Se agregan todas las pestañas al notebook
        self.notebook.add(self.vista_especialidad, text="  Especialidades  ")
        self.notebook.add(self.vista_padecimiento, text="  Padecimientos  ")
        self.notebook.add(self.vista_paciente, text="  Pacientes  ")
        self.notebook.add(self.vista_medico, text="  Médicos  ")
        self.notebook.add(self.vista_cita_medica, text="  Citas médicas  ")
        self.notebook.add(self.vista_reporte, text="  Reportes  ")

    def centrar_ventana(self, ancho: int, alto: int):
        """Centra la ventana en la pantalla"""
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2) - 40
        self.root.geometry(f"{ancho}x{alto}+{x}+{y}")