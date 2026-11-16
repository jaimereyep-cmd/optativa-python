import math

while True:

    try:

        print("---Menu de ejercicios---")
        print("1. Ejercicio 9")
        print("2. Ejercicio 10")
        print("3. Ejercicio 11")
        print("4. Ejercicio 12")
        print("5. Ejercicio 13")
        print("6. Salir")

        opcion = int(input("Introduce un numero: "))

        match opcion:

            case 1:

                metros = float(input("Introduce una medida en metros: "))
                conversion = metros * 100
                print(f"{metros} metros en centimetros son {conversion}")
                pass

            case 2:

                r = int(input("Introduce el radio de la circunferencia: "))
                area = math.pi * r ** 2
                print(f"El area del circulo es = {area}")
                pass

            case 3:

                precio = int(input("Introduce el precio de la comida: "))
                propina = int(input("Introduce el porcentaje de propina: "))
                importe_propina = precio * propina / 100

                total = precio + importe_propina

                print(f"el total es = {total}")
                pass

            case 4:

                peso = float(input("Introduce tu peso: "))
                altura = float(input("Introduce tu altura: "))
                imc = peso / altura ** 2
                print(f"Tu IMC es {imc}")
                pass

            case 5:

                nombre = input("Introduce tu nombre: ")
                apellido = input("Introduce tu apellido: ")

                print(f"Hola {nombre} {apellido}")
                pass

            case 6:

                print("Saliendo del programa...")
                break

            case _:

                print("Introduce un numero valido")

    except ValueError:
        print("Error: Debes introducir un numero valido")

    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")