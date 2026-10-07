import json

# Correcciones: True -> true (booleano JSON en minúscula)
#               coma sobrante después de "Validar mercado" eliminada
texto = '{"codigo":"INI-001", "activa":true, "intereses":["Validar mercado"]}'

datos = json.loads(texto)

print("codigo:", datos["codigo"], "->", type(datos["codigo"]).__name__)
print("activa:", datos["activa"], "->", type(datos["activa"]).__name__)
print("intereses:", datos["intereses"])
