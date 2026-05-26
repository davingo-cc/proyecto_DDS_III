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
from utils.constantes_padecimiento import tipos_padecimientos, tipo_tiempo
#=======================================================================================================================
class VistaPadecimiento(tk.Frame):
    """Se crea la clase VistaPadecimiento"""
#=======================================================================================================================
    def __init__(self, master):
        """Constructor que inicializa las instancias"""
        super().__init__(master)
        self.config(bg="#E8D9C5")
        self.pack(fill="both", expand = True)
#=======================================================================================================================
        """Se configuran estilos"""
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background = "#F5F0E6", foreground = "black", fieldbackground = "#F5F0E6", rowheight = 25)
        style.configure("Treeview.Heading", background = "#C8A27A", foreground = "black", font = ("Arial", 10, "bold"))
#=======================================================================================================================
        """Se crea el titulo"""
        titulo = tk.Label(self, text = "=====Modulo De Padecimiento=====", bg = "#E8D9C5", fg = "#6B4F3A", font = ("Arial", 20, "bold"))
        titulo.pack(pady = 10)
#=======================================================================================================================
        """Se crea formulario"""
        frame_form = tk.Frame(self, bg = "#F5EBDD", bd = 2, relief = "solid")
        frame_form.pack(padx = 10, pady = 10, fill = "x")
#=======================================================================================================================
        """Se crea ID"""
        tk.Label(frame_form,text = "ID:", bg = "#F5EBDD").grid(row = 0, column = 0, padx = 5, pady = 5)
        self.entry_id = tk.Entry(frame_form)
        self.entry_id.grid(row = 0, column = 1, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crea nombre"""
        tk.Label(frame_form,text = "Nombre:", bg = "#F5EBDD").grid(row = 1, column = 0, padx = 5, pady = 5)
        self.entry_nombre = tk.Entry(frame_form)
        self.entry_nombre.grid(row = 1, column = 1, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crea tipo"""
        tk.Label(frame_form,text = "Tipo:", bg = "#F5EBDD").grid(row = 2, column = 0, padx = 5, pady = 5)
        self.combo_tipo = ttk.Combobox(frame_form, state = "readonly", values = tipos_padecimientos)
        self.combo_tipo.grid(row = 2, column = 1, padx = 5, pady = 5)
#=======================================================================================================================
        """Se crea tratamiento"""
        self.var_check = tk.BooleanVar()
        self.check = tk.Checkbutton(frame_form, text = "Tratamiento prolongado", variable = self.var_check, bg = "#F5EBDD", command = self.mostrar_tratamiento)
        self.check.grid(row = 3, column = 0, columnspan = 2, pady = 5)
#=======================================================================================================================
        """Se crea cantidad"""
        self.label_cantidad = tk.Label(frame_form, text = "Cantidad:", bg = "#F5EBDD")
        self.entry_tiempo = tk.Entry(frame_form)
#=======================================================================================================================
        """Se crea tiempo"""
        self.label_tiempo = tk.Label(frame_form, text = "Tiempo:", bg = "#F5EBDD")
        self.combo_tiempo = ttk.Combobox(frame_form, state = "readonly", values = tipo_tiempo)
#=======================================================================================================================
        """Se crean los botones"""
        self.btn_registrar = tk.Button(frame_form, text = "Registrar", bg = "#C8A27A", fg = "white", font = ("Arial", 11, "bold"), width = 15)
        self.btn_registrar.grid(row = 6, column = 0, pady = 10)
        self.btn_reporte1 = tk.Button(frame_form, text = "Reporte Tipo", bg = "#B08968", fg = "white", width = 15)
        self.btn_reporte1.grid(row = 6, column = 1, pady = 10)
        self.btn_reporte2 = tk.Button(frame_form, text = "Tratamientos", bg = "#B08968", fg = "white", width = 15)
        self.btn_reporte2.grid(row = 6, column = 2, pady = 10)
#=======================================================================================================================
        """Se crea buscar"""
        frame_busqueda = tk.Frame(self, bg = "#E8D9C5")
        frame_busqueda.pack(pady = 5)
        tk.Label(frame_busqueda,text = "Buscar tipo:", bg = "#E8D9C5").pack(side = "left")
        self.combo_buscar = ttk.Combobox(frame_busqueda, state = "readonly", values = tipos_padecimientos)
        self.combo_buscar.pack(side = "left", padx = 5)
        self.btn_buscar = tk.Button(frame_busqueda, text = "Buscar", bg = "#C8A27A", fg ="white")
        self.btn_buscar.pack(side = "left")
#=======================================================================================================================
        """Se crea la tabla"""
        columnas = ("id", "nombre", "tipo", "tratamiento")
        self.tabla = ttk.Treeview(self, columns = columnas, show = "headings", height = 12)
        self.tabla.heading("id", text = "ID")
        self.tabla.heading("nombre", text = "Nombre")
        self.tabla.heading("tipo", text = "Tipo")
        self.tabla.heading("tratamiento", text = "Tratamiento")
        self.tabla.pack(fill = "both", expand = True, padx = 10, pady = 10)
#=======================================================================================================================
    def mostrar_tratamiento(self):
        """Se muestra el tratamiento"""
        if self.var_check.get():
            self.label_cantidad.grid(row = 4, column = 0, pady = 5)
            self.entry_tiempo.grid(row = 4, column = 1, pady = 5)
            self.label_tiempo.grid(row = 5, column = 0, pady = 5)
            self.combo_tiempo.grid(row = 5, column = 1, pady = 5)
        else:
            self.label_cantidad.grid_remove()
            self.entry_tiempo.grid_remove()
            self.label_tiempo.grid_remove()
            self.combo_tiempo.grid_remove()
#=======================================================================================================================
    def obtener_datos(self):
        """Se muestran los datos del usuario"""
        tratamiento = "No necesita"
        if self.var_check.get():
            tratamiento = (
                f"{self.entry_tiempo.get()}/"
                f"{self.combo_tiempo.get()}"
            )

        return (
            self.entry_id.get(),
            self.entry_nombre.get(),
            self.combo_tipo.get(),
            tratamiento
        )
#=======================================================================================================================
    def cargar_tabla(self, lista):
        """Se muestra la tabla"""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for indice in lista:
            self.tabla.insert("", "end",
                values=(
                    indice._id_padecimiento,
                    indice._nombre,
                    indice._tipo,
                    indice._tratamiento_prolongado
                ))
#=======================================================================================================================
    def mostrar_info(self, tipo: str, mensaje: str):
        """
        Muestra información al usuario
        :param tipo: tipo de información(error o info)
        :param mensaje: mensaje a mostrar
        """
        if tipo == 'error':
            messagebox.showerror('Error', mensaje)
        else:
            messagebox.showinfo('Información', mensaje)
#=======================================================================================================================
    def mostrar_info(self, tipo: str, mensaje: str):
        """
        Muestra información al usuario
        :param tipo: tipo de información(error o info)
        :param mensaje: mensaje a mostrar
        """
        if tipo == 'error':
            messagebox.showerror('Error', mensaje)
        else:
            messagebox.showinfo('Información', mensaje)