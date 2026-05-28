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
class ControladorMedico:
    """Se crea la clase ControladorMedico"""
#=======================================================================================================================
    def __init__(self, vista, servicio):
        """Constructor que inicializa las instancias"""
        self._vista = vista
        self._servicio = servicio
        self._vista.btn_registrar.config(command=self.registrar)
        self._vista.btn_buscar.config(command=self.buscar_por_cedula)
        self._vista.btn_eliminar.config(command=self.eliminar)
        self._vista.btn_listar.config(command=self.listar)
        self._vista.btn_consulta_provincia.config(command=self.consulta_provincia)
        self._vista.btn_consulta_especialidades.config(command=self.consulta_especialidad)
        self.cargar_tabla()
#=======================================================================================================================
    def registrar(self):
        """Registra las Medicoes"""
        try:
            datos = (self._vista.obtener_datos())
            self._servicio.registrar(
                datos[0],
                datos[1],
                datos[2],
                datos[3],
                datos[4],
                datos[5]
            )

            self._vista.mostrar_info('info', 'Registro exitoso')
            self.cargar_tabla()
        except Exception as error:
            self._vista.mostrar_info('error', str(error))
#=======================================================================================================================
    def cargar_tabla(self):
        """Carga la tabla"""
        datos = self._servicio.listar()
        self._vista.cargar_tabla(datos)
#=======================================================================================================================
    def buscar_por_cedula(self):
        """Buscar por cedula"""
        try:
            cedula = self._vista.obtener_cedula()
            medico = self._servicio.buscar_por_cedula(cedula)
            self._vista.cargar_tabla(medico)
        except Exception as error:
            self._vista.mostrar_info('error', str(error))
#=======================================================================================================================
    def listar(self):
        """Llena a cargar tabla para llenarla con los datos almacenados"""
        lista = self._servicio.listar()
        self._vista.cargar_tabla(lista)
#=======================================================================================================================
    def eliminar(self):
        """Cuando presiona eliminar llama a este método"""
        try:
            cedula = self._vista.obtener_cedula()
            self._servicio.eliminar(cedula)
            self._vista.mostrar_info('info', 'El Medico ha sido eliminado')
            lista = self._servicio.get_lista_vista()
            self._vista.cargar_tabla(lista)
        except Exception as error:
            self._vista.mostrar_info('error', str(error))

#=======================================================================================================================
    def consulta_provincia(self):
        """Ejecuta las acciones de consulta provincia"""
        try:
            provincia = self._vista.obtener_provincia()
            lista = self._servicio.consulta_por_provincia(provincia)
            self._vista.cargar_tabla(lista)
        except Exception as error:
            self._vista.mostrar_info('error', str(error))
#=======================================================================================================================
    def consulta_especialidad(self):
        """Ejecuta las acciones de consulta especialidad"""
        try:
            especialidad = self._vista.obtener_especialidad()
            lista = self._servicio.consulta_por_especialidad(especialidad)
            self._vista.cargar_tabla(lista)
        except Exception as error:
            self._vista.mostrar_info('error', str(error))