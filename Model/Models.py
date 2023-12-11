import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import Qt

from View.menu import Ui_frmMainMenu
from View.config import Ui_frmConfig

class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_frmMainMenu()
        self.ui.setupUi(self)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Obter o tamanho do monitor primário
        # screen = QApplication.primaryScreen()
        # mainScreenRect = screen.availableGeometry()

        # Definir a posição da janela no canto superior esquerdo
        # self.move(mainScreenRect.topLeft())
        self.move(0,0)

        self.ui.txHidden.keyReleaseEvent = self.eventoteclado

        # faz com que o objeto fique invisível
        self.ui.txHidden.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")

    def eventoteclado(self, event):
        carac = event.text()
        if carac == 'q' or carac == 'Q':
            self.close()

class Config(QDialog):
    def __init__(self):
        super().__init__()

        # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_frmMainMenu()
        self.ui.setupUi(self)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Obter o tamanho do monitor primário
        # screen = QApplication.primaryScreen()
        # mainScreenRect = screen.availableGeometry()

        # Definir a posição da janela no canto superior esquerdo
        # self.move(mainScreenRect.topLeft())
        self.move(0,0)