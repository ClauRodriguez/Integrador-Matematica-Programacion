import time
import random

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
    return int(binario)

def binario_to_decimal(num):
    decimal = 0
    binario = str(num)
    for i in range(len(binario)):
        decimal += int(binario[-(i + 1)]) * (2 ** i)
    return decimal

def get_numero_aleatorio(num1, num2):
    return random.randint(num1, num2)

def adivinar_numero(num):
    userNum = get_num_entero("Ingrese un numero: ")
    intentos = 1
    while userNum != num:
        userNum = get_num_entero("Numero incorrecto, intente nuevamente!: ")
        intentos += 1
    message = f"Numero ADIVINADO!!!\nIntentos necesarios: {intentos}"
    return message

def bienvenida():
    print("\n(っ◔ o ◔)っ  Bienvenidos al trabajo integrador \n")
    print("     El siguente programa muestra dos opciones diferentes de juego")
    print("Abajo se extendera un menu de opciones para elegir....\n")
    time.sleep(2)

def menuPrincipal():
    print("|    Opcion 1: Proyecto Conversión de Números        |\n")
    print("|    Opcion 2: Juego de Adivinan el numero           |\n")
    print("|    Opcion 3: Cerrar programa                       |\n")

def menu1():
    print("\n|    Opcion 1: Convertir numero DECIMAL a BINARIO    |\n")
    print("|    Opcion 2: Convertir numero BINARIO a DECIMAL    |\n")
    print("|    Opcion 3: Volver al menu principal              |")

def menu2():
    print("\n|    Opcion 1: Adivinar binario              |\n")
    print("|    Opcion 2: Adivinar decimal                |\n")
    print("|    Opcion 3: Volver al menu principal        |\n")

def select_game():
    menuPrincipal()
    while True:
        opcion = get_num_entero("\nElija un tipo de juego (1/2/3): ")
        if opcion == 1:
            game_Conversion_Numeros()
        elif opcion == 2:
            game_adivinar_numero()
        elif opcion == 3:
            print("Cerrando programa...")
            break
        else:
            print("Opcion incorrecta! Por favor intente nuevamente.")


def game_Conversion_Numeros():
    print("\nSelecciono Proyecto Conversión de Números!!\n")
    menu1()
    while True:
        opcion = get_num_entero("\nElija una opción del menú: ")
        # Procesamos la eleccion del usuario
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
            print("Volviendo al menu principal...\n")
            menuPrincipal()
            break  # Vuelve al menu principal
        else:
            print("Opción inválida. Intenta de nuevo.")

def game_adivinar_numero():
    print("\nSelecciono Juego de Adivinanza!!\n")
    print("El programa lanzara un numero binario entre los rangos que selecciones, luego tendras que adivinar que numero binario es o viceversa, que decimal es :D ")
    print("\nSeleccionemos los rangos!")
    num1 = get_num_entero("\nElija un numero: ") 
    num2 = get_num_entero("\nElija un numero: ")
    print("Perfecto! Ahora elijamos que queremos adivinar!")
    print(f"Recorda que el rango del numero aleatorio va a estar entre {num1} y {num2}")
    menu2()
    while True:
        opcion = get_num_entero("\nElija una opcion (1/2): ")
        if opcion == 1:
            print("\nLa opcion seleccionada es ADIVINAR EL BINARIO...")
            print("\nEn este juego el programa mostrara un numero en binario y debera adivinar que numero en decimal es :D ")
            num_aleatorio_decimal = get_numero_aleatorio(num1, num2)
            num_aletorio_binario = decimal_to_binario(num_aleatorio_decimal)
            print(f"El numero aleatorio en binario es: {num_aletorio_binario}")
            print("\nQue numero en decimal es? ...")
            mensaje = adivinar_numero(num_aleatorio_decimal)
            print(mensaje)

        elif opcion == 2:
            print("\nLa opcion seleccionada es ADIVINAR EL DECIMAL...")
            print("\nEn este juego el programa mostrara un numero en decimal y debera adivinar que numero en binario es :D ")
            num_aleatorio_decimal = get_numero_aleatorio(num1, num2)
            num_binario = decimal_to_binario(num_aleatorio_decimal)
            print(f"El numero aleatorio en decimal es: {num_aleatorio_decimal}")
            print("\nQue numero en binario es? ...")
            mensaje = adivinar_numero(num_binario)
            print(mensaje)

        elif opcion == 3:
            print("Volviendo al menu principal...\n")
            menuPrincipal()
            
            break
        else:
            print("Opcion incorrecta!! Intente de nuevo")
