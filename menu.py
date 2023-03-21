import os
import led 
import temperatura 
import ultrasonico 

def menu():
    while True:
        print("Menu")
        print("----------------")
        print("1. Sensor de temperatura")
        print("2. Sensor ultrasonico")
        print("3. LED")
        print("4. Salir")
        opcion = int(input("Opcion: "))
        if opcion in [1, 2, 3]:
            if opcion == 1:
                temperatura.main()
                return
            elif opcion == 2:
                ultrasonico.main()
                return
            elif opcion == 3:
                led.main()
                return
        elif opcion == 4:
            print("Saliendo...")
            break
        else:
            print("Opción incorrecta")
            print("Elige una opción")
            opcion = int(input())

        # Pausa para que el usuario pueda leer el resultado
        input("Presiona Enter para regresar al menú")
        
if __name__ == '__main__':
    menu()