
Frutas = ["manzanas", "platanos", "naranjas"]

while True:

    print("---Menu de la Fruteria---")
    print("1. Ver lista")
    print("2. Ver elemento por su indice")
    print("3. Añadir elemento")
    print("4. Modificar elemento")
    print("5. Borrar elemento")
    print("6. Salir del programa")

    opcion = int(input("Elige la opcion deseada: "))

    match opcion:

        case 1:
            print("Lista completa: ", Frutas)

        case 2:
            indice = int(input("Elige el indice del elemento que quieras ver: "))
            print(Frutas[indice])

        case 3:
            nuevo = input("Introduce la fruta que quieres añadir: ")
            Frutas.append(nuevo)
            print(f"{nuevo} añadido correctamente.")

        case 4:
            indice = int(input("Introduce el indice del elemento que quieras modificar: "))
            nuevo = input("Introduce la nueva fruta: ")
            Frutas[indice] = nuevo

        case 5:
            indice = int(input("Introduce el elemento que quieres borrar: "))
            Frutas.remove(Frutas[indice])
            print("Indice borrado")

        case 6:
            print("Saliendo del programa...")
            break

        case _:
            print(opcion, "no es una opcion.")