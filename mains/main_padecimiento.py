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
from view.vista_padecimiento import VistaPadecimiento
from controller.controlador_padecimiento import ControladorPadecimiento
from service.servicio_padecimiento import ServicioPadecimiento
from repository.repositorio_padecimiento import RepositorioPadecimiento
#=======================================================================================================================
"""Se crea la funcionalidad de la ventana"""
def main():
    ventana = tk.Tk()
    ventana.title("Sistema Médico")
    ventana.geometry("950x650")
    ventana.config(bg = "#DCEEFF")
#===================================================================================================================
    """Se controla la estructura MVC"""
    vista = VistaPadecimiento(ventana)
    repositorio = RepositorioPadecimiento()
    servicio = ServicioPadecimiento(repositorio)
    controlador = ControladorPadecimiento(vista, servicio)
    ventana.mainloop()
#=======================================================================================================================
"""Ejecución principal"""
if __name__ == "__main__":
    main()
#=======================================================================================================================