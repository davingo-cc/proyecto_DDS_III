"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
class CitaMedica:
    """Entidad que representa una cita médica"""
    def __init__(self, id_cita: str, cedula_paciente: str, cedula_medico: str, fecha: str, motivo: str):
        """Constructor de la clase Cita"""
        self._id_cita = id_cita
        self._cedula_paciente = cedula_paciente
        self._cedula_medico = cedula_medico
        self._fecha = fecha
        self._motivo = motivo

    # GETTERS/PROPERTIES
    @property
    def id_cita(self):
        return self._id_cita

    @property
    def cedula_paciente(self):
        return self._cedula_paciente

    @property
    def cedula_medico(self):
        return self._cedula_medico

    @property
    def fecha(self):
        return self._fecha

    @property
    def motivo(self):
        return self._motivo

    def to_dict(self):
        """Convierte a diccionario para guardarlo en el JSON"""
        return {
            "id_cita": self._id_cita,
            "cedula_paciente": self._cedula_paciente,
            "cedula_medico": self._cedula_medico,
            "fecha": self._fecha,
            "motivo": self._motivo
        }

    @classmethod
    def from_dict(cls, datos):
        """Convierte a objeto leído desde un diccionario"""
        return cls(
            datos["id_cita"],
            datos["cedula_paciente"],
            datos["cedula_medico"],
            datos["fecha"],
            datos["motivo"]
        )