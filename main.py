from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():
        print("\n---Gestor de Tareas Inteligente")
        print("1. Añadir tarea")
        print("2. Añadir tarea compleja (con IA)")
        print("3. Listar tareas")
        print("4. Marcar tarea como completada")
        print("5. Eliminar tarea")
        print("6. Salir")

def main():

    manager = TaskManager()

    while True:
        
        print_menu()

        try:

            choice = int(input("Seleccione una opción: "))

            match choice:
                case 1:
                    description = input("Ingrese la descripción de la tarea: ")
                    manager.add_task(description)
                case 2:
                    description = input("Ingrese la descripción de la tarea compleja: ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        if not subtask.startswith("Error"):
                            manager.add_task(subtask)
                        else:
                            print(subtask)
                            break
                case 3:
                    manager.list_task()
                case 4:
                    id = int(input("Ingrese el ID de la tarea a completar: "))
                    manager.complet_task(id)
                case 5:
                    id = int(input("Ingrese el ID de la tarea a eliminar: "))
                    manager.delete_task(id)
                case 6:
                    print("Saliendo del gestor de tareas. ¡Hasta luego!")
                    break
                case _: 
                    print("Opción no válida. Por favor, intente de nuevo.")

        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()   