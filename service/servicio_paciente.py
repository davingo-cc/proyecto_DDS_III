"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
from model.paciente import Paciente
from model.paciente_dto import PacienteVistaDTO
from repository.repositorio_paciente import RepositorioPaciente
from repository.repositorio_padecimiento import RepositorioPadecimiento


class ServicioPaciente:
    """Clase que representa el servicio paciente, se encarga de realizar validaciones de negocio"""
    def __init__(self, repo_pacientes: RepositorioPaciente, repo_padecimientos: RepositorioPadecimiento):
        """Constructor, inicializa el repositorio"""
        self._repo_pacientes = repo_pacientes
        self._repo_padecimientos = repo_padecimientos

    def registrar(self, cedula_paciente: str, nombre: str, telefono: str, correo: str, provincia: str, id_padecimiento: str):
        """
        Realiza validaciones antes de llamar a repositorio
        """
        # Valida que existan padecimientos primero
        if not self._repo_padecimientos.listar():
            raise ValueError('ERROR | No se puede registrar debido a que no hay padecimientos almacenados')

        # Quita espacios vacíos para las validaciones, no se necesita hacer esto con provincia debido a
        # que no son valores ingresados por el usuario
        cedula_paciente, nombre, telefono, correo, id_padecimiento = (
            cedula_paciente.strip(), nombre.strip(), telefono.strip(), correo.strip(), id_padecimiento.strip()
        )
        if (not cedula_paciente or
            not nombre or
            not telefono or
            not correo or
            not provincia or
            not id_padecimiento
        ):
            raise ValueError('ERROR | No pueden haber campos vacíos')

        # Valida que cédula, correo y padecimiento sean válidos
        if self._repo_pacientes.buscar_por_cedula(cedula_paciente) is not None:
            raise ValueError('ERROR | Ya existe un paciente con esa cédula')
        if '@' not in correo or '.' not in correo:
            raise ValueError('ERROR | Correo con credenciales inválidas')
        if self._repo_padecimientos.buscar_por_id(id_padecimiento) is None:
            raise ValueError('ERROR | No existe un padecimiento con ese ID')

        paciente = Paciente(cedula_paciente, nombre, telefono, correo, provincia, id_padecimiento)
        self._repo_pacientes.registrar(paciente)

    def buscar_por_cedula(self, cedula_paciente: str):
        """Llama a buscar por cedula en el repo, también realiza validaciones"""
        cedula_paciente = cedula_paciente.strip()
        if not cedula_paciente:
            raise ValueError('ERROR | El campo de cédula esta vacío')

        paciente = self._repo_pacientes.buscar_por_cedula(cedula_paciente)
        if paciente is None:
            raise ValueError('ERROR | El paciente indicado no existe')
        return PacienteVistaDTO(
            paciente.cedula_paciente,
            paciente.nombre,
            paciente.telefono,
            paciente.correo,
            paciente.provincia,
            self._repo_padecimientos.buscar_por_id(paciente.id_padecimiento).nombre
        )

    def listar(self):
        """Devuelve una lista completa de todos los pacientes para mostrar en la vista"""
        lista = self._repo_pacientes.listar()
        return self.get_lista_vista(lista)

    def consulta_por_padecimiento(self, id_padecimiento: str):
        """Valida que padecimiento no esté vacío y que exista antes de retornar la lista"""
        id_padecimiento = id_padecimiento.strip()
        # No seleccionó nada
        if not id_padecimiento:
            raise ValueError('ERROR | Debe ingresar un ID de un padecimiento')
        # No existe
        if self._repo_padecimientos.buscar_por_id(id_padecimiento) is None:
            raise ValueError('ERROR | No existe un padecimiento con ese ID')

        lista = self._repo_pacientes.consulta_por_id_padecimiento(id_padecimiento)
        return self.get_lista_vista(lista)

    def consulta_por_provincia(self, provincia: str):
        """Usa un combobox igual al que se usa para registrar, realiza validaciones"""
        # No seleccionó nada
        if not provincia:
            raise ValueError('ERROR | Debe seleccionar una provincia')
        lista = self._repo_pacientes.consulta_por_provincia(provincia)
        return self.get_lista_vista(lista)

    def eliminar(self, cedula_paciente: str):
        """Llama a eliminar por cedula en el repo, también realiza validaciones"""
        cedula_paciente = cedula_paciente.strip()
        if not cedula_paciente:
            raise ValueError('ERROR | El campo de cédula esta vacío')

        paciente = self._repo_pacientes.buscar_por_cedula(cedula_paciente)
        if paciente is None:
            raise ValueError('ERROR | El paciente indicado no existe')
        self._repo_pacientes.eliminar(paciente)

    def get_lista_vista(self, lista):
        """
        Convierte la lista parámetro en una lista de DTOs listos para mostrar en la tabla.
        Se usa PacienteVistaDTO para evitar que la vista acceda directamente a objetos
        complejos como padecimiento, manteniendo bajo acoplamiento entre capas.
        """
        return [
            PacienteVistaDTO(
                p.cedula_paciente,
                p.nombre,
                p.telefono,
                p.correo,
                p.provincia,
                self._repo_padecimientos.buscar_por_id(p.id_padecimiento).nombre
            )
            for p in lista
        ]