"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
class CitaMedicaVistaDTO:
    """
    DTO para presentar datos de pacientes en la vista.
    Evita que la GUI tenga que reconstruir información compleja.
    """
    # Este objeto no representa la entidad real del dominio,
    # sino una versión simplificada y lista para mostrar en la interfaz.
    def __init__(self, id_cita: str, paciente: str, medico: str, fecha: str, motivo: str):
        """Constructor de la clase Cita"""
        self.id_cita = id_cita
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.motivo = motivo