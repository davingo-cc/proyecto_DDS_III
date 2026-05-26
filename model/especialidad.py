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
        self._id_especialidad = (id_especialidad)
        self._nombre = nombre
        self._area_medica = area_medica
        self._tipo_atencion = (tipo_atencion)
#=======================================================================================================================
    def __str__(self):
        """Retorna la informacion del objeto"""
        return (
            f"{self._id_especialidad} "
            f"{self._nombre}"
        )
#=======================================================================================================================
    def to_dict(self):
        """Convierte a diccionario"""
        return {
            "ID": self._id_especialidad,
            "Nombre": self._nombre,
            "Area": self._area_medica,
            "Tipo": self._tipo_atencion
        }
#=======================================================================================================================
    @classmethod
    def from_dict(cls, datos):
        """Convierte a objeto"""
        return cls(
            datos["ID"],
            datos["Nombre"],
            datos["Area"],
            datos["Tipo"]
        )
#=======================================================================================================================