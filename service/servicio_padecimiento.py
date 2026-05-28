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
    def __init__(self, repositorio_padecimiento):
        """Constructor que inicializa la instancia"""
        self._repo = repositorio_padecimiento
#=======================================================================================================================
    def para_registrar(self, id_padecimiento: str, nombre: str, tipo: str, tratamiento_prolongado: str):
        """Registra el padecimiento en el repositorio, y sus validaciones"""
        id_padecimiento = id_padecimiento.strip()
        nombre = nombre.strip()

        if not id_padecimiento:
            raise ValueError("ERROR | El ID esta vacío")

        if not nombre:
            raise ValueError("ERROR | El nombre esta vacío")

        if not tipo:
            raise ValueError("ERROR | Debe seleccionar un tipo")

        ids = set()
        lista = (self._repo.listar())
        for indice in lista:
            ids.add(indice.id_padecimiento)

        if id_padecimiento in ids:
            raise ValueError("ERROR | el ID esta repetido")

        for indice in lista:
            if indice.nombre.lower() == nombre.lower():
                raise ValueError("ERROR | el padecimiento esta repetido")

        if tipo.lower() == "agudo" and tratamiento_prolongado != "No necesita":
            raise ValueError(
                "ERROR | agudo no puede tener tratamiento prolongado ya que un padecimiento agudo es de corta duración."
            )

        if tratamiento_prolongado != "No necesita":
            cantidad_tiempo, tipo_tiempo = tratamiento_prolongado.strip().split('/')

            try:
                cantidad_tiempo = int(cantidad_tiempo)
            except ValueError:
                raise ValueError("ERROR | La duración debe ser un número entero")

            if cantidad_tiempo <= 0:
                raise ValueError("ERROR | La duración debe ser mayor a 0")

        padecimiento = Padecimiento(id_padecimiento, nombre, tipo, tratamiento_prolongado)
        self._repo.agregar(padecimiento)
#=======================================================================================================================
    def listar(self):
        """Lista de padecimientos"""
        return self._repo.listar()
#=======================================================================================================================
    def listar_tipo(self, tipo: str):
        """Lista por tipo"""
        return self._repo.buscar_por_tipo(tipo)
#=======================================================================================================================
    def reporte_tipo(self):
        """Reporte por tipo"""
        reporte = {}
        lista = (self._repo.listar())
        for indice in lista:
            tipo = indice.tipo

            if tipo in reporte:
                reporte[tipo] += 1
            else:
                reporte[tipo] = 1
        return reporte
#=======================================================================================================================
    def reporte_tratamientos(self):
        """Reporte que indica que padecimientos no necesitan tratamiento prolongado"""
        lista_aux = []
        lista = (self._repo.listar())
        for indice in lista:
            if indice.tratamiento_prolongado != "No necesita":
                lista_aux.append(indice)
        return lista_aux
#=======================================================================================================================
    def eliminar(self, id_padecimiento: str):
        """Método que elimina un padecimiento según su id"""
        if not id_padecimiento.strip():
            raise ValueError("ERROR | el ID esta vacío")
        eliminar = self._repo.buscar_por_id(id_padecimiento)
        if not eliminar:
            raise ValueError('ERROR | no existe un padecimiento con ese id')
        self._repo.eliminar(eliminar)
#=======================================================================================================================
    def get_padecimientos_vista(self):
        """
        Retorna la lista de padecimientos con una estructura específica para que vista_pacientes la muestre en un combobox
        """
        padecimientos = []
        for p in self.listar():
            texto = f'{p.id_padecimiento} | {p.nombre}'
            padecimientos.append(texto)
        return padecimientos