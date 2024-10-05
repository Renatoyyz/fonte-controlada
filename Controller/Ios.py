import platform

sistema_operacional = platform.system()
print(sistema_operacional)
# Condição para Raspberry Pi
if sistema_operacional == 'Linux' and 'aarch64' in platform.machine():
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
    HIGH = 1
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
                print(f'ligado{pin}')
            else:
                print(f'desligado{pin}')

class InOut:
    def __init__(self):
        self.BUZZER = 18
        self.NPN_OUTPUTS = [13, 12, 6, 5]
        self.PNP_OUTPUTS = [19, 16, 26, 20]
        self.RELAY_OUTPUTS = [21, 4, 22, 23]
        
        GPIO.setmode(GPIO.BCM) 
        GPIO.setwarnings(False)
        
        GPIO.setup(self.BUZZER, GPIO.OUT)
        for pin in self.NPN_OUTPUTS + self.PNP_OUTPUTS + self.RELAY_OUTPUTS:
            GPIO.setup(pin, GPIO.OUT)

    def buzzer(self, estado):
        # Ação invertida de controle
        if estado == 1:
            GPIO.output(self.BUZZER, 0)
        else:
            GPIO.output(self.BUZZER, 1)

    def npn_output(self, index, estado):
        if 0 <= index < len(self.NPN_OUTPUTS):
            GPIO.output(self.NPN_OUTPUTS[index], estado)

    def pnp_output(self, index, estado):
        if 0 <= index < len(self.PNP_OUTPUTS):
            GPIO.output(self.PNP_OUTPUTS[index], estado)

    def relay_output(self, index, estado):
        if 0 <= index < len(self.RELAY_OUTPUTS):
            GPIO.output(self.RELAY_OUTPUTS[index], estado)