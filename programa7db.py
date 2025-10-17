import sqlite3

class dbconsqlite:
    def __init__(self, archivodb, nombre_tabla):
        self.archivodb = archivodb
        self.nombre_tabla = nombre_tabla

    def crear_conexion(self):
        self.conn = sqlite3.connect(self.archivodb)
        self.c = self.conn.cursor()

    def cerrar_conexion(self):
        self.conn.close()

    def crear_tabla(self):
        self.crear_conexion()
        self.c.execute(
            """
            CREATE table %s(
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

    def insertar_en_tabla(self):
        self.crear_conexion()
        self.c.execute(
            """
            INSERT INTO %s VALUES ("Marco Antonio", 15, 6.6, 1, "A", "CDIA", 21)
            """
            % self.nombre_tabla
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

miDB = dbconsqlite("archivo.db", "estudiantes")
miDB.crear_tabla()
miDB.insertar_en_tabla()
miDB.ver_valores()