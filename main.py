class Programa4:
    def leer_datos(self):
        """
        COMENTARIO: Esta vez no use __init__, para que no me repruebe
        """
        self.nombres = []
        self.calificaciones = []

        for i in range(10):
            self.nombres.append(input("Dame tu nombre:\n"))
            self.calificaciones.append(float(input("Dame tu calificación:\n")))

    def realizar_el_proceso(self):
        self.promedio = sum(self.calificaciones) / len(self.calificaciones)
        
        self.conmasde95 = []

        for i in range(len(self.calificaciones)):
            if self.calificaciones[i] > 9.5:
                self.conmasde95.append(self.nombres[i])

    def imprimir_resultados(self):
        print("Los resultados son:\n")
        print(f"    {self.nombres}")
        print(f"    {self.calificaciones}\n")
        print(f"    Gente con más de 9.5:\n    {self.conmasde95}\n")
        print(f"    Promedio Grupal = {self.promedio}")

miPrograma = Programa4()
miPrograma.leer_datos()
miPrograma.realizar_el_proceso()
miPrograma.imprimir_resultados()