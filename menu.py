import os
from temperatura import main as temperatura
from ultrasonico import main as ultrasonico
from led import main as led

if __name__ == '__main__':
    menuTemp = temperatura()
    menuUltra = ultrasonico()
    menuLed = led()
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
                menuTemp.main()
            elif opcion == 2:
                menuUltra.main()
            elif opcion == 3:
                menuLed.main()
        elif opcion == "4":
            print("Saliendo...")
            i = 1
        else:
            print("Opción incorrecta")
            print ("Elige una opción")
            opcion = int(input())
