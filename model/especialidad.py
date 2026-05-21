class Especialidad:
    """Entidad que representa una especialidad en el sistema"""
    def __init__(self,  id_especialidad: str, nombre: str, area_medica: str, tipo_atencion: str):
        """Constructor de la clase Especialidad"""
        self.id_especialidad = id_especialidad
        self.nombre = nombre
        self.area_medica = area_medica
        self.tipo_atencion = tipo_atencion

    def to_dict(self) -> dict:
        """Convierte el objeto en un diccionario para guardarlo en un JSON"""
        return {
            "id_especialidad": self.id_especialidad,
            "nombre": self.nombre,
            "area_medica": self.area_medica,
            "tipo_atencion": self.tipo_atencion
        }

    @classmethod # Método de clase que permite reconstruir un objeto Customer
    def from_dict(cls, data: dict):
        """Convierte un diccionario del JSON en objeto"""
        return cls(
            data['id_especialidad'],
            data['nombre'],
            data['area_medica'],
            data['tipo_atencion']
        )

    def __str__(self) -> str:
        return f"ID: {self.id_especialidad}\nNombre: {self.nombre}\nÁrea médica: {self.area_medica}\nTipo atencion: {self.tipo_atencion}"
