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
from collections import Counter
from repository.repositorio_cita_medica import RepositorioCitaMedica
from repository.repositorio_paciente import RepositorioPaciente
from repository.repositorio_medico import RepositorioMedico
from repository.repositorio_especialidad import RepositorioEspecialidad
from repository.repositorio_padecimiento import RepositorioPadecimiento
#=======================================================================================================================
class ReporteTop3DTO:
    """DTO para el reporte 1: Top 3 pacientes con más citas"""
    def __init__(self, posicion: int, cedula: str, nombre: str, total_citas: int):
        self.posicion = posicion
        self.cedula = cedula
        self.nombre = nombre
        self.total_citas = total_citas
#=======================================================================================================================
class ReportePadecimientoProvinciaDTO:
    """DTO para el reporte 2: Padecimiento más frecuente por provincia"""
    def __init__(self, provincia: str, padecimiento: str, cantidad: int):
        self.provincia = provincia
        self.padecimiento = padecimiento
        self.cantidad = cantidad
#=======================================================================================================================
class ReporteEspecialidadDTO:
    """DTO para el reporte 3: Especialidad más demandada"""
    def __init__(self, especialidad: str, area: str, total_citas: int):
        self.especialidad = especialidad
        self.area = area
        self.total_citas = total_citas
#=======================================================================================================================
class ServicioReportes:
    """Clase que genera los reportes del sistema clínico"""
#=======================================================================================================================
    def __init__(self, repo_citas: RepositorioCitaMedica, repo_pacientes: RepositorioPaciente,
                 repo_medicos: RepositorioMedico, repo_especialidades: RepositorioEspecialidad,
                 repo_padecimientos: RepositorioPadecimiento):
        """Constructor, inicializa los repositorios necesarios"""
        self._repo_citas = repo_citas
        self._repo_pacientes = repo_pacientes
        self._repo_medicos = repo_medicos
        self._repo_especialidades = repo_especialidades
        self._repo_padecimientos = repo_padecimientos
#=======================================================================================================================
    def reporte_top3_pacientes(self):
        """
        Reporte 1: Top 3 pacientes con mayor cantidad de citas registradas.
        Cuenta las apariciones de cada cédula de paciente en las citas.
        """
        citas = self._repo_citas.listar()
        if not citas:
            raise ValueError('ERROR | No hay citas registradas para generar el reporte')

        conteo = Counter(c.cedula_paciente for c in citas)
        # Ordenar de mayor a menor, tomar los 3 primeros
        top3 = conteo.most_common(3)

        resultado = []
        for posicion, (cedula, total) in enumerate(top3, start=1):
            paciente = self._repo_pacientes.buscar_por_cedula(cedula)
            nombre = paciente.nombre if paciente else f'Cédula: {cedula}'
            resultado.append(ReporteTop3DTO(posicion, cedula, nombre, total))

        return resultado
#=======================================================================================================================
    def reporte_padecimiento_por_provincia(self):
        """
        Reporte 2: Padecimiento más frecuente por cada provincia.
        Por cada provincia, determina cuál padecimiento tienen más pacientes.
        """
        pacientes = self._repo_pacientes.listar()
        if not pacientes:
            raise ValueError('ERROR | No hay pacientes registrados para generar el reporte')

        from utils.constantes import provincias
        resultado = []

        for provincia in provincias:
            # Pacientes de esta provincia
            pacientes_provincia = [p for p in pacientes if p.provincia == provincia]
            if not pacientes_provincia:
                continue

            # Contar padecimientos
            conteo = Counter(p.id_padecimiento for p in pacientes_provincia)
            id_padecimiento_mas_frecuente, cantidad = conteo.most_common(1)[0]

            padecimiento = self._repo_padecimientos.buscar_por_id(id_padecimiento_mas_frecuente)
            nombre_padecimiento = padecimiento.nombre if padecimiento else f'ID: {id_padecimiento_mas_frecuente}'

            resultado.append(ReportePadecimientoProvinciaDTO(provincia, nombre_padecimiento, cantidad))

        if not resultado:
            raise ValueError('ERROR | No hay datos suficientes para generar el reporte')

        return resultado
#=======================================================================================================================
    def reporte_especialidad_mas_demandada(self):
        """
        Reporte 3: Especialidades ordenadas por demanda (cantidad de citas).
        Cada cita se asocia al médico y de ahí a su especialidad.
        """
        citas = self._repo_citas.listar()
        if not citas:
            raise ValueError('ERROR | No hay citas registradas para generar el reporte')

        # Contar cuántas citas tiene cada especialidad a través del médico
        conteo_especialidad = Counter()
        for cita in citas:
            medico = self._repo_medicos.buscar_por_cedula(cita.cedula_medico)
            if medico:
                conteo_especialidad[medico.id_especialidad] += 1

        if not conteo_especialidad:
            raise ValueError('ERROR | No se pudo asociar ninguna cita a una especialidad')

        resultado = []
        for id_esp, total in conteo_especialidad.most_common():
            especialidad = self._repo_especialidades.buscar_por_id(id_esp)
            if especialidad:
                resultado.append(ReporteEspecialidadDTO(
                    especialidad.nombre,
                    especialidad.area_medica,
                    total
                ))

        return resultado
