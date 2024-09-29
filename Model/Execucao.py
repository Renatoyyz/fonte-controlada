from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import Qt
from View.execucao import Ui_frmExecucao

class Atualizador(QtCore.QThread):
    atualizacao = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = False

    def run(self):
        while self.running:
            self.atualizacao.emit()
            self.msleep(100)

    def inicia(self):
        self.running = True

    def stop(self):
        self.running = False

class Execucao(QDialog):
    def __init__(self, dado, io, db, nome_programa):
        super().__init__()
        self.dado = dado
        self.io = io
        self.database = db
        self.nome_programa = nome_programa
        self.programa_salvo = None
        self.iniciado = False
        self.npn_canal1_contador = 1

        self.VERDE = "verde"
        self.CINZA = "cinza"

        # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_frmExecucao()
        self.ui.setupUi(self)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Maximizar a janela
        if self.dado.full_scream == True:
            self.setWindowState(Qt.WindowState.WindowFullScreen)

        self.ui.btVoltar.clicked.connect(self.voltar)
        self.ui.btIniciarPausar.clicked.connect(self.iniciar_pausar)

        # Configuração do Atualizador
        self.atualizador = Atualizador()
        self.atualizador.atualizacao.connect(self.atualizar_interface)
        self.atualizador.inicia()
        self.atualizador.start()

        self.config()

        # Variáveis para controle de tempo e estado
        self.tempo_decorrido = 0
        self.estado_cor = self.VERDE

    def config(self):
        self.programa_salvo = self.database.read(self.nome_programa)
        self.ui.lbNomeProg.setText(self.nome_programa)
        self.mudar_texto_label("lbNpn_qdt_1", f"{self.npn_canal1_contador} de {self.programa_salvo[0][4]}")
        self.mudar_cor_label("lbNpn_canal_1", self.CINZA)
        self.mudar_cor_label("lbNpn_canal_2", self.CINZA)
        self.mudar_cor_label("lbNpn_canal_3", self.CINZA)
        self.mudar_cor_label("lbNpn_canal_4", self.CINZA)
        self.mudar_cor_label("lbPnp_canal_1", self.CINZA)
        self.mudar_cor_label("lbPnp_canal_2", self.CINZA)
        self.mudar_cor_label("lbPnp_canal_3", self.CINZA)
        self.mudar_cor_label("lbPnp_canal_4", self.CINZA)
        self.mudar_cor_label("lbRele_canal_1", self.CINZA)
        self.mudar_cor_label("lbRele_canal_2", self.CINZA)
        self.mudar_cor_label("lbRele_canal_3", self.CINZA)
        self.mudar_cor_label("lbRele_canal_4", self.CINZA)

    
    @QtCore.pyqtSlot()
    def atualizar_interface(self):
        if not self.programa_salvo:
            return
        
        npn_habilita_desabilita = self.programa_salvo[0][15]
        npn_base_tempo = self.programa_salvo[0][14]
        npn_canal1_ton = self.programa_salvo[0][2]
        npn_canal1_toff = self.programa_salvo[0][3]
        npn_canal1_qtd = self.programa_salvo[0][4]

        if npn_habilita_desabilita == 1 and self.iniciado:
            incremento = 0.1 if npn_base_tempo == 0 else 0.1 / 60  # Incrementa em 0.1 segundos ou 0.1 minutos

            if self.estado_cor == self.VERDE:
                self.tempo_decorrido += incremento
                self.io.npn_output(0, 1)
                if self.tempo_decorrido >= npn_canal1_ton:
                    self.tempo_decorrido = 0
                    self.mudar_cor_label("lbNpn_canal_1", self.CINZA)
                    self.estado_cor = self.CINZA
            else:
                self.tempo_decorrido += incremento
                self.io.npn_output(0, 0)
                if self.tempo_decorrido >= npn_canal1_toff:
                    self.tempo_decorrido = 0
                    self.mudar_cor_label("lbNpn_canal_1", self.VERDE)
                    self.estado_cor = self.VERDE

                    # Atualiza o texto do label com o ciclo atual

                    self.npn_canal1_contador += 1  # Incrementa o contador ao finalizar npn_canal1_toff

                    if self.npn_canal1_contador > npn_canal1_qtd:
                        self.iniciado = False
                        self.npn_canal1_contador = 10
                        self.mudar_cor_label("lbNpn_canal_1", self.CINZA)
        
                    self.mudar_texto_label("lbNpn_qdt_1", f"{self.npn_canal1_contador} de {npn_canal1_qtd}")
        else:
            self.io.npn_output(0, 0)
            self.tempo_decorrido = 0
            self.mudar_cor_label("lbNpn_canal_1", self.CINZA)
            self.estado_cor = self.CINZA

    def mudar_cor_label(self, label_name, cor):
        label = getattr(self.ui, label_name, None)
        if label:
            if cor == self.VERDE:
                label.setStyleSheet("background-color: rgb(33, 255, 6);")
            elif cor == self.CINZA:
                label.setStyleSheet("background-color: rgb(184, 184, 184);")
            else:
                raise ValueError("Cor inválida. Use 'verde' ou 'vermelho'.")
            
    def mudar_texto_label(self, label_name, texto):
        label = getattr(self.ui, label_name, None)
        if label:
            label.setText(texto)
        else:
            raise AttributeError(f"Label '{label_name}' não encontrado.")

    def exemplo_uso(self):
        self.mudar_cor_label("lbNpn_canal_1", "verde")
        self.mudar_cor_label("lbNpn_canal_2", "vermelho")

    def voltar(self):
        self.close()

    def iniciar_pausar(self):
        self.iniciado = not self.iniciado
        if self.iniciado:
            self.ui.btIniciarPausar.setText("Pausar")
            self.estado_cor = self.VERDE
            self.mudar_cor_label("lbNpn_canal_1", self.estado_cor)
        else:
            self.ui.btIniciarPausar.setText("Iniciar")
    
    def closeEvent(self, event):
        self.atualizador.stop()
        self.atualizador.wait()
        event.accept()