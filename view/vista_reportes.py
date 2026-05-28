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
#=======================================================================================================================
class VistaReportes(tk.Frame):
    """Se crea la clase VistaReportes"""
#=======================================================================================================================
    def __init__(self, notebook):
        """Constructor que inicializa las instancias"""
        super().__init__(notebook)
        self.config(bg="#E8D9C5")
#=======================================================================================================================
        """Se configuran estilos"""
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#F5F0E6", foreground="black", fieldbackground="#F5F0E6", rowheight=25)
        style.configure("Treeview.Heading", background="#C8A27A", foreground="black", font=("Arial", 10, "bold"))
#=======================================================================================================================
        """Se crea el titulo"""
        titulo = tk.Label(self, text="REPORTES", bg="#E8D9C5", fg="#6B4F3A", font=("Arial", 20, "bold"))
        titulo.pack(pady=10)
#=======================================================================================================================
        """Se crea reporte 1: Top 3 pacientes con más citas"""
        frame_reporte1 = tk.Frame(self, bg="#F5EBDD", bd=2, relief="solid")
        frame_reporte1.pack(padx=10, pady=5, fill="x")

        frame_titulo1 = tk.Frame(frame_reporte1, bg="#C8A27A")
        frame_titulo1.pack(fill="x")
        tk.Label(frame_titulo1,
                 text="Top 3 — Pacientes con más citas registradas",
                 bg="#C8A27A",
                 fg="white",
                 font=("Arial", 11, "bold")).pack(side="left", padx=10, pady=5)
        self.btn_reporte1 = tk.Button(frame_titulo1,
                                      text="Generar",
                                      bg="#6B4F3A",
                                      fg="white",
                                      font=("Arial", 10, "bold"),
                                      width=10)
        self.btn_reporte1.pack(side="right", padx=10, pady=5)

        columnas1 = ("posicion", "cedula", "nombre", "total_citas")
        self.tabla_reporte1 = ttk.Treeview(frame_reporte1, columns=columnas1, show="headings", height=3)
        self.tabla_reporte1.heading("posicion", text="#")
        self.tabla_reporte1.heading("cedula", text="Cédula")
        self.tabla_reporte1.heading("nombre", text="Nombre")
        self.tabla_reporte1.heading("total_citas", text="Total de Citas")
        self.tabla_reporte1.column("posicion", width=50)
        self.tabla_reporte1.column("cedula", width=150)
        self.tabla_reporte1.column("nombre", width=300)
        self.tabla_reporte1.column("total_citas", width=150)
        self.tabla_reporte1.pack(fill="x", padx=10, pady=10)
#=======================================================================================================================
        """Se crea reporte 2: Padecimiento más frecuente por provincia"""
        frame_reporte2 = tk.Frame(self, bg="#F5EBDD", bd=2, relief="solid")
        frame_reporte2.pack(padx=10, pady=5, fill="x")

        frame_titulo2 = tk.Frame(frame_reporte2, bg="#C8A27A")
        frame_titulo2.pack(fill="x")
        tk.Label(frame_titulo2,
                 text="Padecimiento más frecuente por provincia",
                 bg="#C8A27A",
                 fg="white",
                 font=("Arial", 11, "bold")).pack(side="left", padx=10, pady=5)
        self.btn_reporte2 = tk.Button(frame_titulo2,
                                      text="Generar",
                                      bg="#6B4F3A",
                                      fg="white",
                                      font=("Arial", 10, "bold"),
                                      width=10)
        self.btn_reporte2.pack(side="right", padx=10, pady=5)

        columnas2 = ("provincia", "padecimiento", "cantidad")
        self.tabla_reporte2 = ttk.Treeview(frame_reporte2, columns=columnas2, show="headings", height=7)
        self.tabla_reporte2.heading("provincia", text="Provincia")
        self.tabla_reporte2.heading("padecimiento", text="Padecimiento más frecuente")
        self.tabla_reporte2.heading("cantidad", text="Cantidad de pacientes")
        self.tabla_reporte2.column("provincia", width=200)
        self.tabla_reporte2.column("padecimiento", width=250)
        self.tabla_reporte2.column("cantidad", width=200)
        self.tabla_reporte2.pack(fill="x", padx=10, pady=10)
#=======================================================================================================================
        """Se crea reporte 3: Especialidad más demandada"""
        frame_reporte3 = tk.Frame(self, bg="#F5EBDD", bd=2, relief="solid")
        frame_reporte3.pack(padx=10, pady=5, fill="x")

        frame_titulo3 = tk.Frame(frame_reporte3, bg="#C8A27A")
        frame_titulo3.pack(fill="x")
        tk.Label(frame_titulo3,
                 text="Especialidad más demandada",
                 bg="#C8A27A",
                 fg="white",
                 font=("Arial", 11, "bold")).pack(side="left", padx=10, pady=5)
        self.btn_reporte3 = tk.Button(frame_titulo3,
                                      text="Generar",
                                      bg="#6B4F3A",
                                      fg="white",
                                      font=("Arial", 10, "bold"),
                                      width=10)
        self.btn_reporte3.pack(side="right", padx=10, pady=5)

        columnas3 = ("especialidad", "area", "total_citas")
        self.tabla_reporte3 = ttk.Treeview(frame_reporte3, columns=columnas3, show="headings", height=5)
        self.tabla_reporte3.heading("especialidad", text="Especialidad")
        self.tabla_reporte3.heading("area", text="Área Médica")
        self.tabla_reporte3.heading("total_citas", text="Total de Citas")
        self.tabla_reporte3.column("especialidad", width=250)
        self.tabla_reporte3.column("area", width=250)
        self.tabla_reporte3.column("total_citas", width=150)
        self.tabla_reporte3.pack(fill="x", padx=10, pady=10)
#=======================================================================================================================
    def cargar_reporte1(self, lista):
        """Carga el top 3 de pacientes con más citas"""
        for fila in self.tabla_reporte1.get_children():
            self.tabla_reporte1.delete(fila)
        for indice in lista:
            self.tabla_reporte1.insert("", "end", values=(
                indice.posicion,
                indice.cedula,
                indice.nombre,
                indice.total_citas
            ))
#=======================================================================================================================
    def cargar_reporte2(self, lista):
        """Carga el padecimiento más frecuente por provincia"""
        for fila in self.tabla_reporte2.get_children():
            self.tabla_reporte2.delete(fila)
        for indice in lista:
            self.tabla_reporte2.insert("", "end", values=(
                indice.provincia,
                indice.padecimiento,
                indice.cantidad
            ))
#=======================================================================================================================
    def cargar_reporte3(self, lista):
        """Carga las especialidades ordenadas por demanda"""
        for fila in self.tabla_reporte3.get_children():
            self.tabla_reporte3.delete(fila)
        for indice in lista:
            self.tabla_reporte3.insert("", "end", values=(
                indice.especialidad,
                indice.area,
                indice.total_citas
            ))
#=======================================================================================================================
    @staticmethod
    def mostrar_info(tipo: str, mensaje: str):
        """Muestra información al usuario"""
        if tipo == 'error':
            messagebox.showerror('Error', mensaje)
        else:
            messagebox.showinfo('Información', mensaje)