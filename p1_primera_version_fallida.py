import json

# PRIMERA VERSIÓN (falla a propósito: se conserva como evidencia)
texto = '{"codigo":"INI-001", "activa":True, "intereses":["Validar mercado",]}'

try:
    datos = json.loads(texto)
    print(datos)
except json.JSONDecodeError as error:
    print("Error inicial:", error)
