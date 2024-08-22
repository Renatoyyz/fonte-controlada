from PyQt5 import QtCore
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import Qt

from View.teste_saidas import Ui_frmTesteSaidas

class TesteSaidas(QDialog):
    def __init__(self, dado , io , db, tipo_saida):
        super().__init__()
        self.dado = dado
        self.io = io
        self.database = db
        self.tipo_saida = tipo_saida

         # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_frmTesteSaidas()
        self.ui.setupUi(self)

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
        # lambda: self.canal(self.tipo_saida, n, m)
        # self.tipo_saida = o tipo de saida
        # n = o canal da saída
        # m = o estado de ligar/desligar
        self.ui.btLigaCanal1.clicked.connect(lambda: self.canal(self.tipo_saida, 0, 1))
        self.ui.btLigaCanal2.clicked.connect(lambda: self.canal(self.tipo_saida, 1, 1))
        self.ui.btLigaCanal3.clicked.connect(lambda: self.canal(self.tipo_saida, 2, 1))
        self.ui.btLigaCanal4.clicked.connect(lambda: self.canal(self.tipo_saida, 3, 1))
    
        self.ui.btDesligaCanal1.clicked.connect(lambda: self.canal(self.tipo_saida, 0, 0))
        self.ui.btDesligaCanal2.clicked.connect(lambda: self.canal(self.tipo_saida, 1, 0))
        self.ui.btDesligaCanal3.clicked.connect(lambda: self.canal(self.tipo_saida, 2, 0))
        self.ui.btDesligaCanal4.clicked.connect(lambda: self.canal(self.tipo_saida, 3, 0))
        

    def canal(self, tipo_saida, saida, status):
        # Se for NPN
        if tipo_saida == 1:
           print(f"Tipo: {tipo_saida}\nCanal: {saida}\nStatus: {status}")
           self.io.npn_output(saida, status)
        # Se for PNP
        elif tipo_saida == 2:
            print(f"Tipo: {tipo_saida}\nCanal: {saida}\nStatus: {status}")
            self.io.pnp_output(saida, status)
        # Se for Rele
        elif tipo_saida == 3:
            print(f"Tipo: {tipo_saida}\nCanal: {saida}\nStatus: {status}")
            self.io.relay_output(saida, status)


    def voltar(self):
        self.close()

    def closeEvent(self, event):
        # Desliga todas as saídas
        for i in range(4):
            print(f"Tipo: {1}\nCanal: {i}\nStatus: {0}")
            self.io.npn_output(i, 0)
            print(f"Tipo: {2}\nCanal: {i}\nStatus: {0}")
            self.io.pnp_output(i, 0)
            print(f"Tipo: {3}\nCanal: {i}\nStatus: {0}")
            self.io.relay_output(i, 0)
        event.accept()