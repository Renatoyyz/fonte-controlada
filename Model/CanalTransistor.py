from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from PyQt5.QtCore import Qt

from Controller.Teclados import NumericKeyboard
from View.config_canal_transistor import Ui_frmConfigCanalTransistor

class CanalTransistor(QDialog):
    def __init__(self, dado , io , db, npn_pnp):
        super().__init__()
        self.dado = dado
        self.io = io
        self.database = db
        self.npn_pnp = npn_pnp
        self.prog = None

        # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_frmConfigCanalTransistor()
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
        self.ui.txQtdCiclosCanal_1.mousePressEvent = self.tx_canal_1_qtd
        self.ui.txTonCanal_2.mousePressEvent = self.tx_canal_2_ton
        self.ui.txToffCanal_2.mousePressEvent = self.tx_canal_2_toff
        self.ui.txQtdCiclosCanal_2.mousePressEvent = self.tx_canal_2_qtd
        self.ui.txTonCanal_3.mousePressEvent = self.tx_canal_3_ton
        self.ui.txToffCanal_3.mousePressEvent = self.tx_canal_3_toff
        self.ui.txQtdCiclosCanal_3.mousePressEvent = self.tx_canal_3_qtd
        self.ui.txPwmCanal_4.mousePressEvent = self.tx_canal_4_pwm
        self.ui.txPeriodoCanal_4.mousePressEvent = self.tx_canal_4_periodo_pwm
        self.ui.txTonCanal_4.mousePressEvent = self.tx_canal_4_ton
        self.ui.txToffCanal_4.mousePressEvent = self.tx_canal_4_toff
        self.ui.txQtdCiclosCanal_4.mousePressEvent = self.tx_canal_4_qtd

        self.ui.btSalvar.clicked.connect(self.salvar)

        self.config()

    def config(self):
        if self.npn_pnp == self.dado.CANAL_NPN:
            self.ui.lbTipoCanal.setText("Canal Transistor NPN")
            self.prog = self.dado.resgata_programa_tupla()
            start_index = 17
        else:
            self.ui.lbTipoCanal.setText("Canal Transistor PNP")
            self.prog = self.dado.resgata_programa_tupla()
            start_index = 1

        self.ui.txTonCanal_1.setText(str(self.prog[start_index]))
        self.ui.txToffCanal_1.setText(str(self.prog[start_index + 1]))
        self.ui.txQtdCiclosCanal_1.setText(str(self.prog[start_index + 2]))
        self.ui.txTonCanal_2.setText(str(self.prog[start_index + 3]))
        self.ui.txToffCanal_2.setText(str(self.prog[start_index + 4]))
        self.ui.txQtdCiclosCanal_2.setText(str(self.prog[start_index + 5]))
        self.ui.txTonCanal_3.setText(str(self.prog[start_index + 6]))
        self.ui.txToffCanal_3.setText(str(self.prog[start_index + 7]))
        self.ui.txQtdCiclosCanal_3.setText(str(self.prog[start_index + 8]))
        self.ui.txPwmCanal_4.setText(str(self.prog[start_index + 9]))
        self.ui.txPeriodoCanal_4.setText(str(self.prog[start_index + 10]))
        self.ui.txTonCanal_4.setText(str(self.prog[start_index + 11]))  
        self.ui.txToffCanal_4.setText(str(self.prog[start_index + 12]))
        self.ui.txQtdCiclosCanal_4.setText(str(self.prog[start_index + 13]))

        if self.prog[start_index + 14] == self.dado.BASE_TEMPO_SEGUNDOS:
            self.ui.rbtBaseSegundos.setChecked(True)
        else:
            self.ui.rbtBaseMinutos.setChecked(True)
        if self.prog[start_index + 15] == self.dado.HABILITA_CANAL:
            self.ui.ckbHabilitaModulo.setChecked(True)
        else:
            self.ui.ckbHabilitaModulo.setChecked(False)

    def tx_canal_1_ton(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txTonCanal_1.setText(teclado.line_edit.text())

    def tx_canal_1_toff(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txToffCanal_1.setText(teclado.line_edit.text())

    def tx_canal_1_qtd(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txQtdCiclosCanal_1.setText(teclado.line_edit.text())

    def tx_canal_2_ton(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txTonCanal_2.setText(teclado.line_edit.text())

    def tx_canal_2_toff(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txToffCanal_2.setText(teclado.line_edit.text())

    def tx_canal_2_qtd(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txQtdCiclosCanal_2.setText(teclado.line_edit.text())

    def tx_canal_3_ton(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txTonCanal_3.setText(teclado.line_edit.text())

    def tx_canal_3_toff(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txToffCanal_3.setText(teclado.line_edit.text())

    def tx_canal_3_qtd(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txQtdCiclosCanal_3.setText(teclado.line_edit.text())

    def tx_canal_4_pwm(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txPwmCanal_4.setText(teclado.line_edit.text())

    def tx_canal_4_periodo_pwm(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txPeriodoCanal_4.setText(teclado.line_edit.text())

    def tx_canal_4_ton(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txTonCanal_4.setText(teclado.line_edit.text())

    def tx_canal_4_toff(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txToffCanal_4.setText(teclado.line_edit.text())

    def tx_canal_4_qtd(self, event):
        teclado = NumericKeyboard(self.dado, type="text")
        teclado.exec_()
        self.ui.txQtdCiclosCanal_4.setText(teclado.line_edit.text())

    def salvar(self):
        # Check if all fields are filled
        required_fields = [
            self.ui.txTonCanal_1, self.ui.txToffCanal_1, self.ui.txQtdCiclosCanal_1,
            self.ui.txTonCanal_2, self.ui.txToffCanal_2, self.ui.txQtdCiclosCanal_2,
            self.ui.txTonCanal_3, self.ui.txToffCanal_3, self.ui.txQtdCiclosCanal_3,
            self.ui.txPwmCanal_4, self.ui.txPeriodoCanal_4, self.ui.txTonCanal_4, self.ui.txToffCanal_4, self.ui.txQtdCiclosCanal_4
        ]

        for field in required_fields:
            if not field.text():
                QMessageBox.warning(self, "Campos obrigatórios", "Por favor, preencha todos os campos.")
                return
        if self.npn_pnp == self.dado.CANAL_NPN:
            npn_base_tempo = self.dado.BASE_TEMPO_SEGUNDOS if self.ui.rbtBaseSegundos.isChecked() else self.dado.BASE_TEMPO_MINUTOS
            npn_habilita_desabilita = self.dado.HABILITA_CANAL if self.ui.ckbHabilitaModulo.isChecked() else self.dado.DESABILITA_CANAL 
            self.prog = self.dado.cria_programa_tupla(
                nome_programa=self.dado.nome_programa,
                pnp_canal1_ton=self.prog[1],
                pnp_canal1_toff=self.prog[2],
                pnp_canal1_qtd=self.prog[3],
                pnp_canal2_ton=self.prog[4],
                pnp_canal2_toff=self.prog[5],
                pnp_canal2_qtd=self.prog[6],
                pnp_canal3_ton=self.prog[7],
                pnp_canal3_toff=self.prog[8],
                pnp_canal3_qtd=self.prog[9],
                pnp_canal4_pwm=self.prog[10],
                pnp_canal4_periodo_pwm=self.prog[11],
                pnp_canal4_ton=self.prog[12],
                pnp_canal4_toff=self.prog[13],
                pnp_canal4_qtd=self.prog[14],
                pnp_base_tempo=self.prog[15],
                pnp_habilita_desabilita=self.prog[16],
                npn_canal1_ton=float(self.ui.txTonCanal_1.text()),
                npn_canal1_toff=float(self.ui.txToffCanal_1.text()),
                npn_canal1_qtd=int(self.ui.txQtdCiclosCanal_1.text()),
                npn_canal2_ton=float(self.ui.txTonCanal_2.text()),
                npn_canal2_toff=float(self.ui.txToffCanal_2.text()),
                npn_canal2_qtd=int(self.ui.txQtdCiclosCanal_2.text()),
                npn_canal3_ton=float(self.ui.txTonCanal_3.text()),
                npn_canal3_toff=float(self.ui.txToffCanal_3.text()),
                npn_canal3_qtd=int(self.ui.txQtdCiclosCanal_3.text()),
                npn_canal4_pwm=float(self.ui.txPwmCanal_4.text()),
                npn_canal4_periodo_pwm=float(self.ui.txPeriodoCanal_4.text()),
                npn_canal4_ton=float(self.ui.txTonCanal_4.text()),
                npn_canal4_toff=float(self.ui.txToffCanal_4.text()),
                npn_canal4_qtd=int(self.ui.txQtdCiclosCanal_4.text()),
                npn_base_tempo=npn_base_tempo,
                npn_habilita_desabilita=npn_habilita_desabilita,
                rele_canal1_ton=self.prog[33],
                rele_canal1_toff=self.prog[34],
                rele_canal1_qtd=self.prog[35],
                rele_canal2_ton=self.prog[36],
                rele_canal2_toff=self.prog[37],
                rele_canal2_qtd=self.prog[38],
                rele_canal3_ton=self.prog[39],
                rele_canal3_toff=self.prog[40],
                rele_canal3_qtd=self.prog[41],
                rele_canal4_ton=self.prog[42],
                rele_canal4_toff=self.prog[43],
                rele_canal4_qtd=self.prog[44],
                rele_base_tempo=self.prog[45],
                rele_habilita_desabilita=self.prog[46]
            )
            self.dado.salva_programa_tupla(self.prog)
            self.close()
        else:
            pnp_base_tempo = self.dado.BASE_TEMPO_SEGUNDOS if self.ui.rbtBaseSegundos.isChecked() else self.dado.BASE_TEMPO_MINUTOS
            pnp_habilita_desabilita = self.dado.HABILITA_CANAL if self.ui.ckbHabilitaModulo.isChecked() else self.dado.DESABILITA_CANAL 
            self.prog = self.dado.cria_programa_tupla(
                nome_programa=self.dado.nome_programa,
                pnp_canal1_ton=float(self.ui.txTonCanal_1.text()),
                pnp_canal1_toff=float(self.ui.txToffCanal_1.text()),
                pnp_canal1_qtd=int(self.ui.txQtdCiclosCanal_1.text()),
                pnp_canal2_ton=float(self.ui.txTonCanal_2.text()),
                pnp_canal2_toff=float(self.ui.txToffCanal_2.text()),
                pnp_canal2_qtd=int(self.ui.txQtdCiclosCanal_2.text()),
                pnp_canal3_ton=float(self.ui.txTonCanal_3.text()),
                pnp_canal3_toff=float(self.ui.txToffCanal_3.text()),
                pnp_canal3_qtd=int(self.ui.txQtdCiclosCanal_3.text()),
                pnp_canal4_pwm=float(self.ui.txPwmCanal_4.text()),
                pnp_canal4_periodo_pwm=float(self.ui.txPeriodoCanal_4.text()),
                pnp_canal4_ton=float(self.ui.txTonCanal_4.text()),
                pnp_canal4_toff=float(self.ui.txToffCanal_4.text()),
                pnp_canal4_qtd=int(self.ui.txQtdCiclosCanal_4.text()),
                pnp_base_tempo=pnp_base_tempo,
                pnp_habilita_desabilita=pnp_habilita_desabilita,
                npn_canal1_ton=self.prog[17],
                npn_canal1_toff=self.prog[18],
                npn_canal1_qtd=self.prog[19],
                npn_canal2_ton=self.prog[20],
                npn_canal2_toff=self.prog[21],
                npn_canal2_qtd=self.prog[22],
                npn_canal3_ton=self.prog[23],
                npn_canal3_toff=self.prog[24],
                npn_canal3_qtd=self.prog[25],
                npn_canal4_pwm=self.prog[26],
                npn_canal4_periodo_pwm=self.prog[27],
                npn_canal4_ton=self.prog[28],
                npn_canal4_toff=self.prog[29],
                npn_canal4_qtd=self.prog[30],
                npn_base_tempo=self.prog[31],
                npn_habilita_desabilita=self.prog[32],
                rele_canal1_ton=self.prog[33],
                rele_canal1_toff=self.prog[34],
                rele_canal1_qtd=self.prog[35],
                rele_canal2_ton=self.prog[36],
                rele_canal2_toff=self.prog[37],
                rele_canal2_qtd=self.prog[38],
                rele_canal3_ton=self.prog[39],
                rele_canal3_toff=self.prog[40],
                rele_canal3_qtd=self.prog[41],
                rele_canal4_ton=self.prog[42],
                rele_canal4_toff=self.prog[43],
                rele_canal4_qtd=self.prog[44],
                rele_base_tempo=self.prog[45],
                rele_habilita_desabilita=self.prog[46]
            )
            self.dado.salva_programa_tupla(self.prog)   
            self.close()

    def voltar(self):
        self.close()

    def closeEvent(self, event):
        event.accept()