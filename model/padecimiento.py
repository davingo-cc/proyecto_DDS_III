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
        self._tratamiento_prolongado = (tratamiento_prolongado)
#=======================================================================================================================
    def __str__(self):
        """Retorna la informacion del objeto"""
        return (
            f"{self._id_padecimiento} "
            f"{self._nombre}"
            f"{self._tipo}"
            f"{self._tratamiento_prolongado}"
        )
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