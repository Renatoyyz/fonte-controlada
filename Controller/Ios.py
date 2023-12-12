import platform
sistema_operacional = platform.system()

# Condição para Raspberry Pi
if sistema_operacional == 'Linux' and 'arm' in platform.machine():
    try:
        import RPi.GPIO as GPIO
    except ImportError:
        print("A biblioteca para Raspberry Pi não está instalada.")
        # Se a biblioteca RPi.GPIO não estiver instalada, você pode definir uma classe simulada
        class GPIO:
            OUT = None
            BCM = None
            @staticmethod
            def setup(pin, mode):
                pass

            @staticmethod
            def setmode(mode):
                pass

            @staticmethod
            def setwarnings(state):
                pass

            @staticmethod
            def output(pin, value):
                pass
# Condição para outros sistemas operacionais
else:
    print("Sistema operacional não suportado.")
    # Se não estiver em um sistema suportado, você pode definir uma classe simulada
    HIGH = 0
    class GPIO:
        OUT = None
        BCM = None
        
        @staticmethod
        def setup(pin, mode):
            pass

        @staticmethod
        def setmode(mode):
            pass

        @staticmethod
        def setwarnings(state):
            pass

        @staticmethod
        def output(pin, value):
            if value == HIGH:
                print('ligado')
            else:
                print('desligado')

import time
import threading

class InOut:
    def __init__(self):
        self.BUZZER = 20
        
        GPIO.setup(self.BUZZER, GPIO.OUT)
        GPIO.setmode(GPIO.BCM) 
        GPIO.setwarnings(False)

    def buzzer(self, estado):
        # Ação invertida de controle
        if estado == 1:
            GPIO.output(self.BUZZER, 0)
        else:
            GPIO.output(self.BUZZER, 1)
