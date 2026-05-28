"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
from model.medico import Medico
from model.medico_dto import MedicoVistaDTO
from repository.repositorio_medico import RepositorioMedico
from repository.repositorio_especialidad import RepositorioEspecialidad


class ServicioMedico:
    """Clase que representa el servicio medico, se encarga de realizar validaciones de negocio"""
    def __init__(self, repo_medicos: RepositorioMedico, repo_especialidades: RepositorioEspecialidad):
        """Constructor, inicializa el repositorio"""
        self._repo_medicos = repo_medicos
        self._repo_especialidades = repo_especialidades

    def registrar(self, cedula_medico: str, nombre: str, telefono: str, correo: str, provincia: str, id_especialidad: str):
        """
        Realiza validaciones antes de llamar a repositorio
        """
        # Valida que existan especialidades primero
        if not self._repo_especialidades.listar():
            raise ValueError('ERROR | No se puede registrar debido a que no hay especialidades almacenados')

        # Quita espacios vacíos para las validaciones, no se necesita hacer esto con provincia debido a
        # que no son valores ingresados por el usuario
        cedula_medico, nombre, telefono, correo, id_especialidad = (
            cedula_medico.strip(), nombre.strip(), telefono.strip(), correo.strip(), id_especialidad.strip()
        )
        if (not cedula_medico or
            not nombre or
            not telefono or
            not correo or
            not provincia or
            not id_especialidad
        ):
            raise ValueError('ERROR | No pueden haber campos vacíos')

        # Valida que cédula, correo y especialidad sean válidos
        if self._repo_medicos.buscar_por_cedula(cedula_medico) is not None:
            raise ValueError('ERROR | Ya existe un medico con esa cédula')
        if '@' not in correo or '.' not in correo:
            raise ValueError('ERROR | Correo con credenciales inválidas')
        if self._repo_especialidades.buscar_por_id(id_especialidad) is None:
            raise ValueError('ERROR | No existe un especialidad con ese ID')

        medico = Medico(cedula_medico, nombre, telefono, correo, provincia, id_especialidad)
        self._repo_medicos.registrar(medico)

    def buscar_por_cedula(self, cedula_medico: str):
        """Llama a buscar por cedula en el repo, también realiza validaciones"""
        cedula_medico = cedula_medico.strip()
        if not cedula_medico:
            raise ValueError('ERROR | El campo de cédula esta vacío')

        medico = self._repo_medicos.buscar_por_cedula(cedula_medico)
        if medico is None:
            raise ValueError('ERROR | El medico indicado no existe')
        return MedicoVistaDTO(
            medico.cedula_medico,
            medico.nombre,
            medico.telefono,
            medico.correo,
            medico.provincia,
            self._repo_especialidades.buscar_por_id(medico.id_especialidad).nombre
        )

    def listar(self):
        """Devuelve una lista completa de todos los medicos para mostrar en la vista"""
        lista = self._repo_medicos.listar()
        return self.get_lista_vista(lista)

    def consulta_por_especialidad(self, id_especialidad: str):
        """Valida que especialidad no esté vacío y que exista antes de retornar la lista"""
        id_especialidad = id_especialidad.strip()
        # No seleccionó nada
        if not id_especialidad:
            raise ValueError('ERROR | Debe ingresar un ID de un especialidad')
        # No existe
        if self._repo_especialidades.buscar_por_id(id_especialidad) is None:
            raise ValueError('ERROR | No existe un especialidad con ese ID')

        lista = self._repo_medicos.consulta_por_id_especialidad(id_especialidad)
        return self.get_lista_vista(lista)

    def consulta_por_provincia(self, provincia: str):
        """Usa un combobox igual al que se usa para registrar, realiza validaciones"""
        # No seleccionó nada
        if not provincia:
            raise ValueError('ERROR | Debe seleccionar una provincia')
        lista = self._repo_medicos.consulta_por_provincia(provincia)
        return self.get_lista_vista(lista)

    def eliminar(self, cedula_medico: str):
        """Llama a eliminar por cedula en el repo, también realiza validaciones"""
        cedula_medico = cedula_medico.strip()
        if not cedula_medico:
            raise ValueError('ERROR | El campo de cédula esta vacío')

        medico = self._repo_medicos.buscar_por_cedula(cedula_medico)
        if medico is None:
            raise ValueError('ERROR | El medico indicado no existe')
        self._repo_medicos.eliminar(medico)

    def get_lista_vista(self, lista):
        """
        Convierte la lista parámetro en una lista de DTOs listos para mostrar en la tabla.
        Se usa MedicoVistaDTO para evitar que la vista acceda directamente a objetos
        complejos como especialidad, manteniendo bajo acoplamiento entre capas.
        """
        return [
            MedicoVistaDTO(
                p.cedula_medico,
                p.nombre,
                p.telefono,
                p.correo,
                p.provincia,
                self._repo_especialidades.buscar_por_id(p.id_especialidad).nombre
            )
            for p in lista
        ]