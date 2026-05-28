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
from model.paciente import Paciente
from model.padecimiento import Padecimiento


class RepositorioPaciente:
    """Entidad que representa el repositorio paciente donde se accede a los datos"""
    def __init__(self):
        """Constructor de la clase RepositorioPaciente, inicializa lista y la carga con los datos en el JSON"""
        self.lista = []
        self.indice_cedula = {}

        if not os.path.exists("data"):
            os.mkdir("data")

        self.archivo = "data/pacientes.json"
        self.cargar_datos()

    def cargar_datos(self):
        """Introduce los datos del JSON en la lista"""
        try:
            with open(self.archivo, "r", encoding = "utf-8") as file:
                datos = json.load(file)
                for indice in datos:
                    objeto = (Paciente.from_dict(indice))
                    self.lista.append(objeto)
                    self.indice_cedula[objeto.cedula_paciente] = objeto
        except:
            self.lista = []
            self.indice_cedula = {}

    def guardar_datos(self):
        """Sobreescribe el JSON con los datos de la lista"""
        with open(self.archivo, "w", encoding = "utf-8") as file:
            lista_diccionarios = [i.to_dict() for i in self.lista]
            json.dump(lista_diccionarios, file, indent = 4, ensure_ascii = False)

    def registrar(self, paciente: Paciente):
        """Método para registrar un paciente en el sistema"""
        self.lista.append(paciente)
        self.indice_cedula[paciente.cedula_paciente] = paciente
        self.guardar_datos()

    def listar(self):
        """Retorna el listado de pacientes"""
        return list(self.lista)

    def buscar_por_cedula(self, cedula_paciente: str):
        """Busca el padecimiento según su id usando el diccionario índice"""
        return self.indice_cedula.get(cedula_paciente)

    def consulta_por_provincia(self, provincia):
        """Retorna una lista de pacientes de la provincia indicada"""
        listado_provincia = []
        for i in self.lista:
            if i.provincia == provincia:
                listado_provincia.append(i)
        return listado_provincia

    def consulta_por_id_padecimiento(self, id_padecimiento: str):
        """Retorna una lista de pacientes que sufren del padecimiento indicado"""
        listado_padecimiento = []
        for i in self.lista:
            if i.id_padecimiento == id_padecimiento:
                listado_padecimiento.append(i)
        return listado_padecimiento

    def eliminar(self, paciente: Paciente):
        """Elimina el paciente indicado"""
        self.lista.remove(paciente)
        self.indice_cedula.pop(paciente.cedula_paciente)
        self.guardar_datos()