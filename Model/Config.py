from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt

from View.config import Ui_frmConfig

from Model.TesteSaidas import TesteSaidas

class Config(QDialog):
    def __init__(self, dado , io , db):
        super().__init__()
        self.dado = dado
        self.io = io
        self.database = db

        # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_frmConfig()
        self.ui.setupUi(self)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Maximizar a janela
        # self.showMaximized()
        if self.dado.full_scream == True:
            self.setWindowState(Qt.WindowState.WindowFullScreen)

        self.ui.btVoltar.clicked.connect(self.voltar)

        # Se self.tipo_saida:
        # tipo_saida = 1: Saida NPN
        # tipo_saida = 2: Saida PNP
        # tipo_saida = 3: Saida Rele
        self.ui.btCanalNPN.clicked.connect(lambda: self.teste_saida(1))
        self.ui.btCanalPNP.clicked.connect(lambda: self.teste_saida(2))
        self.ui.btCanalRele.clicked.connect(lambda: self.teste_saida(3))

    def teste_saida(self, tipo_saida):
        tela_npn = TesteSaidas(dado=self.dado, io=self.io, db=self.database, tipo_saida=tipo_saida)
        tela_npn.exec_()

    def voltar(self):
        self.close()

    def closeEvent(self, event):
        event.accept()