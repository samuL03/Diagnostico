import sqlite3

conexion = sqlite3.connect(":memory:")
conexion.executescript("""
CREATE TABLE emprendedores(id INTEGER PRIMARY KEY, alias TEXT);
CREATE TABLE iniciativas(
    id INTEGER PRIMARY KEY, emprendedor_id INTEGER, estado TEXT
);
INSERT INTO emprendedores VALUES
(1, 'Emprendedor A'), (2, 'Emprendedor B'), (3, 'Emprendedor C');
INSERT INTO iniciativas VALUES
(101, 1, 'activa'), (102, 2, 'archivada'), (103, 1, 'activa');
""")

# Se relaciona iniciativas.emprendedor_id (clave foránea) con
# emprendedores.id (clave primaria) mediante JOIN.
consulta = """
SELECT i.id, e.alias
FROM iniciativas AS i
JOIN emprendedores AS e ON e.id = i.emprendedor_id
WHERE i.estado = 'activa'
ORDER BY i.id;
"""

if consulta:
    print(conexion.execute(consulta).fetchall())

conexion.close()
