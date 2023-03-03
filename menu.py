import os

def menu():
    opciones = {
        "1": ("Sensor de temperatura", "temperatura.py"),
        "2": ("Sensor ultrasonico", "ultrasonico.py"),
        "3": ("LED", "led.py")
    }
    
    print("Opciones:")
    for clave, valor in opciones.items():
        print(f"{clave}. {valor[0]}")
    
    opcion = input("Elige una opción (1-3): ")

    if opcion in opciones:
        os.system(f"python3 {opciones[opcion][1]}")
    else:
        print("Opción incorrecta")
        menu()
