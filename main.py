import sys
from PyQt5.QtWidgets import QApplication
from Model.Models import MainMenu
from Controller.Ios import InOut
from Controller.Dados import Dado

if __name__ == '__main__':
    app = QApplication(sys.argv)
    out = InOut()
    dado = Dado()

    window = MainMenu(dado=dado)
    window.show()
    out.buzzer(estado=1)
    # Quando fecha a aplicação, destroi a plicação no sistema bem como encerra todas as threads em execução.
    #sys.exit([app.exec(), dado.temp.stop(), pwm.stop(), pwm_frio.stop(), io.stop()])
    sys.exit(app.exec())