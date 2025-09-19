class Area:
    def obtener_datos(self):
        self.base = float(input("Dame la base:\n"))
        self.altura = float(input("Dame la altura:\n"))

    def sacar_area(self):
        self.area = (self.base * self.altura) / 2

    def imprimir_area(self):
        print(f"Área = {self.area}")

miArea = Area()
miArea.obtener_datos()
miArea.sacar_area()
miArea.imprimir_area()