"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
import tkinter as tk

from controller.controlador_especialidad import ControladorEspecialidad
from controller.controlador_medicos import ControladorMedico
from controller.controlador_pacientes import ControladorPaciente
from controller.controlador_padecimiento import ControladorPadecimiento
from controller.controlador_cita_medica import ControladorCitaMedica
from controller.controlador_reportes import ControladorReportes

from repository.repositorio_especialidad import RepositorioEspecialidad
from repository.repositorio_medico import RepositorioMedico
from repository.repositorio_paciente import RepositorioPaciente
from repository.repositorio_padecimiento import RepositorioPadecimiento
from repository.repositorio_cita_medica import RepositorioCitaMedica

from service.servicio_especialidad import ServicioEspecialidad
from service.servicio_medico import ServicioMedico
from service.servicio_paciente import ServicioPaciente
from service.servicio_padecimiento import ServicioPadecimiento
from service.servicio_cita_medica import ServicioCitaMedica
from service.servicio_reportes import ServicioReportes

from view.vista_principal import VistaPrincipal
from view.vista_especialidad import VistaEspecialidad
from view.vista_padecimiento import VistaPadecimiento
from view.vista_paciente import VistaPaciente
from view.vista_medico import VistaMedico
from view.vista_cita_medica import VistaCitaMedica
from view.vista_reportes import VistaReportes

#=======================================================================================================================
def main():
    ventana = tk.Tk()
    principal = VistaPrincipal(ventana, VistaEspecialidad, VistaPadecimiento, VistaPaciente,
                               VistaMedico, VistaCitaMedica, VistaReportes)

    # Repositorios
    repo_especialidad = RepositorioEspecialidad()
    repo_padecimiento = RepositorioPadecimiento()
    repo_paciente = RepositorioPaciente()
    repo_medico = RepositorioMedico()
    repo_cita = RepositorioCitaMedica()

    # Servicios
    servicio_especialidad = ServicioEspecialidad(repo_especialidad)
    servicio_padecimiento = ServicioPadecimiento(repo_padecimiento)
    servicio_paciente = ServicioPaciente(repo_paciente, repo_padecimiento)
    servicio_medico = ServicioMedico(repo_medico, repo_especialidad)
    servicio_cita = ServicioCitaMedica(repo_cita, repo_paciente, repo_medico)
    servicio_reportes = ServicioReportes(repo_cita, repo_paciente, repo_medico,
                                         repo_especialidad, repo_padecimiento)

    # Controladores
    ControladorEspecialidad(principal.vista_especialidad, servicio_especialidad)
    ControladorPadecimiento(principal.vista_padecimiento, servicio_padecimiento)
    ControladorPaciente(principal.vista_paciente, servicio_paciente)
    ControladorMedico(principal.vista_medico, servicio_medico)
    ControladorCitaMedica(principal.vista_cita_medica, servicio_cita)
    ControladorReportes(principal.vista_reporte, servicio_reportes)

    ventana.mainloop()

if __name__ == "__main__":
    main()
