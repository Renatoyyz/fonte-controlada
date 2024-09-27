from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QDialog
from PyQt5.QtCore import Qt

from Controller.Teclados import NumericKeyboard
from View.config_canal_rele import Ui_frmConfigCanalRele

class CanalRele(QDialog):
    def __init__(self, dado , io , db):
        super().__init__()
        self.dado = dado
        self.io = io
        self.database = db

        # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_frmConfigCanalRele()
        self.ui.setupUi(self)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Maximizar a janela
        # self.showMaximized()
        if self.dado.full_scream == True:
            self.setWindowState(Qt.WindowState.WindowFullScreen)

        self.ui.btVoltar.clicked.connect(self.voltar)
        self.ui.txTonCanal_1.mousePressEvent = self.tx_canal_1_ton
        self.ui.txToffCanal_1.mousePressEvent = self.tx_canal_1_toff
        self.ui.txTonCanal_2.mousePressEvent = self.tx_canal_2_ton
        self.ui.txToffCanal_2.mousePressEvent = self.tx_canal_2_toff
        self.ui.txTonCanal_3.mousePressEvent = self.tx_canal_3_ton
        self.ui.txToffCanal_3.mousePressEvent = self.tx_canal_3_toff
        self.ui.txTonCanal_4.mousePressEvent = self.tx_canal_4_ton
        self.ui.txToffCanal_4.mousePressEvent = self.tx_canal_4_toff
        self.ui.txQtdCiclos.mousePressEvent = self.tx_qtd_ciclos

    def tx_canal_1_ton(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txTonCanal_1.setText(teclado.line_edit.text())

    def tx_canal_1_toff(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txToffCanal_1.setText(teclado.line_edit.text())

    def tx_canal_2_ton(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txTonCanal_2.setText(teclado.line_edit.text())  

    def tx_canal_2_toff(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txToffCanal_2.setText(teclado.line_edit.text()) 
    
    def tx_canal_3_ton(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txTonCanal_3.setText(teclado.line_edit.text())

    def tx_canal_3_toff(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txToffCanal_3.setText(teclado.line_edit.text())

    def tx_canal_4_ton(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txTonCanal_4.setText(teclado.line_edit.text())

    def tx_canal_4_toff(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txToffCanal_4.setText(teclado.line_edit.text())

    def tx_qtd_ciclos(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txQtdCiclos.setText(teclado.line_edit.text())

    def voltar(self):
        self.close()

    def closeEvent(self, event):
        event.accept()