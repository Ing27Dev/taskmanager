#!/bin/bash
# Script para ejecutar los tests del proyecto

# Asegurarse de que estamos en el directorio del proyecto
cd "$(dirname "$0")"

# Activar el entorno virtual si existe
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Ejecutar pytest con el PYTHONPATH correcto
PYTHONPATH=$(pwd) pytest -v "$@"