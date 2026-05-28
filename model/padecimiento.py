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
class Padecimiento:
    """Crea el objeto Padecimiento"""
#=======================================================================================================================
    def __init__(self, id_padecimiento: str, nombre: str, tipo: str, tratamiento_prolongado: str):
        """Constructor que inicializa los atributos del objeto"""
        self._id_padecimiento = id_padecimiento
        self._nombre = nombre
        self._tipo = tipo
        self._tratamiento_prolongado = tratamiento_prolongado
#=======================================================================================================================
    # GETTERS/PROPERTIES
    @property
    def id_padecimiento(self):
        return self._id_padecimiento

    @property
    def nombre(self):
        return self._nombre

    @property
    def tipo(self):
        return self._tipo

    @property
    def tratamiento_prolongado(self):
        return self._tratamiento_prolongado
#=======================================================================================================================
    def to_dict(self):
        """Convierte a diccionario"""
        return {
            "ID": self._id_padecimiento,
            "Nombre": self._nombre,
            "Tipo": self._tipo,
            "Tratamiento": self._tratamiento_prolongado
        }
#=======================================================================================================================
    @classmethod
    def from_dict(cls, datos):
        """Convierte a objeto"""
        return cls(
            datos["ID"],
            datos["Nombre"],
            datos["Tipo"],
            datos["Tratamiento"]
        )
#=======================================================================================================================