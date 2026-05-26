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
import json
import os
from model.especialidad import (Especialidad)
#=======================================================================================================================
class RepositorioEspecialidad:
    """Se crea la clase RepositorioEspecialidad"""
#=======================================================================================================================
    def __init__(self):
        """Se crea la carpeta"""
        self.lista = []
        super().__init__()
        if not os.path.exists("data"):
            os.mkdir("data")

        self.archivo = ("data/especialidades.json")
        self.cargar_datos()
#=======================================================================================================================
    def agregar(self, especialidad: Especialidad):
        """Agrega una especialidad en la carpeta"""
        self.lista.append(especialidad)
        self.guardar_datos()
#=======================================================================================================================
    def consultar(self):
        """Consulta una especialidad en la carpeta"""
        return self.lista
#=======================================================================================================================
    def guardar_datos(self):
        """Guarda los datos de especialidad"""
        lista_diccionarios = []
        for indice in self.lista:
            lista_diccionarios.append(indice.to_dict())

        with open(self.archivo, "w", encoding = "utf-8") as file:
            json.dump(lista_diccionarios, file, indent = 4, ensure_ascii = False)
#=======================================================================================================================
    def cargar_datos(self):
        """Carga los datos de especialidad"""
        try:
            with open(self.archivo, "r", encoding = "utf-8") as file:
                datos = json.load(file)
                for indice in datos:
                    objeto = (Especialidad.from_dict(indice))
                    self.lista.append(objeto)
        except:
            self.lista = []
#=======================================================================================================================
    def buscar_tipo(self, tipo: str):
        """Busca el tipo de atención"""
        lista_aux = []
        for indice in self.lista:
            if (indice._tipo_atencion.lower() == tipo.lower()):
                lista_aux.append(indice)
        return lista_aux
#=======================================================================================================================
    def buscar_id(self, id_especialidad: str):
        """Busca el id de especialidad"""
        for indice in self.lista:
            if (indice._id_especialidad == id_especialidad):
                return indice
        return None
#=======================================================================================================================