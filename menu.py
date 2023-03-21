import os
from led import main as led
from temperatura import main as temperatura
from ultrasonico import main as ultrasonico

def clear_console():
    os.system('cls' if os.name=='nt' else 'clear')

def show_menu():
    clear_console()
    print("Menu")
    print("----------------")
    print("1. Sensor de temperatura")
    print("2. Sensor ultrasonico")
    print("3. LED")
    print("4. Salir")
    print("----------------")

def get_option():
    while True:
        try:
            opcion = int(input("Opcion: "))
            if opcion in range(1,5):
                break
            else:
                print("Opción incorrecta. Elige una opción del menú.")
        except ValueError:
            print("Opción incorrecta. Ingresa un número del menú.")
    return opcion

if __name__ == '__main__':
    i = 0
    while i == 0:
        show_menu()
        opcion = get_option()
        if opcion == 1:
            temperatura.main()
        elif opcion == 2:
            ultrasonico.main()
        elif opcion == 3:
            led.main()
        else:
            print("Saliendo...")
            i = 1
