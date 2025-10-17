import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):
    if not client.api_key:
        return ["Error: OpenAI API key is not configured."]
    
    try:

        promt = f"""Desglosa la siguiente tarea en compleja en una lista lista de 3 a 5 tareas simples y accionables.
        Tarea: {description}

        Formato de respuesta:
        - Subtarea 1
        - Subtarea 2
        - Subtarea 3
        - etc.
        
        Responde solo con la lista de subtareas, una por línea, empezando con un guion."""

        params = {
            "model": "gpt-5",
            "messages": [
                {"role": "system", "content": "Eres un asistente experto en gestion de tareas que ayuda a dividir tareas complejas en pasos simples y accionables."},
                {"role": "user","content": promt}
            ],
            "max_completion_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "low"
        }

        response = client.chat.completions.create(**params)

        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        return subtasks if subtasks else ["Error: No se pudieron generar subtareas."]

    except Exception as e:
        return [f"Error: {str(e)}"]