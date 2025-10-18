"""
Módulo de gestión de tareas.
Proporciona las clases necesarias para manejar tareas y su persistencia en JSON.
"""

import json

class Task:
    """
    Representa una tarea individual con identificador único, descripción y estado.
    """

    def __init__(self, id, description, completed=False):
        """
        Inicializa una nueva tarea.
        Args:
            id (int): Identificador único de la tarea
            description (str): Descripción de la tarea
            completed (bool, optional): Estado de completitud. Por defecto False
        """
        self.id = id
        self.description = description
        self.completed = completed
    
    def __str__(self):
        status = "✔" if self.completed else " "
        return f"[{status}] #{self.id}: {self.description}"

class TaskManager:
    """
    Gestor principal de tareas que maneja la persistencia y operaciones CRUD.
    Mantiene una lista de tareas y las guarda/carga desde un archivo JSON.
    """

    FILENAME = "tasks.json"  # Archivo donde se almacenan las tareas

    def __init__(self):
        """
        Inicializa el gestor de tareas y carga las tareas existentes del archivo.
        """
        self._tasks = []        # Lista de objetos Task
        self._next_id = 1       # Siguiente ID disponible para nueva tarea
        self.load_tasks()       # Carga tareas del archivo si existe
    
    def add_task(self, description):
        """
        Añade una nueva tarea a la lista y la guarda en el archivo.
        Args:
            description (str): Descripción de la tarea a añadir
        """
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Tarea añadida: {description}")
        self.save_tasks()

    def list_task(self):
        """
        Muestra todas las tareas en la consola.
        Si no hay tareas, muestra un mensaje informativo.
        """
        if not self._tasks:
            print("No hay tareas pendientes")
        else:
            for task in self._tasks:
                print(task)

    def complet_task(self, id):
        """
        Marca una tarea como completada dado su ID.
        Args:
            id (int): ID de la tarea a completar
        """
        for task in self._tasks:
            if task.id == id:
                task.completed = True
                print(f"Tarea completada: {task}")
                self.save_tasks()
                return
        print(f"No se ha encontrado la tarea con id: #{id}")
        

    def delete_task(self, id):
        """
        Elimina una tarea dado su ID.
        Args:
            id (int): ID de la tarea a eliminar
        """
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"La tarea con id: #{id} ha sido eliminada")
                self.save_tasks()
                return
        print(f"No se ha encontrado la tarea con id: #{id}")
       

    def load_tasks(self):
        """
        Carga las tareas desde el archivo JSON.
        Si el archivo no existe, inicializa una lista vacía.
        También actualiza el próximo ID disponible basado en las tareas cargadas.
        """
        try:
            with open(self.FILENAME, 'r') as file:
                data = json.load(file)
                self._tasks = [Task(item["id"],item["description"],item["completed"]) for item in data]
                if self._tasks:
                    self._next_id = self._tasks[-1].id + 1
                else:
                    self._next_id = 1
        except FileNotFoundError:
            self._tasks = []

    def save_tasks(self):
        """
        Guarda todas las tareas en el archivo JSON.
        Maneja y reporta cualquier error que ocurra durante el guardado.
        """
        try:
            with open(self.FILENAME, 'w') as file:
                json.dump([{"id": task.id, "description": task.description, "completed": task.completed} for task in self._tasks], file, indent=4)
        except Exception as e:
            print(f"Error al guardar las tareas: {e}")