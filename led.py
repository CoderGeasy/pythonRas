import time
import RPi.GPIO as GPIO  #Importamos el paquete RPi.GPIO y en el código nos refiriremos a el como GPIO

pin_led = 22  #Variable que contiene el pin(GPIO.BCM) al cual conectamos la señal del LED

GPIO.setmode(GPIO.BCM)   #Establecemos el modo según el cual nos refiriremos a los GPIO de nuestra RPi            
GPIO.setup(pin_led, GPIO.OUT) #Configuramos el GPIO18 como salida

#Contenemos el código principal en una estructura try para limpiar los GPIO al terminar o presentarse un error
try:
    def onOff():
        print ("Presiona 1 para encender el LED")
        print("Presiona 2 para apagarlo")
        
        opcion = input("Opcion: ")  #Leemos la opcion del usuario
        if opcion == "1":   #Implementamos un loop infinito
            GPIO.output( pin_led , GPIO.HIGH )
        elif opcion == "2":
            GPIO.output( pin_led , GPIO.LOW )
        else:
            print("Opcion incorrecta")
            onOff()
except KeyboardInterrupt:
    # CTRL+C
    print("\nInterrupcion por teclado")
except:
    print("Otra interrupcion")
finally:
    GPIO.cleanup()
    print("GPIO.cleanup() ejecutado")