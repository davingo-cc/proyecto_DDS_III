"""
Desarrollo de Software III
Proyecto # 1
-Sistema de gestión de una clinica
Integrantes:
-David Chang Castañeda
-Enzo Bejarano
-Windell Urroz Costés
"""
from view.vista_reportes import VistaReportes


#=======================================================================================================================
class ControladorReportes:
    """Se crea la clase ControladorReportes"""
#=======================================================================================================================
    def __init__(self, vista: VistaReportes, servicio):
        """Constructor que inicializa las instancias y conecta los botones"""
        self._vista = vista
        self._servicio = servicio
        self._vista.btn_reporte1.config(command=self.generar_reporte1)
        self._vista.btn_reporte2.config(command=self.generar_reporte2)
        self._vista.btn_reporte3.config(command=self.generar_reporte3)
#=======================================================================================================================
    def generar_reporte1(self):
        """Genera el reporte Top 3 pacientes con más citas"""
        try:
            lista = self._servicio.reporte_top3_pacientes()
            self._vista.cargar_reporte1(lista)
        except Exception as error:
            self._vista.mostrar_info('error', str(error))
            self._vista.limpiar_reporte1()
#=======================================================================================================================
    def generar_reporte2(self):
        """Genera el reporte de padecimiento más frecuente por provincia"""
        try:
            lista = self._servicio.reporte_padecimiento_por_provincia()
            self._vista.cargar_reporte2(lista)
        except Exception as error:
            self._vista.mostrar_info('error', str(error))
            self._vista.limpiar_reporte2()
#=======================================================================================================================
    def generar_reporte3(self):
        """Genera el reporte de especialidades más demandadas"""
        try:
            lista = self._servicio.reporte_especialidad_mas_demandada()
            self._vista.cargar_reporte3(lista)
        except Exception as error:
            self._vista.mostrar_info('error', str(error))
            self._vista.limpiar_reporte3()
