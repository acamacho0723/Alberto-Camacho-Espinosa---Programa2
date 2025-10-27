# Para este ejercicio usamos una copia del trabajo de base de datos anterior...
# agregaremos más funciones para este ejercicio
import sqlite3

class dbconsqlite:
    def __init__(self, archivodb, nombre_tabla):
        self.archivodb = archivodb
        self.nombre_tabla = nombre_tabla
        self.identificadores = ["nombre", "edad", "promedio", "semestre", "grupo", "carrera", "aula"]

    def crear_conexion(self):
        self.conn = sqlite3.connect(self.archivodb)
        self.c = self.conn.cursor()

    def cerrar_conexion(self):
        self.conn.close()

    def crear_tabla(self):
        self.crear_conexion()
        self.c.execute(
            """
            CREATE TABLE IF NOT EXISTS %s(
                nombre TEXT,
                edad INTEGER,
                promedio REAL,
                semestre INTEGER,
                grupo TEXT,
                carrera TEXT,
                aula INTEGER
            )
            """
            % self.nombre_tabla
        )
        self.conn.commit()
        self.cerrar_conexion()

    def insertar_en_tabla(self, nombre, edad, promedio, semestre, grupo, carrera, aula):
        self.crear_conexion()
        self.c.execute(
            """
            INSERT INTO %s VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            % (self.nombre_tabla, nombre, edad, promedio, semestre, grupo, carrera, aula)
        )
        self.conn.commit()
        self.cerrar_conexion()

    def ver_valores(self):
        self.crear_conexion()
        self.c.execute(
            """
            SELECT * FROM %s
            """
            % self.nombre_tabla
        )
        resultados = self.c.fetchall()
        for fila in resultados:
            print(fila)
        self.cerrar_conexion()

    def borrar_elementos(self, identificador, valor):
        if identificador not in self.identificadores:
            raise f"EL IDENTIFICADOR NO EXISTE EN {self.identificadores}. INSERTA UN IDENTIFICADOR VALIDO"

        self.crear_conexion()
        self.c.execute(
            """
            DELETE FROM %s
            WHERE %s = %s;
            """
            %
            (self.nombre_tabla, identificador, valor)
        )
        self.conn.commit()
        self.cerrar_conexion()

    def modificar(self, nuevo_id, valor_nuevo, identificador, valor):
        if nuevo_id not in self.identificadores or identificador not in self.identificadores:
            raise f"EL IDENTIFICADOR NO EXISTE EN {self.identificadores}. INSERTA UN IDENTIFICADOR VALIDO"
        
        self.crear_conexion()
        self.c.execute(
            """
            UPDATE %s
            SET %s = %s
            WHERE %s = %s
            """
            %
            (self.nombre_tabla, nuevo_id, valor_nuevo, identificador, valor)
        )
        self.conn.commit()
        self.cerrar_conexion()

# Crear tabla e insertar datos iniciales
print("Crear tabla e insertar datos iniciales")
miDB = dbconsqlite("archivo.db", "estudiantes")
miDB.crear_tabla()
miDB.insertar_en_tabla('"Marco Antonio"', 15, 5.5, 2, '"A"', '"CDIA"', 21)
miDB.insertar_en_tabla('"De Jesus"', 17, 6.6, 4, '"D"', '"Mecatronica"', 6)
miDB.ver_valores()

# Vamos a cambiarle la carrera a Marco Antonio
print("\nVamos a cambiarle la carrera a Marco Antonio")
miDB.modificar("carrera", "'Automotriz'", "nombre", "'Marco Antonio'")
miDB.ver_valores()

# Vamos a borrar el registro del estudiante "De Jesus"
print("\nVamos a borrar el registro del estudiante De Jesus")
miDB.borrar_elementos("nombre", "'De Jesus'")
miDB.ver_valores()