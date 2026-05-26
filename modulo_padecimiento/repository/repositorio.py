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
from typing import Generic
from typing import TypeVar
#=======================================================================================================================
"""Asignación de valor"""
T = TypeVar("T")
#=======================================================================================================================
class Repositorio(Generic[T]):
    """Crea el repositorio del objeto"""
#=======================================================================================================================
    def __init__(self):
        """Constructor que inicaliza la lista del objeto"""
        self.lista_entidades = []
#=======================================================================================================================
    def agregar(self, entidad: T):
        """Agrega el objeto de la lista de entidades"""
        pass
#=======================================================================================================================
    def consultar(self):
        """Consultar toda la entidad"""
        pass
#=======================================================================================================================