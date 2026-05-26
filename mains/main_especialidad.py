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
from view.vista_especialidad import VistaEspecialidad
from controller.controlador_especialidad import ControladorEspecialidad
from service.servicio_especialidad import ServicioEspecialidad
from repository.repositorio_especialidad import RepositorioEspecialidad
#=======================================================================================================================
"""Se crea la funcionalidad de la ventana"""
def main():
    ventana = tk.Tk()
    ventana.title("Sistema Médico")
    ventana.geometry("950x650")
    ventana.config(bg = "#E8D9C5")
#=======================================================================================================================
    """Se controla la estructura MVC"""
    vista = VistaEspecialidad(ventana)
    repositorio = RepositorioEspecialidad()
    servicio = ServicioEspecialidad(repositorio)
    controlador = ControladorEspecialidad(vista, servicio)
    ventana.mainloop()
#=======================================================================================================================
"""Ejecución principal"""
if __name__ == "__main__":
    main()
#=======================================================================================================================