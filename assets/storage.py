import json
import os

# Creamos la carpeta de proyectos si no existe
PROJECTS_DIR = "proyectos"
os.makedirs(PROJECTS_DIR, exist_ok=True)

def guardar_proyecto(nombre, config):
    """Guarda la configuración en un archivo JSON."""
    # Limpiamos el nombre para que sea un archivo válido (ej. "Torre Andina" -> "torre_andina.json")
    filename = "".join([c if c.isalnum() else "_" for c in nombre]).lower() + ".json"
    filepath = os.path.join(PROJECTS_DIR, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    return filename

def listar_proyectos():
    """Devuelve una lista con los nombres de los archivos guardados."""
    if not os.path.exists(PROJECTS_DIR):
        return []
    archivos = [f for f in os.listdir(PROJECTS_DIR) if f.endswith('.json')]
    return archivos

def cargar_proyecto(filename):
    """Carga la configuración desde un archivo JSON."""
    filepath = os.path.join(PROJECTS_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)