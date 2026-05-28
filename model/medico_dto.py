class MedicoVistaDTO:
    """
    DTO para presentar datos de medicos en la vista.
    Evita que la GUI tenga que reconstruir información compleja.
    """
    # Este objeto no representa la entidad real del dominio,
    # sino una versión simplificada y lista para mostrar en la interfaz.
    def __init__(self, cedula_medico: str, nombre: str, telefono: str, correo: str, provincia: str, especialidad: str):
        self.cedula_medico = cedula_medico
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.provincia = provincia
        self.especialidad = especialidad