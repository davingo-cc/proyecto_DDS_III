"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
import json
import os
from model.medico import Medico
from model.especialidad import Especialidad


class RepositorioMedico:
    """Entidad que representa el repositorio medico donde se accede a los datos"""
    def __init__(self):
        """Constructor de la clase RepositorioMedico, inicializa lista y la carga con los datos en el JSON"""
        self.lista = []
        self.indice_cedula = {}

        if not os.path.exists("data"):
            os.mkdir("data")

        self.archivo = "data/medicos.json"
        self.cargar_datos()

    def cargar_datos(self):
        """Introduce los datos del JSON en la lista"""
        try:
            with open(self.archivo, "r", encoding = "utf-8") as file:
                datos = json.load(file)
                for indice in datos:
                    objeto = (Medico.from_dict(indice))
                    self.lista.append(objeto)
                    self.indice_cedula[objeto.cedula_medico] = objeto
        except:
            self.lista = []
            self.indice_cedula = {}

    def guardar_datos(self):
        """Sobreescribe el JSON con los datos de la lista"""
        with open(self.archivo, "w", encoding = "utf-8") as file:
            lista_diccionarios = [i.to_dict() for i in self.lista]
            json.dump(lista_diccionarios, file, indent = 4, ensure_ascii = False)

    def registrar(self, medico: Medico):
        """Método para registrar un medico en el sistema"""
        self.lista.append(medico)
        self.indice_cedula[medico.cedula_medico] = medico
        self.guardar_datos()

    def listar(self):
        """Retorna el listado de medicos"""
        return list(self.lista)

    def buscar_por_cedula(self, cedula_medico: str):
        """Busca el especialidad según su id usando el diccionario índice"""
        return self.indice_cedula.get(cedula_medico)

    def consulta_por_provincia(self, provincia):
        """Retorna una lista de medicos de la provincia indicada"""
        listado_provincia = []
        for i in self.lista:
            if i.provincia == provincia:
                listado_provincia.append(i)
        return listado_provincia

    def consulta_por_id_especialidad(self, id_especialidad: str):
        """Retorna una lista de medicos que sufren del especialidad indicado"""
        listado_especialidad = []
        for i in self.lista:
            if i.id_especialidad == id_especialidad:
                listado_especialidad.append(i)
        return listado_especialidad

    def eliminar(self, medico: Medico):
        """Elimina el medico indicado"""
        self.lista.remove(medico)
        self.indice_cedula.pop(medico.cedula_medico)
        self.guardar_datos()