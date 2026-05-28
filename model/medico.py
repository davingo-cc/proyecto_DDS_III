"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
class Medico:
    """Entidad que representa a un medico"""
    def __init__(self, cedula_medico: str, nombre: str, telefono: str, correo: str, provincia: str, id_especialidad: str):
        """Constructor de la clase medico"""
        self._cedula_medico = cedula_medico
        self._nombre = nombre
        self._telefono = telefono
        self._correo = correo
        self._provincia = provincia
        self._id_especialidad = id_especialidad

    # GETTERS/PROPERTIES
    @property
    def cedula_medico(self):
        return self._cedula_medico

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
    def id_especialidad(self):
        return self._id_especialidad

    def to_dict(self):
        """Convierte a diccionario para guardarlo en el JSON"""
        return {
            "cedula_medico": self._cedula_medico,
            "nombre": self._nombre,
            "telefono": self._telefono,
            "correo": self._correo,
            "provincia": self._provincia,
            "id_especialidad": self._id_especialidad
        }

    @classmethod
    def from_dict(cls, datos):
        """Convierte a objeto leído desde un diccionario"""
        return cls(
            datos["cedula_medico"],
            datos["nombre"],
            datos["telefono"],
            datos["correo"],
            datos["provincia"],
            datos["id_especialidad"]
        )