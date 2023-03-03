import time
import RPi.GPIO as GPIO

pin_led = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)

print("hola")

def onOff():
    print ("Presiona 1 para encender el LED")
    print("Presiona 2 para apagarlo")
    
    opcion = input("Opcion: ")
    if opcion == "1":  
        GPIO.output(pin_led, GPIO.HIGH)
        time.sleep(1) # Espera 1 segundo
    elif opcion == "2":
        GPIO.output(pin_led, GPIO.LOW)
        time.sleep(1) # Espera 1 segundo
    else:
        print("Opcion incorrecta")
        onOff()

try:
    print("entró")
    onOff()
except KeyboardInterrupt:
    print("\nInterrupcion por teclado")
except:
    print("Otra interrupcion")
finally:
    GPIO.cleanup()
