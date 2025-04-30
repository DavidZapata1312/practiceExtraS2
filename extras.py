# Función para verificar si un número es par o impar
def parOrIm():
    num = float(input("Ingrese un numero: "))  # Se pide un número (con decimales)
    if num % 2 == 0:  # Se verifica si el número es divisible entre 2 sin residuo
        print (f"{num} es par")
    else: 
        print(f"{num} es impar")

# Función para verificar si un año es bisiesto
def leapYear():
    year = int(input("Ingrese un año: "))  # Se pide un año como número entero
    # Condición clásica para año bisiesto:
    # divisible por 4 Y no divisible por 100, O divisible por 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print (f"{year} Es bisiesto")
    else:
        print (f"{year} No es bisiesto")

# Función para calcular la suma de todos los números desde 1 hasta n
def sumToN():
    while True:
        num = int(input("Ingrese un número positivo: "))
        if num > 0:
            total = 0
            for i in range(1, num + 1):  # Suma del 1 hasta num
                total += i
            print(f"La suma de los números de 1 hasta {num} es: {total}")
            break  # Sale del bucle cuando se ingresa un número válido
        else:
            print("Por favor, ingrese un número positivo.")

# Función para mostrar los números impares desde 1 hasta un número dado
def oddInN():
    odds = []  # Lista para guardar los impares

    num = int(input("Ingrese un número: "))  # Se pide un número entero

    for i in range(1, num + 1):  # Se recorre desde 1 hasta el número ingresado
        if i % 2 != 0:  # Si el número no es divisible entre 2
            odds.append(i)  # Se agrega a la lista

    # Se muestra el resultado al final
    print("\nCantidad de impares encontrados:", len(odds))
    print("Números impares:", odds)

# Función principal que muestra el menú y dirige al usuario según su elección
def menu():
    while True:
        # Opciones disponibles
        print("\n📋 MENÚ DE OPCIONES 📋")
        print("1. Verificar si un número es par o impar")
        print("2. Verificar si un año es bisiesto")
        print("3. Calcular la suma de 1 hasta un número dado")
        print("4. Mostrar todos los impares hasta un número dado")
        print("5. Salir")

        opcion = input("Elija una opción (1-5): ")

        # Se ejecuta la función correspondiente según la opción elegida
        if opcion == '1':
            parOrIm()
        elif opcion == '2':
            leapYear()
        elif opcion == '3':
            sumToN()
        elif opcion == '4':
            oddInN()
        elif opcion == '5':
            print("¡Hasta luego!")  # Mensaje de despedida
            break  # Se rompe el bucle y termina el programa
        else:
            print("Opción no válida. Intenta nuevamente.")  # Validación de opción

# Punto de entrada principal del programa
if __name__ == '__main__':
    menu()  # Llama al menú principal
