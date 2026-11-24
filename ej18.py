productos = ["manzana", "platanos", "naranjas", "kiwi", "fresas"]
info_tienda = ["Fruteria de la Huerta", "Calle Mayor 12", "912345678", "2010"]
precios = {"manzanas": 1.50, "platanos": 2.10, "naranjas": 1.20, "kiwis":3.45, "fresas": 2.80}

while True:

    print("--- Menu Fruteria de la Huerta ---")
    print("1. Gestion de listas")
    print("2. ")
    print("3. ")
    print("4. Salir del programa")

    try:
        opcion = int(input("Introduce la opcion aqui: "))

        match opcion:
            case 1: 
                print("\n a) Consultar\n b)Añadir\n c)Modificar\n d)Eliminar" )

                sub = input("Introduce una opcion:").lower()

                match sub:
                    case "a":
                        print(f"Productos : {productos}")
                    case "b":
                        nuevo = input("Introduce el nombre del nuevo producto: ")
                        productos.append(nuevo)
                        print(f"{nuevo} añadido correctamente")
                    case "c":
                        for i, p in enumerate(productos):
                            print(f"{i}: {p}")
                        indice = input("introduce el indice a modificar: ")
                        nuevo = input("Nuevo nombre del producto: ")
                        productos[indice] = nuevo
                        print("Producto modificado")
                    case "d":
                        indice = input("Introduce el indice que quieres eliminar: ")
                        productos.remove(productos[indice])
            case 4:
                print("Saliendo del programa...")
                break
            case _:
                print("Opcion no valida.")

    except ValueError:
        print("Error. Introduce un valor valido")
    except IndexError:
        print("Error. Ese indice no existe en la lista")