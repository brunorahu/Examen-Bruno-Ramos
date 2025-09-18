class FigurasGeometricas:
    def __init__(self):
        self.base = 0
        self.altura = 0
        self.lado1 = 0
        self.lado2 = 0
        self.radio = 0

    def validar_numero(self, mensaje):
        while True:
            try:
                valor = float(input(mensaje))
                if valor <= 0:
                    print("El valor debe ser igual o mayor que cero. Intenta de nuevo.")
                else:
                    return valor
            except ValueError:
                print("Entrada inválida. Ingresa un número.")

    def datos_triangulo(self):
        print("\n--- Cálculo área de un Triángulo ---")
        self.base = self.validar_numero("Ingrese la base del triángulo: ")
        self.altura = self.validar_numero("Ingrese la altura del triángulo: ")

    def datos_rectangulo(self):
        print("\n--- Cálculo área de un Rectángulo ---")
        self.lado1 = self.validar_numero("Ingrese el primer lado (base): ")
        self.lado2 = self.validar_numero("Ingrese el segundo lado (altura): ")

    def datos_circulo(self):
        print("\n--- Cálculo área de un Rectángulo ---")
        self.radio = self.validar_numero("Ingrese el radio del círculo: ")

    def area_triangulo(self):
        return (self.base * self.altura) / 2

    def area_rectangulo(self):
        return self.lado1 * self.lado2
    
    def area_circulo(self):
        return (self.radio * self.radio) * 3.141592

    def mostrar_resultados(self):
        print("\nResultados obtenidos:")
        if self.base and self.altura:
            print(f"Área del triángulo: {self.area_triangulo():.2f}")
        if self.lado1 and self.lado2:
            print(f"Área del rectángulo: {self.area_rectangulo():.2f}")
        if self.readio:
            print(f"Área del círculo: {self.area_circulo():.2f}")