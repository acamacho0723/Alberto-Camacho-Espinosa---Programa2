class Alumno:
    def __init__(self, nombre, edad, peso, promedio):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.promedio = promedio

    def inscripcion(self):
        return f"El alumno {self.nombre} que tiene {self.edad} años ha sido inscrito"

    def asesorias(self):
        return f"El alumno {self.nombre} que tiene {self.edad} años y un promedio de {self.promedio} ha sido inscrito"
    
# Ejemplos
print(Alumno("Juanito", 15, 50, 6.5).inscripcion())
print(Alumno("Joseph de Jesús", 50, 15, 5.6).asesorias())