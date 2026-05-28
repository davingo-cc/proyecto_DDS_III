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
class Especialidad:
    """Crea el objeto Especialidad"""
#=======================================================================================================================
    def __init__(self, id_especialidad: str, nombre: str, area_medica: str, tipo_atencion: str):
        """Constructor que inicializa los atributos del objeto"""
        self._id_especialidad = id_especialidad
        self._nombre = nombre
        self._area_medica = area_medica
        self._tipo_atencion = tipo_atencion
#=======================================================================================================================
    def to_dict(self):
        """Convierte a diccionario"""
        return {
            "ID": self._id_especialidad,
            "Nombre": self._nombre,
            "Área médica": self._area_medica,
            "Tipo": self._tipo_atencion
        }
#=======================================================================================================================
    @classmethod
    def from_dict(cls, datos):
        """Convierte a objeto"""
        return cls(
            datos["ID"],
            datos["Nombre"],
            datos["Área médica"],
            datos["Tipo"]
        )
#=======================================================================================================================
    # GETTERS/PROPERTIES
    @property
    def id_especialidad(self):
        return self._id_especialidad

    @property
    def nombre(self):
        return self._nombre

    @property
    def area_medica(self):
        return self._area_medica

    @property
    def tipo_atencion(self):
        return self._tipo_atencion