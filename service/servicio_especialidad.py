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
        self._repo = repositorio_especialidad
#=======================================================================================================================
    def para_registrar(self, id_especialidad: str, nombre: str, area_medica: str, tipo_atencion: str):
        """Registra la especialidad en el repositorio y sus validaciones"""
        id_especialidad = id_especialidad.strip()
        nombre = nombre.strip()
        area_medica = area_medica.strip()

        if not id_especialidad:
            raise ValueError("ERROR | El ID esta vacío")

        if not nombre:
            raise ValueError("ERROR | El nombre esta vacío")

        if not area_medica:
            raise ValueError("ERROR | El area médica esta vacía")

        if not tipo_atencion:
            raise ValueError("ERROR | Debe seleccionar un tipo de atención")

        ids = set()
        lista = self._repo.listar()
        for indice in lista:
            ids.add(indice.id_especialidad)
        if id_especialidad in ids:
            raise ValueError("ERROR | El ID esta repetido")

        for indice in lista:
            if indice.nombre.lower() == nombre.lower():
                raise ValueError("ERROR | La especialidad esta repetida")

        especialidad = Especialidad(id_especialidad, nombre, area_medica, tipo_atencion)
        self._repo.agregar(especialidad)
#=======================================================================================================================
    def listar(self):
        """Lista de especialidades"""
        return self._repo.listar()
#=======================================================================================================================
    def listar_tipo(self, tipo: str):
        """Lista por tipo"""
        return self._repo.buscar_por_tipo(tipo)
#=======================================================================================================================
    def reporte_tipo(self):
        """Reporte por tipo"""
        reporte = {}
        lista = self._repo.listar()
        for indice in lista:
            tipo = indice.tipo_atencion
            if tipo in reporte:
                reporte[tipo] += 1
            else:
                reporte[tipo] = 1
        return reporte
#=======================================================================================================================
    def buscar_por_id(self, id_especialidad: str):
        """Busca una especialidad por ID"""
        return self._repo.buscar_por_id(id_especialidad)
#=======================================================================================================================
    def eliminar(self, id_especialidad: str):
        """Método que elimina un padecimiento según su id"""
        if not id_especialidad.strip():
            raise ValueError("ERROR | El ID esta vacío")
        eliminar = self._repo.buscar_por_id(id_especialidad)
        if not eliminar:
            raise Exception('ERROR | No existe una especialidad con ese id')
        self._repo.eliminar(eliminar)