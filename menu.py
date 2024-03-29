import os
import led 
import temperatura 
import ultrasonico 

if __name__ == '__main__':
    i = 0
    while i == 0:
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
            elif opcion == 2:
                while ultrasonico.main() != "menu":
                    pass
            elif opcion == 3:
                led.main()
        elif opcion == 4:
            print("Saliendo...")
            i = 1
        else:
            print("Opción incorrecta")
            print("Elige una opción")
            opcion = int(input())
