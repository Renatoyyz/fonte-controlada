from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import Qt

from View.menu import Ui_frmMainMenu
from Model.Config import Config

from Model.TesteSaidas import TesteSaidas

class MainMenu(QMainWindow):
    def __init__(self, dado , io , db):
        super().__init__()
        self.dado = dado
        self.io = io
        self.database = db

        # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_frmMainMenu()
        self.ui.setupUi(self)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Maximizar a janela
        # self.showMaximized()
        if self.dado.full_scream == True:
            self.setWindowState(Qt.WindowState.WindowFullScreen)

        self.ui.txHidden.keyReleaseEvent = self.eventoteclado
        self.ui.btConfigProg.clicked.connect(self.tela_config)

        # faz com que o objeto fique invisível
        self.ui.txHidden.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")

        # Se self.tipo_saida:
        # tipo_saida = 1: Saida NPN
        # tipo_saida = 2: Saida PNP
        # tipo_saida = 3: Saida Rele
        self.ui.btTestOutNPN.clicked.connect(lambda: self.teste_saida(1))
        self.ui.btTestOutPNP.clicked.connect(lambda: self.teste_saida(2))
        self.ui.btTestOutRelay.clicked.connect(lambda: self.teste_saida(3))

    def teste_saida(self, tipo_saida):
        tela_npn = TesteSaidas(dado=self.dado, io=self.io, db=self.database, tipo_saida=tipo_saida)
        tela_npn.exec_()
        


    def tela_config(self):
        tela_config = Config(self.dado, self.io, self.database)
        tela_config.exec_()

    def eventoteclado(self, event):
        carac = event.text()
        if carac == 'q' or carac == 'Q':
            self.close()