"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
from utils.constantes import meses_30_dias, meses_31_dias

#=======================================================================================================================
"""Se crean las importaciones"""
from model.cita_medica import CitaMedica
from model.cita_medica_dto import CitaMedicaVistaDTO
from repository.repositorio_cita_medica import RepositorioCitaMedica
from repository.repositorio_paciente import RepositorioPaciente
from repository.repositorio_medico import RepositorioMedico
#=======================================================================================================================
class ServicioCitaMedica:
    """Clase que representa el servicio de citas médicas, se encarga de realizar validaciones de negocio"""
#=======================================================================================================================
    def __init__(self, repo_citas: RepositorioCitaMedica, repo_pacientes: RepositorioPaciente,
                 repo_medicos: RepositorioMedico):
        """Constructor, inicializa los repositorios necesarios"""
        self._repo_citas = repo_citas
        self._repo_pacientes = repo_pacientes
        self._repo_medicos = repo_medicos
#=======================================================================================================================
    def registrar(self, id_cita: str, cedula_paciente: str, cedula_medico: str,
                  dia: str, mes: str, anio: str, motivo: str):
        """Realiza validaciones antes de llamar al repositorio"""
        # Limpia espacios
        id_cita = id_cita.strip()
        cedula_paciente = cedula_paciente.strip()
        cedula_medico = cedula_medico.strip()
        dia = dia.strip()
        motivo = motivo.strip()

        # Campos obligatorios
        if not id_cita or not cedula_paciente or not cedula_medico or not dia or not mes or not anio or not motivo:
            raise ValueError('ERROR | No pueden haber campos vacíos')

        # ID único
        if self._repo_citas.buscar_por_id(id_cita) is not None:
            raise ValueError('ERROR | Ya existe una cita con ese ID')

        # Paciente existe
        if self._repo_pacientes.buscar_por_cedula(cedula_paciente) is None:
            raise ValueError('ERROR | No existe un paciente con esa cédula')

        # Médico existe
        if self._repo_medicos.buscar_por_cedula(cedula_medico) is None:
            raise ValueError('ERROR | No existe un médico con esa cédula')

        fecha = f"{dia.zfill(2)}/{mes}/{anio}"
        self._validar_fecha(cedula_paciente, cedula_medico, fecha)
        cita = CitaMedica(id_cita, cedula_paciente, cedula_medico, fecha, motivo)
        self._repo_citas.registrar(cita)
#=======================================================================================================================
    def buscar_por_id(self, id_cita: str):
        """Busca una cita por su ID y retorna un DTO listo para la vista"""
        id_cita = id_cita.strip()
        if not id_cita:
            raise ValueError('ERROR | El campo ID está vacío')

        cita = self._repo_citas.buscar_por_id(id_cita)
        if cita is None:
            raise ValueError('ERROR | No existe una cita con ese ID')

        return self._a_dto(cita)
#=======================================================================================================================
    def listar(self):
        """Devuelve la lista completa de citas como DTOs"""
        return [self._a_dto(c) for c in self._repo_citas.listar()]
#=======================================================================================================================
    def buscar_por_cedula_medico(self, cedula_medico: str):
        """Retorna todas las citas de un médico como DTOs"""
        cedula_medico = cedula_medico.strip()
        if not cedula_medico:
            raise ValueError('ERROR | El campo de cédula del médico está vacío')
        if self._repo_medicos.buscar_por_cedula(cedula_medico) is None:
            raise ValueError('ERROR | No existe un médico con esa cédula')

        lista = self._repo_citas.buscar_por_cedula_medico(cedula_medico)
        return [self._a_dto(c) for c in lista]
#=======================================================================================================================
    def eliminar(self, id_cita: str):
        """Elimina la cita con el ID indicado"""
        id_cita = id_cita.strip()
        if not id_cita:
            raise ValueError('ERROR | El campo ID está vacío')

        cita = self._repo_citas.buscar_por_id(id_cita)
        if cita is None:
            raise ValueError('ERROR | No existe una cita con ese ID')

        self._repo_citas.eliminar(cita)
#=======================================================================================================================
    def _a_dto(self, cita: CitaMedica) -> CitaMedicaVistaDTO:
        """Convierte un objeto CitaMedica a CitaMedicaVistaDTO para la vista"""
        paciente = self._repo_pacientes.buscar_por_cedula(cita.cedula_paciente)
        medico = self._repo_medicos.buscar_por_cedula(cita.cedula_medico)

        nombre_paciente = paciente.nombre if paciente else cita.cedula_paciente
        nombre_medico = medico.nombre if medico else cita.cedula_medico

        return CitaMedicaVistaDTO(
            cita.id_cita,
            nombre_paciente,
            nombre_medico,
            cita.fecha,
            cita.motivo
        )
#=======================================================================================================================
    def _validar_fecha(self, cedula_paciente: str, cedula_medico: str, fecha: str):
        """Valida que la fecha sea correcta"""
        dia, mes, anio = fecha.split('/')
        try:
            dia = int(dia)
        except ValueError:
            raise ValueError('ERROR | El día debe ser un número entero')

        # Valida que el día no sea incorrecto
        if mes in meses_30_dias:
            max_dias = 30
        elif mes in meses_31_dias:
            max_dias = 31
        else:
            if anio == '2028':
                max_dias = 29
            else:
                max_dias = 28

        if dia not in range(1, max_dias + 1):
            raise ValueError(f'ERROR| El día {dia} está fuera del rango permitido (1-{max_dias}, mes: {mes})')

        lista = self._repo_citas.listar()
        for cita in lista:
            if cita.cedula_paciente == cedula_paciente and cita.fecha == fecha:
                raise ValueError(
                    f'ERROR | El paciente con cédula {cedula_paciente} ya tiene una cita asignada para la fecha {fecha}'
                    '\nNo puede registrar dos citas en el mismo día para un mismo paciente\n'
                )
            if cita.cedula_medico == cedula_medico and cita.fecha == fecha:
                raise ValueError(
                    f'ERROR | El médico con cédula {cedula_medico} ya tiene una cita asignada para la fecha {fecha}'
                    '\nNo puede registrar dos citas en el mismo día para un mismo médico\n'
                )