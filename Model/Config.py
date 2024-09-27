from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import Qt

from View.config import Ui_frmConfig
from Controller.Teclados import NumericKeyboard, AlphanumericKeyboard
from Model.CanalTransistor import CanalTransistor
from Model.CanalRele import CanalRele


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
        self.ui.txNomeProg.mousePressEvent = self.eventoteclado
        self.ui.btCanalNPN.clicked.connect(lambda: self.tela_canal_transistor_npn())
        self.ui.btCanalPNP.clicked.connect(lambda: self.tela_canal_transistor_pnp())
        self.ui.btCanalRele.clicked.connect(lambda: self.tela_canal_rele())

    def eventoteclado(self, event):
        num_teclado = AlphanumericKeyboard(dado=self.dado)
        num_teclado.exec_()
        self.ui.txNomeProg.setText(num_teclado.line_edit.text())   

    def tela_canal_transistor_npn(self):
        tela_npn = CanalTransistor(dado=self.dado, io=self.io, db=self.database, npn_pnp=self.dado.CANAL_NPN)
        tela_npn.exec_()

    def tela_canal_transistor_pnp(self):
        tela_pnp = CanalTransistor(dado=self.dado, io=self.io, db=self.database, npn_pnp=self.dado.CANAL_PNP)
        tela_pnp.exec_() 

    def tela_canal_rele(self):
        tela_rele =  CanalRele(dado=self.dado, io=self.io, db=self.database)
        tela_rele.exec_() 

    def voltar(self):
        self.close()

    def closeEvent(self, event):
        event.accept()