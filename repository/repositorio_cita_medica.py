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
from model.cita_medica import CitaMedica
#=======================================================================================================================
class RepositorioCitaMedica:
    """Clase que representa el repositorio de citas médicas donde se accede a los datos"""
#=======================================================================================================================
    def __init__(self):
        """Constructor de la clase RepositorioCitaMedica, inicializa lista y la carga con los datos en el JSON"""
        self.lista = []
        self.indice_id = {}  # llave: id_cita, valor: objeto CitaMedica

        if not os.path.exists("data"):
            os.mkdir("data")

        self.archivo = "data/citas.json"
        self.cargar_datos()
#=======================================================================================================================
    def cargar_datos(self):
        """Introduce los datos del JSON en la lista"""
        try:
            with open(self.archivo, "r", encoding="utf-8") as file:
                datos = json.load(file)
                for indice in datos:
                    objeto = CitaMedica.from_dict(indice)
                    self.lista.append(objeto)
                    self.indice_id[objeto.id_cita] = objeto
        except:
            self.lista = []
            self.indice_id = {}
#=======================================================================================================================
    def guardar_datos(self):
        """Sobreescribe el JSON con los datos de la lista"""
        with open(self.archivo, "w", encoding="utf-8") as file:
            lista_diccionarios = [i.to_dict() for i in self.lista]
            json.dump(lista_diccionarios, file, indent=4, ensure_ascii=False)
#=======================================================================================================================
    def registrar(self, cita: CitaMedica):
        """Método para registrar una cita médica en el sistema"""
        self.lista.append(cita)
        self.indice_id[cita.id_cita] = cita
        self.guardar_datos()
#=======================================================================================================================
    def listar(self):
        """Retorna el listado completo de citas"""
        return list(self.lista)
#=======================================================================================================================
    def buscar_por_id(self, id_cita: str):
        """Busca la cita según su id usando el diccionario índice"""
        return self.indice_id.get(id_cita)
#=======================================================================================================================
    def buscar_por_cedula_medico(self, cedula_medico: str):
        """Retorna una lista de citas asociadas al médico indicado"""
        return [c for c in self.lista if c.cedula_medico == cedula_medico]
#=======================================================================================================================
    def eliminar(self, cita: CitaMedica):
        """Elimina la cita indicada"""
        self.lista.remove(cita)
        self.indice_id.pop(cita.id_cita, None)
        self.guardar_datos()
