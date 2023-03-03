import time
import RPi.GPIO as GPIO

pin_led = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)

print("hola")

def main():
    i = 0
     
    while i == 0:
        print("Menú")
        print("Presiona 1 para encender el LED")
        print("Presiona 2 para apagar el LED")
        print("Presiona 3 para salir")
        opcion = int(input("Opcion: "))
        if opcion in [1, 2]:  
            if opcion == 1:
                GPIO.output(pin_led, GPIO.HIGH)
                time.sleep(1) # Espera 1 segundo
            elif opcion == "2":
                GPIO.output(pin_led, GPIO.LOW)
                time.sleep(1) # Espera 1 segundo
        elif opcion == 3:
            print("Saliendo...")
            i = 1
        else:
            print("Opcion incorrecta")
            opcion = int(input("Opcion: "))
    try:
        print("entró")
        main()
    except KeyboardInterrupt:
        print("\nInterrupcion por teclado")
    except:
        print("Otra interrupcion")
    finally:
        GPIO.cleanup()
