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
from model.padecimiento import (Padecimiento)
#=======================================================================================================================
class RepositorioPadecimiento:
    """Se crea la clase RepositorioPadecimiento"""
#=======================================================================================================================
    def __init__(self):
        """Se crea la carpeta"""
        self.lista = []
        self.indice_id = {}  # llave: id_padecimiento, valor: objeto Padecimiento
        super().__init__()

        if not os.path.exists("data"):
            os.mkdir("data")

        self.archivo = "data/padecimientos.json"
        self.cargar_datos()
#=======================================================================================================================
    def agregar(self, padecimiento: Padecimiento):
        """Agrega un padecimiento en la carpeta"""
        self.lista.append(padecimiento)
        self.indice_id[padecimiento.id_padecimiento] = padecimiento
        self.guardar_datos()
#=======================================================================================================================
    def listar(self):
        """Retorna la lista de padecimientos"""
        return self.lista
#=======================================================================================================================
    def guardar_datos(self):
        lista_diccionarios = []
        for indice in self.lista:
            lista_diccionarios.append(indice.to_dict())

        with open(self.archivo, "w", encoding = "utf-8") as file:
            json.dump(lista_diccionarios, file, indent = 4, ensure_ascii = False)
#=======================================================================================================================
    def cargar_datos(self):
        """Carga los datos del padecimiento"""
        try:
            with open(self.archivo, "r", encoding = "utf-8") as file:
                datos = json.load(file)
                for indice in datos:
                    objeto = Padecimiento.from_dict(indice)
                    self.lista.append(objeto)
                    self.indice_id[objeto.id_padecimiento] = objeto
        except:
            self.lista = []
            self.indice_id = {}
#=======================================================================================================================
    def buscar_por_tipo(self, tipo: str):
        """Busca el tipo de un padecimiento"""
        lista_aux = []
        for indice in self.lista:
            if indice.tipo.lower() == tipo.lower():
                lista_aux.append(indice)
        return lista_aux
#=======================================================================================================================
    def buscar_por_id(self, id_padecimiento: str):
        """Busca el padecimiento según su id usando el diccionario índice"""
        return self.indice_id.get(id_padecimiento)
#=======================================================================================================================
    def eliminar(self, eliminar: Padecimiento):
        """Elimina el padecimiento con el id indicado"""
        for indice in self.lista:
            if indice == eliminar:
                self.lista.remove(indice)
                self.indice_id.pop(eliminar.id_padecimiento)
        self.guardar_datos()