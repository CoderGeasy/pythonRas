import os

def menu():
    print("1. Sensor de temperatura")
    print("2. Sensor ultrasonico")
    print("3. LED")
    
    opcion = input("Elige una opcion: ")

    if opcion == "1":               
        os.system("python3 temperatura.py")
    elif opcion == "2":
        os.system("python3 ultrasonico.py")
    elif opcion == "3":
        os.system("python3 led.py")
    else:
        print("Opcion incorrecta")
        menu()
    