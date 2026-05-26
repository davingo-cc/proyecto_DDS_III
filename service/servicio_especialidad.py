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
"""Se crean las importaciones"""
from model.especialidad import Especialidad
#=======================================================================================================================
class ServicioEspecialidad:
    """Se crea la clase ServicioEspecialidad"""
#=======================================================================================================================
    def __init__(self,repositorio_especialidad):
        """Constructor que inicializa la instancia"""
        self._repo = (repositorio_especialidad)
#=======================================================================================================================
    def para_registrar(self, id_especialidad: str, nombre: str, area_medica: str, tipo_atencion: str):
        """Registra la especialidad en el repositorio y sus validaciones"""

        if not id_especialidad.strip():
            raise ValueError("Error, el ID esta vacío")

        if not nombre.strip():
            raise ValueError("Error, el nombre esta vacío")

        if not area_medica.strip():
            raise ValueError("Error, el area médica esta vacía")

        if not tipo_atencion.strip():
            raise ValueError("Error, debe seleccionar un tipo")

        ids = set()
        lista = (self._repo.consultar())
        for indice in lista:
            ids.add(indice._id_especialidad)
        if id_especialidad in ids:
            raise ValueError("Error, el ID esta repetido")

        for indice in lista:
            if (indice._nombre.lower() == nombre.lower()):
                raise ValueError("Error, la especialidad esta repetida")

        especialidad = Especialidad(id_especialidad, nombre, area_medica, tipo_atencion)
        self._repo.agregar(especialidad)
#=======================================================================================================================
    def listar(self):
        """Lista de especialidades"""
        return (self._repo.consultar())
#=======================================================================================================================
    def listar_tipo(self, tipo: str):
        """Lista por tipo"""
        return (self._repo.buscar_tipo(tipo))
#=======================================================================================================================
    def reporte_tipo(self):
        """Reporte por tipo"""
        reporte = {}
        lista = (self._repo.consultar())
        for indice in lista:
            tipo = indice._tipo_atencion
            if tipo in reporte:
                reporte[tipo] += 1
            else:
                reporte[tipo] = 1
        return reporte
#=======================================================================================================================