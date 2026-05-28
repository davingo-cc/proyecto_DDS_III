# Sistema de Gestión de Clínica Comunitaria

Proyecto programado — Desarrollo de Software III  
Universidad de Costa Rica, Sede Regional del Pacífico  
Bach. Informática Empresarial

**Integrantes:**
- David Chang Castañeda
- Enzo Bejarano
- Windell Urroz Costés

---

## Descripción

Sistema de escritorio desarrollado en Python con interfaz gráfica (tkinter) para la gestión de una clínica comunitaria. Permite administrar especialidades médicas, padecimientos, pacientes, médicos y citas médicas, con persistencia de datos en archivos JSON.

El sistema fue diseñado con arquitectura MVC, principios SOLID y uso explícito de estructuras de datos (listas, diccionarios, conjuntos y tuplas), como parte de los requerimientos del curso Desarrollo de Software III.

---

## Módulos del sistema

| Módulo | Descripción |
|---|---|
| Especialidades | Registro, consulta, filtrado y eliminación de especialidades médicas |
| Padecimientos | Registro de padecimientos con soporte para tratamiento prolongado |
| Pacientes | Gestión de pacientes vinculados a un padecimiento |
| Médicos | Gestión de médicos vinculados a una especialidad |
| Citas médicas | Registro de citas entre pacientes y médicos con fecha y motivo |
| Reportes | Reportes cruzados: top pacientes, padecimiento por provincia, especialidad más demandada |

---

## Arquitectura

El sistema sigue la arquitectura **MVC extendida** con cinco capas bien definidas:

```
proyecto_DDS_III/
│
├── model/          → Entidades del dominio y DTOs
├── repository/     → Acceso a datos y persistencia JSON
├── service/        → Lógica de negocio y validaciones
├── controller/     → Coordinación entre vista y servicio
├── view/           → Interfaz gráfica modular (tkinter)
├── utils/          → Constantes compartidas
├── data/           → Archivos JSON generados automáticamente
└── main.py         → Punto de entrada
```

### Flujo de una operación

```
Vista → Controlador → Servicio → Repositorio → JSON
                    ↓
               Validaciones
               de negocio
```

### Modelos y relaciones

```
Especialidad ←── Medico ←── CitaMedica ──→ Paciente ──→ Padecimiento
(id_especialidad)  (cedula)   (cedula_med)  (cedula)    (id_padecimiento)
                              (cedula_pac)
```

### DTOs utilizados

Para desacoplar la vista del dominio, se usan objetos de transferencia (DTO) que la capa de servicio construye antes de enviar datos a la vista:

- `PacienteVistaDTO` — incluye el nombre del padecimiento en lugar del ID
- `MedicoVistaDTO` — incluye el nombre de la especialidad en lugar del ID
- `CitaMedicaVistaDTO` — incluye nombres de paciente y médico en lugar de cédulas

---

## Principios SOLID aplicados

### S — Single Responsibility
Cada clase tiene una única responsabilidad. El repositorio solo accede a datos, el servicio solo valida lógica de negocio, el controlador solo coordina, la vista solo presenta.

```python
# RepositorioPadecimiento solo persiste y consulta
def buscar_por_id(self, id_padecimiento: str):
    return self.indice_id.get(id_padecimiento)

# ServicioPadecimiento solo valida
if tipo.lower() == "agudo" and tratamiento_prolongado != "No necesita":
    raise ValueError("ERROR | agudo no puede tener tratamiento prolongado")
```

### O — Open/Closed
La lista de controladores en `VistaPrincipal` permite agregar nuevas pestañas sin modificar la lógica de navegación existente.

```python
self.controladores = [
    self.ctrl_especialidad,
    self.ctrl_padecimiento,
    ...
]
def _al_cambiar_pestana(self, event):
    self.controladores[self.notebook.index(self.notebook.select())].cargar_tabla()
```

### L — Liskov Substitution
Todas las vistas heredan de `tk.Frame` y pueden usarse como `master` del notebook sin cambiar el comportamiento esperado.

### I — Interface Segregation
Los servicios exponen solo los métodos que cada controlador necesita. Por ejemplo, `ServicioMedico` recibe `repo_medicos` y `repo_especialidades` por separado en lugar de un único objeto que agrupe todo.

### D — Dependency Inversion
Los servicios no instancian sus repositorios internamente, los reciben como parámetros en el constructor.

```python
# El servicio depende de la abstracción, no de la implementación concreta
class ServicioPaciente:
    def __init__(self, repo_pacientes: RepositorioPaciente, repo_padecimientos: RepositorioPadecimiento):
        self._repo_pacientes = repo_pacientes
        self._repo_padecimientos = repo_padecimientos
```

---

## Estructuras de datos utilizadas

| Estructura | Uso |
|---|---|
| `list` | Lista principal de objetos en cada repositorio |
| `dict` | Índice por ID/cédula para búsqueda O(1) en repositorios |
| `set` | Validación de IDs duplicados en los servicios |
| `tuple` | `obtener_datos()` en cada vista retorna una tupla con los valores del formulario |

---

## Instrucciones de uso

### Requisitos

- Python 3.10 o superior
- tkinter (incluido en la instalación estándar de Python)
- No requiere instalación de librerías externas

### Ejecución

```bash
# Clonar el repositorio
git clone https://github.com/usuario/proyecto_DDS_III.git
cd proyecto_DDS_III

# Ejecutar el sistema
python main.py
```

### Orden recomendado de uso

El sistema tiene dependencias entre módulos. Se recomienda registrar datos en este orden:

```
1. Especialidades   →   2. Padecimientos   →   3. Médicos   →   4. Pacientes   →   5. Citas médicas
```

> No se puede registrar un médico si no hay especialidades, ni un paciente si no hay padecimientos.

### Persistencia

Los datos se guardan automáticamente en la carpeta `data/` al registrar o eliminar cualquier registro. Si la carpeta no existe, el sistema la crea al iniciar.

```
data/
├── especialidades.json
├── padecimientos.json
├── pacientes.json
└── medicos.json
```

---

## Reportes disponibles

| Reporte | Descripción |
|---|---|
| Top 3 pacientes con más citas | Ranking de pacientes por cantidad de citas registradas |
| Padecimiento más frecuente por provincia | Agrupa pacientes por provincia y determina el padecimiento predominante |
| Especialidad más demandada | Cruza médicos con citas para determinar qué especialidad tiene más consultas |

---

## Control de versiones

El proyecto utiliza Git y está alojado en GitHub. Cada integrante realizó commits durante el desarrollo, reflejando la evolución del sistema semana a semana.

```bash
git log --oneline   # ver historial de commits
```
