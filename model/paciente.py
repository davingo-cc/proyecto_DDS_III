"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
class Paciente:
    """Entidad que representa a un paciente"""
    def __init__(self, cedula_paciente: str, nombre: str, telefono: str, correo: str, provincia: str, id_padecimiento: str):
        """Constructor de la clase paciente"""
        self._cedula_paciente = cedula_paciente
        self._nombre = nombre
        self._telefono = telefono
        self._correo = correo
        self._provincia = provincia
        self._id_padecimiento = id_padecimiento

    # GETTERS/PROPERTIES
    @property
    def cedula_paciente(self):
        return self._cedula_paciente

    @property
    def nombre(self):
        return self._nombre

    @property
    def telefono(self):
        return self._telefono

    @property
    def correo(self):
        return self._correo

    @property
    def provincia(self):
        return self._provincia

    @property
    def id_padecimiento(self):
        return self._id_padecimiento

    def to_dict(self):
        """Convierte a diccionario para guardarlo en el JSON"""
        return {
            "cedula_paciente": self._cedula_paciente,
            "nombre": self._nombre,
            "telefono": self._telefono,
            "correo": self._correo,
            "provincia": self._provincia,
            "id_padecimiento": self._id_padecimiento
        }

    @classmethod
    def from_dict(cls, datos):
        """Convierte a objeto leído desde un diccionario"""
        return cls(
            datos["cedula_paciente"],
            datos["nombre"],
            datos["telefono"],
            datos["correo"],
            datos["provincia"],
            datos["id_padecimiento"]
        )