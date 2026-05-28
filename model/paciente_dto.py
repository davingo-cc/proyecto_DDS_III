class PacienteVistaDTO:
    """
    DTO para presentar datos de pacientes en la vista.
    Evita que la GUI tenga que reconstruir información compleja.
    """
    # Este objeto no representa la entidad real del dominio,
    # sino una versión simplificada y lista para mostrar en la interfaz.
    def __init__(self, cedula_paciente: str, nombre: str, telefono: str, correo: str, provincia: str, padecimiento: str):
        self.cedula_paciente = cedula_paciente
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.provincia = provincia
        self.padecimiento = padecimiento