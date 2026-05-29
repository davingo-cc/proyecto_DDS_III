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
class ControladorCitaMedica:
    """Se crea la clase ControladorCitaMedica"""
#=======================================================================================================================
    def __init__(self, vista, servicio):
        """Constructor que inicializa las instancias y conecta los botones"""
        self._vista = vista
        self._servicio = servicio
        self._vista.btn_registrar.config(command=self.registrar)
        self._vista.btn_buscar.config(command=self.buscar_por_id)
        self._vista.btn_eliminar.config(command=self.eliminar)
        self._vista.btn_listar.config(command=self.listar)
        self._vista.btn_consulta_medico.config(command=self.consulta_por_medico)
        self.cargar_tabla()
#=======================================================================================================================
    def registrar(self):
        """Registra una nueva cita médica"""
        try:
            datos = self._vista.obtener_datos()
            self._servicio.registrar(
                datos[0],  # id_cita
                datos[1],  # cedula_paciente
                datos[2],  # cedula_medico
                datos[3],  # dia
                datos[4],  # mes
                datos[5],  # anio
                datos[6]   # motivo
            )
            self._vista.mostrar_info('info', 'Cita registrada exitosamente')
            self._vista.limpiar_campos()
            self.cargar_tabla()
        except Exception as error:
            self._vista.mostrar_info('error', str(error))
#=======================================================================================================================
    def cargar_tabla(self):
        """Carga la tabla con todas las citas"""
        datos = self._servicio.listar()
        self._vista.cargar_tabla(datos)
#=======================================================================================================================
    def buscar_por_id(self):
        """Busca una cita por su ID y la muestra en la tabla"""
        try:
            id_cita = self._vista.obtener_id()
            dto = self._servicio.buscar_por_id(id_cita)
            self._vista.cargar_tabla_solo_uno(dto)
        except Exception as error:
            self._vista.mostrar_info('error', str(error))
#=======================================================================================================================
    def listar(self):
        """Lista todas las citas en la tabla"""
        lista = self._servicio.listar()
        self._vista.cargar_tabla(lista)
#=======================================================================================================================
    def eliminar(self):
        """Elimina la cita con el ID ingresado"""
        try:
            id_cita = self._vista.obtener_id()
            self._servicio.eliminar(id_cita)
            self._vista.mostrar_info('info', 'La cita ha sido eliminada')
            self._vista.limpiar_campos()
            self.cargar_tabla()
        except Exception as error:
            self._vista.mostrar_info('error', str(error))
#=======================================================================================================================
    def consulta_por_medico(self):
        """Muestra todas las citas del médico ingresado"""
        try:
            cedula_medico = self._vista.obtener_cedula_medico()
            lista = self._servicio.buscar_por_cedula_medico(cedula_medico)
            self._vista.cargar_tabla(lista)
        except Exception as error:
            self._vista.mostrar_info('error', str(error))
