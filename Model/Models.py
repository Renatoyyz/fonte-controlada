import typing
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import Qt

from View.menu import Ui_frmMainMenu
from View.config import Ui_frmConfig

from Controller.Teclados import AlphanumericKeyboard
from Controller.SimpleMassage import SimpleMessageBox

class MainMenu(QMainWindow):
    def __init__(self, dado=None, io=None):
        super().__init__()
        self.dado = dado
        self.io = io

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
        self.ui.btConfigProg.clicked.connect(self.open_config)
        self.ui.btInitProg.clicked.connect(self.init_prog)

        # faz com que o objeto fique invisível
        self.ui.txHidden.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")
        

    def eventoteclado(self, event):
        carac = event.text()
        if carac == 'q' or carac == 'Q':
            self.close()

    def open_config(self):
        self.janela_config = Config(dado=self.dado)
        #self.janela2.showMaximized()
        self.janela_config.exec_()

    def init_prog(self):
        msg = SimpleMessageBox(message="Olá mundo")
        msg.exec()

class Config(QDialog):
    def __init__(self, dado=None, io=None):
        super().__init__()

        self.dado = dado
        self.io = io

        # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_frmConfig()
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

        self.ui.btVoltar.clicked.connect(self.voltar)
        self.ui.txNomeProg.mouseReleaseEvent = self.write_name

    def voltar(self):
        self.close()

    def closeEvent(self, event):
        print("fechou")

    def write_name(self, event):
        self.teclado = AlphanumericKeyboard(dado=self.dado, mode='nome_programa')
        self.teclado.exec_()
        self.ui.txNomeProg.setText(self.dado.nome_prog)

        
        