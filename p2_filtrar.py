iniciativas = [
    {"codigo": "INI-001", "sector": "tecnologia", "pendiente": True},
    {"codigo": "INI-002", "sector": "alimentos", "pendiente": True},
    {"codigo": "INI-003", "sector": "tecnologia", "pendiente": False},
    {"codigo": "INI-004", "sector": "tecnologia"},
]


def seleccionar_pendientes(registros, sector):
    """Retorna los códigos del sector indicado con pendiente exactamente True.

    - No modifica la lista recibida (solo lee).
    - Si falta el campo 'pendiente', .get() devuelve None y el registro se
      excluye: ausente se trata como "no pendiente".
    - Se usa 'is True' para no confundir el booleano True con una cadena
      como "true" (que sería truthy pero no es un booleano).
    """
    return [
        r["codigo"]
        for r in registros
        if r.get("sector") == sector and r.get("pendiente") is True
    ]


# Prueba 1: con resultados
assert seleccionar_pendientes(iniciativas, "tecnologia") == ["INI-001"]
# Prueba 2: sin resultados
assert seleccionar_pendientes(iniciativas, "economia_circular") == []
# Extra: la lista original no cambió
assert len(iniciativas) == 4 and "pendiente" not in iniciativas[3]

print("tecnologia ->", seleccionar_pendientes(iniciativas, "tecnologia"))
print("economia_circular ->", seleccionar_pendientes(iniciativas, "economia_circular"))
print("Todas las pruebas pasaron")
