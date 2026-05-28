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
class ControladorEspecialidad:
    """Se crea la clase ControladorEspecialidad"""
#=======================================================================================================================
    def __init__(self, vista, servicio):
        """Constructor que inicializa las instancias"""
        self._vista = vista
        self._servicio = servicio
        self._vista.btn_registrar.config(command = self.registrar)
        self._vista.btn_buscar.config(command = self.buscar_tipo)
        self._vista.btn_reporte.config(command = self.reporte_tipo)
        self._vista.btn_eliminar.config(command = self.eliminar)
        self._vista.btn_listar.config(command = self.listar)
        self.cargar_tabla()
#=======================================================================================================================
    def registrar(self):
        """Registra las especialidades"""
        try:
            datos = (self._vista.obtener_datos())
            self._servicio.para_registrar(
                datos[0],
                datos[1],
                datos[2],
                datos[3]
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
    def buscar_tipo(self):
        """Buscar por tipo"""
        tipo = (self._vista.combo_buscar.get())
        datos = (self._servicio.listar_tipo(tipo))
        self._vista.cargar_tabla(datos)
#=======================================================================================================================
    def reporte_tipo(self):
        """Reporte de tipo"""
        datos = (self._servicio.reporte_tipo())
        texto = ""
        for clave, valor in datos.items():
            texto += (
                f"{clave}: {valor}\n"
            )
        self._vista.mostrar_info('info', texto)
#=======================================================================================================================
    def eliminar(self):
        """Cuando presiona eliminar llama a este método"""
        lista = self._servicio.listar()
        try:
            id_especialidad = self._vista.obtener_id()
            self._servicio.eliminar(id_especialidad)
            self._vista.cargar_tabla(lista)
        except Exception as error:
            self._vista.mostrar_info('error', str(error))
            self._vista.limpiar_campos()
#=======================================================================================================================
    def listar(self):
        """Carga la tabla con los datos de los padecimientos"""
        lista = self._servicio.listar()
        self._vista.cargar_tabla(lista)