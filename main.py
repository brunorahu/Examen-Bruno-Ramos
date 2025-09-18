from clases.areas import FigurasGeometricas

def main():
    print("=== Calculadora de Áreas ===")
    figura = FigurasGeometricas()

    while True:
        print("\nSeleccione la figura que desea calcular:")
        print("1. Triángulo")
        print("2. Rectángulo")
        print("3. Círculo")        
        print("4. Salir")

        opcion = input("Ingrese su opción (1-4): ")

        if opcion == "1":
            figura.datos_triangulo()
            print(f"Área del triángulo: {figura.area_triangulo():.2f}")
        elif opcion == "2":
            figura.datos_rectangulo()
            print(f"Área del rectángulo: {figura.area_rectangulo():.2f}")
        elif opcion == "3":
            figura.datos_circulo()
            print(f"Área del rectángulo: {figura.area_circulo():.2f}")
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Sintaxis incorrecta: Ingrese su opción (1-4). Intente de nuevo.")

main()