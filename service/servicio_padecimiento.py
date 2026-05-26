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
from model.padecimiento import (Padecimiento)
#=======================================================================================================================
class ServicioPadecimiento:
    """Se crea la clase ServicioPadecimiento"""
#=======================================================================================================================
    def __init__(self,repositorio_padecimiento):
        """Constructor que inicializa la instancia"""
        self._repo = (repositorio_padecimiento)
#=======================================================================================================================
    def para_registrar(self, id_padecimiento: str, nombre: str, tipo: str, tratamiento_prolongado: str):
        """Registra el padecimiento en el repositorio, y sus validaciones"""

        if not id_padecimiento.strip():
            raise ValueError("Error, el ID esta vacio")

        if not nombre.strip():
            raise ValueError("Error, el nombre esta vacío")

        if not tipo.strip():
            raise ValueError("Error, debe de seleccionar un tipo")

        ids = set()
        lista = (self._repo.consultar())
        for indice in lista:
            ids.add(indice._id_padecimiento)

        if id_padecimiento in ids:
            raise ValueError("Error, el ID esta repetido")

        for indice in lista:
            if (indice._nombre.lower() == nombre.lower()):
                raise ValueError("Error, el padecimiento esta repetido")

        if (tipo.lower() == "agudo" and tratamiento_prolongado != "no necesita"):
            raise ValueError("Error, agudo no puede tener tratamiento")

        if (tratamiento_prolongado != "No necesita"):
            cantidad_tiempo, tipo_tiempo = tratamiento_prolongado.strip().split('/')

            try:
                cantidad_tiempo = int(cantidad_tiempo)
                if cantidad_tiempo < 0:
                    raise Exception("Error, la cantidad de días/meses debe ser mayor a 0")
            except ValueError:
                raise Exception("Error, la cantidad de días/meses debe ser un número entero mayor a 0")

            if int(numero) <= 0:
                raise ValueError("Error, numero invalido")

        padecimiento = Padecimiento(id_padecimiento, nombre, tipo, tratamiento_prolongado)
        self._repo.agregar(padecimiento)
#=======================================================================================================================
    def listar(self):
        """Lista de padecimientos"""
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
            tipo = indice._tipo

            if tipo in reporte:
                reporte[tipo] += 1
            else:
                reporte[tipo] = 1
        return reporte
#=======================================================================================================================
    def reporte_tratamientos(self):
        """Reporte por tratamientos"""
        lista_aux = []
        lista = (self._repo.consultar())
        for indice in lista:
            if (indice._tratamiento_prolongado != "no necesita"):
                lista_aux.append(indice)
        return lista_aux
#=======================================================================================================================