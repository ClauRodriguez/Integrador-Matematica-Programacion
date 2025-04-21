import time

def get_num_entero(mensaje):
    num = input(f"{mensaje}")
    while not es_numero_entero(num):
        num = input(f"ERROR... {mensaje}")
    return int(num)

def es_numero_entero(num):
    try:
        int(num) 
        return True 
    except ValueError:
        return False
    
def decimal_to_binario(num):
    binario = ""
    while num > 0:
        resto = num % 2
        num = num // 2
        binario = str(resto) + binario
    return binario

def binario_to_decimal(num):
    decimal = 0
    binario = str(num)
    for i in range(len(binario)):
        decimal += int(binario[-(i + 1)]) * (2 ** i)
    return decimal

def bienvenida():
    print("\n(っ◔◡◔)っ  Bienvenidos al trabajo integrador \n")
    print("     El siguente programa convierte numeros DECIMALES a BINARIO o viceversa segun el usuario escoja")
    print("Abajo se extendera un menu de opciones para elegir....\n")
    time.sleep(2)

def menu():
    print("|    Opcion 1: Convertir numero DECIMAL a BINARIO    |\n")
    print("|    Opcion 2: Convertir numero BINARIO a DECIMAL    |")

def opciones():
    menu()
    while True:
        opcion = get_num_entero("\nElija una opción del menú: ")
        # Procesar la elección del usuario
        if opcion == 1:
            print("\n       Opcion 1 -> Convertir numero DECIMAL a BINARIO\n")
            num = get_num_entero("Ingrese un numero decimal: ") #pedimos y validamos que el numero ingresado sea un numero entero
            binario = decimal_to_binario(num) # convertimos el numero decimal a binario mediante la funcion "decimal_to_binario"
            print(f"        El numero binario del decimal {num} es: {binario}")
        elif opcion == 2:
            print("\n       Opcion 2 -> Convertir numero BINARIO a DECIMAL\n")
            num = get_num_entero("Ingrese un numero binario: ")
            decimal = binario_to_decimal(num)
            print(f"        El numero decimal del binario {num} es: {decimal}")
        elif opcion == 3:
            print("Saliendo del programa...")
            break  # Salir del bucle
        else:
            print("Opción inválida. Intenta de nuevo.")



