import time
print("-------- AGENDA --------")


def menu():
    print("¿Que operacion desea realizar?\n 1- Buscar contacto.\n 2- Agregar contacto.\n "
          "3- Borrar contacto.\n 4- Modificar contacto.\n 5- Salir.\n")


def impimir_datos(linea):
    datos = linea.strip().split(",")
    nombre = datos[1]
    apellido = datos[2]
    telefono = datos[3]
    email = datos[4]
    empresa = datos[5]
    print("--------------------------------")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Teléfono:", telefono)
    print("Email:", email)
    print("Empresa:", empresa)
    print("--------------------------------")

menu()
operacion = int(input("Ingrese un numero de operacion: "))
print("----------------------------------------------------------------")

while operacion != 5:
    if operacion == 1:
        print("Buscar por:\n1-Nombre.\n2-Apellido.\n3-Empresa.")
        numero = int(input("Ingrese un numero de operacion: "))
        base_de_datos = open("C:/Users/Lenovo/OneDrive/Escritorio/basedatos.txt", "r", encoding="UTF-8")
        lineas = base_de_datos.readlines()
        if numero == 1:
            nombre_a_buscar = input("Ingrese el nombre para buscar: ")
            encontrado = False
            for linea in lineas:
                if nombre_a_buscar in linea:
                    time.sleep(1)
                    impimir_datos(linea)
                    encontrado = True
                    break
            if not encontrado:
                nombre_a_buscar = input("El nombre no existe en la agenda. Vuelva a buscar.")
                continue


        if numero == 2:
            apellido_a_buscar = input("Ingrese el apellido a buscar: ")
            encontrado = False
            for linea in lineas:
                if apellido_a_buscar in linea:
                    impimir_datos(linea)
                    encontrado = True
                    break
            if not encontrado:
                print("El contacto no existe en la agenda. Vuelva a buscar.")
                print("--------------------------------")
                continue

        if numero == 3:
            empresa_a_buscar = input("Ingrese la empresa a buscar: ")
            encontrado = False
            for linea in lineas:
                if empresa_a_buscar in linea:
                    impimir_datos(linea)
                    encontrado = True
                    break
            if not encontrado:
                print("La empresa no existe en la agenda. Vuelva a buscar.")
                print("--------------------------------")
                continue
        base_de_datos.close()
        time.sleep(2)
        menu()
        operacion = int(input("Ingrese un numero de operacion: "))

    elif operacion == 2:
        base_de_datos = open("C:/Users/Lenovo/OneDrive/Escritorio/basedatos.txt", "a+", encoding="UTF-8")

        nombre_agenda = input("Ingrese el nombre del contacto para agendar: ")
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        numero = input("Ingrese el numero de telefono: ")
        email = input("Ingrese el e-mail: ")
        empresa = input("Ingrese la empresa: ")

        base_de_datos.write("\n")
        base_de_datos.write(nombre_agenda + ",")
        base_de_datos.write(nombre + ",")
        base_de_datos.write(apellido + ",")
        base_de_datos.write(numero + ",")
        base_de_datos.write(email + ",")
        base_de_datos.write(empresa)
        base_de_datos.close()


        print("Contacto agregado exitosamente. Por favor, corrobore los datos.")
        time.sleep(1)
        base_de_datos = open("C:/Users/Lenovo/OneDrive/Escritorio/basedatos.txt", "r", encoding="UTF-8")
        lineas = base_de_datos.readlines()
        encontrado = False
        for linea in lineas:
            if nombre in linea:
                impimir_datos(linea)
        base_de_datos.close()
        time.sleep(8)
        menu()
        operacion = int(input("Ingrese un numero de operacion: "))



    elif operacion == 3:
        nombre_a_buscar = input("Ingrese el nombre del contacto a eliminar: ")
        base_de_datos = open("C:/Users/Lenovo/OneDrive/Escritorio/basedatos.txt", "r+", encoding="UTF-8")
        lineas = base_de_datos.readlines()
        base_de_datos.seek(0)
        base_de_datos.truncate()
        encontrado = False
        for linea in lineas:
            if nombre_a_buscar not in linea:
                base_de_datos.write(linea)
            else:
                encontrado = True
        base_de_datos.close()
        if encontrado:
            time.sleep(2)
            print("El contacto ha sido eliminado.")
            print("--------------------------------")
        else:
            print("El contacto no existe en la agenda.")
        time.sleep(1)
        menu()
        operacion = int(input("Ingrese un numero de operacion: "))



    elif operacion == 4:
        base_de_datos = open("C:/Users/Lenovo/OneDrive/Escritorio/basedatos.txt", "r+", encoding="UTF-8")
        lineas = base_de_datos.readlines()

        nombre_a_modificar = input("Ingrese el nombre del contacto a modificar: ")
        encontrado = False
        for i, linea in enumerate(lineas):
            if nombre_a_modificar in linea:
                encontrado = True
                datos = linea.strip().split(",")
                nombre = datos[1]
                apellido = datos[2]
                telefono = datos[3]
                email = datos[4]
                empresa = datos[5]
                print("--------------------------------")
                print("Nombre:", nombre)
                print("Apellido:", apellido)
                print("Teléfono:", telefono)
                print("Email:", email)
                print("Empresa:", empresa)
                print("--------------------------------")

                nombre = input("Ingrese el nuevo nombre (Dejar vacío si no desea cambiar): ")
                apellido = input("Ingrese el nuevo apellido (Dejar vacío si no desea cambiar): ")
                telefono = input("Ingrese el nuevo teléfono (Dejar vacío si no desea cambiar): ")
                email = input("Ingrese el nuevo email (Dejar vacío si no desea cambiar): ")
                empresa = input("Ingrese la nueva empresa (Dejar vacío si no desea cambiar): ")

                lineas[
                    i] = f"{nombre_a_modificar},{nombre if nombre else datos[1]},{apellido if apellido else datos[2]}," \
                         f"{telefono if telefono else datos[3]},{email if email else datos[4]}," \
                         f"{empresa if empresa else datos[5]}\n"
                break

        if not encontrado:
            print("El contacto no existe en la agenda.")
            base_de_datos.close()
            menu()
            operacion = int(input("Ingrese un numero de operacion: "))
            continue

        base_de_datos.seek(0)
        base_de_datos.truncate()
        base_de_datos.writelines(lineas)
        base_de_datos.close()
        time.sleep(2)
        print("Contacto modificado exitosamente.")
        encontrado = False
        for linea in lineas:
            if nombre_a_modificar in linea:
                impimir_datos(linea)
        print("--------------------------------")
        time.sleep(1)
        menu()
        operacion = int(input("Ingrese un numero de operacion: "))

else:
    print("CERRANDO AGENDA...")
    time.sleep(3)
    print("-- MUCHAS GRACIAS --")

