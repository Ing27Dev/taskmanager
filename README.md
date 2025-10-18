# TaskManager con IA

Un gestor de tareas inteligente que utiliza IA para desglosar tareas complejas en subtareas manejables.

## 🌟 Características

- Gestión básica de tareas (CRUD):
  - ✅ Añadir tareas
  - 📋 Listar tareas
  - ✔️ Marcar tareas como completadas
  - 🗑️ Eliminar tareas
  - 🤖 Integración con IA:
  - Desglose automático de tareas complejas en 3-5 subtareas
  - Utiliza OpenAI GPT para análisis inteligente
  - 💾 Persistencia de datos:
  - Guardado automático en archivo JSON
  - Carga del estado previo al iniciar

## 📋 Requisitos Previos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Conexión a Internet (para funciones de IA)
- Clave API de OpenAI (para funciones de IA)

## 🚀 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Ing27Dev/taskmanager.git
cd taskmanager
```

2. Crear y activar un entorno virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # En Linux/Mac
# o
.venv\Scripts\activate     # En Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la clave API de OpenAI:
```bash
# Crear archivo .env en la raíz del proyecto
echo "OPENAI_API_KEY=tu_clave_api_aqui" > .env
```

## 💻 Uso

1. Activar el entorno virtual (si no está activo):
```bash
source .venv/bin/activate  # Linux/Mac
# o
.venv\Scripts\activate     # Windows
```

2. Ejecutar el programa:
```bash
python main.py
```

3. Usar el menú interactivo:
   - Opción 1: Añadir tarea simple
   - Opción 2: Añadir tarea compleja (usa IA)
   - Opción 3: Listar tareas
   - Opción 4: Marcar tarea como completada
   - Opción 5: Eliminar tarea
   - Opción 6: Salir

## 🏗️ Estructura del Proyecto

\`\`\`
TaskManager/
├── __init__.py
├── main.py               # Punto de entrada, interfaz de usuario
├── task_manager.py      # Lógica de gestión de tareas
├── ai_service.py        # Servicios de IA para procesar tareas
├── requirements.txt     # Dependencias del proyecto
├── run_tests.sh        # Script para ejecutar tests
├── tasks.json          # Almacenamiento de tareas (generado)
├── .env               # Configuración (crear manualmente)
└── tests/
    ├── __init__.py
    ├── test_task_manager.py
    └── test_ai_service.py
\`\`\`

## 🔧 Desarrollo

### Dependencias Principales

- openai: Integración con GPT para análisis de tareas
- python-dotenv: Gestión de variables de entorno
- pytest: Framework de testing

### Tests

El proyecto incluye tests unitarios completos. Para ejecutarlos:

1. Usando el script incluido:
```bash
./run_tests.sh
```

2. O manualmente:
```bash
PYTHONPATH=. pytest -v
```

Los tests cubren:
- TaskManager:
  - Creación y gestión de tareas
  - Persistencia de datos
  - Manejo de estados
- AIService:
  - Integración con OpenAI
  - Manejo de errores
  - Procesamiento de respuestas

## 📝 Clases y Métodos Principales

### Task
```python
class Task:
    def __init__(self, id, description, completed=False)
```
Representa una tarea individual con:
- id: Identificador único
- description: Descripción de la tarea
- completed: Estado de completitud

### TaskManager
```python
class TaskManager:
    def add_task(self, description)    # Añade nueva tarea
    def list_task()                    # Lista todas las tareas
    def complet_task(self, id)         # Marca tarea como completada
    def delete_task(self, id)          # Elimina una tarea
    def load_tasks()                   # Carga tareas del archivo
    def save_tasks()                   # Guarda tareas en archivo
```

### AIService
```python
def create_simple_tasks(description)    # Desglosa tarea compleja
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crear rama para feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add: AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📄 Licencia

Este proyecto está licenciado bajo los términos de la licencia MIT.

## 👥 Autores

- [@Ing27Dev](https://github.com/Ing27Dev) - Desarrollo inicial

## 🙏 Agradecimientos

- OpenAI por proporcionar la API para el análisis de tareas
- Comunidad de Python por las herramientas y frameworks utilizados
