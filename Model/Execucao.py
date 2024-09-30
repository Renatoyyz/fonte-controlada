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
        self.npn_canal2_contador = 1
        self.npn_canal3_contador = 1
        self.npn_canal4_contador = 1

        self.pnp_canal1_contador = 1
        self.pnp_canal2_contador = 1
        self.pnp_canal3_contador = 1
        self.pnp_canal4_contador = 1

        self.tempo_npn_decorrido_canal1 = 0
        self.tempo_npn_decorrido_canal2 = 0
        self.tempo_npn_decorrido_canal3 = 0
        self.tempo_npn_decorrido_canal4 = 0

        self.tempo_pnp_decorrido_canal1 = 0
        self.tempo_pnp_decorrido_canal2 = 0
        self.tempo_pnp_decorrido_canal3 = 0
        self.tempo_pnp_decorrido_canal4 = 0

        self.tempo_rele_decorrido_canal1 = 0
        self.tempo_rele_decorrido_canal2 = 0
        self.tempo_rele_decorrido_canal3 = 0
        self.tempo_rele_decorrido_canal4 = 0

        self.tempo_ligado_canal4 = 0
        self.tempo_desligado_canal4 = 0

        self.VERDE = "verde"
        self.CINZA = "cinza"

        # Variáveis para controle de tempo e estado
        self.tempo_decorrido = 0
        self.estado_cor_npn_1 = self.VERDE
        self.estado_cor_npn_2 = self.CINZA
        self.estado_cor_npn_3 = self.CINZA
        self.estado_cor_npn_4 = self.CINZA

        self.estado_cor_pnp_1 = self.CINZA
        self.estado_cor_pnp_2 = self.CINZA
        self.estado_cor_pnp_3 = self.CINZA
        self.estado_cor_pnp_4 = self.CINZA
        
        self.estado_cor_rele_1 = self.CINZA
        self.estado_cor_rele_2 = self.CINZA
        self.estado_cor_rele_3 = self.CINZA
        self.estado_cor_rele_4 = self.CINZA

        self.estado_ligado_canal4 = True

        # Variáveis carregadas do programa salvo
        self.npn_habilita_desabilita = None
        self.npn_base_tempo = None
        self.npn_canal1_ton = None
        self.npn_canal1_toff = None
        self.npn_canal1_qtd = None
        self.npn_canal2_ton = None
        self.npn_canal2_toff = None
        self.npn_canal2_qtd = None
        self.npn_canal3_ton = None
        self.npn_canal3_toff = None
        self.npn_canal3_qtd = None
        self.npn_pwm_canal4 = None
        self.npn_pwm_periodo_canal4 = None
        self.npn_canal4_ton = None
        self.npn_canal4_toff = None
        self.npn_canal4_qtd = None
        

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

    def config(self):
        self.programa_salvo = self.database.read(self.nome_programa)
        self.ui.lbNomeProg.setText(f"{self.nome_programa}: Parado")
        self.mudar_texto_label("lbNpn_qdt_1", f"{self.npn_canal1_contador} de {self.programa_salvo[0][4]}")
        self.mudar_texto_label("lbNpn_qdt_2", f"{self.npn_canal2_contador} de {self.programa_salvo[0][7]}")
        self.mudar_texto_label("lbNpn_qdt_3", f"{self.npn_canal3_contador} de {self.programa_salvo[0][10]}")
        self.mudar_texto_label("lbNpn_qdt_4", f"{self.npn_canal4_contador} de {self.programa_salvo[0][15]}")
        
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

        # Carregar variáveis do programa salvo
        self.npn_canal1_ton = self.programa_salvo[0][18]
        self.npn_canal1_toff = self.programa_salvo[0][19]
        self.npn_canal1_qtd = self.programa_salvo[0][20]
        self.npn_canal2_ton = self.programa_salvo[0][21]
        self.npn_canal2_toff = self.programa_salvo[0][22]
        self.npn_canal2_qtd = self.programa_salvo[0][23]
        self.npn_canal3_ton = self.programa_salvo[0][24]
        self.npn_canal3_toff = self.programa_salvo[0][25]
        self.npn_canal3_qtd = self.programa_salvo[0][26]
        self.npn_pwm_canal4 = self.programa_salvo[0][27]
        self.npn_pwm_periodo_canal4 = self.programa_salvo[0][28]
        self.npn_canal4_ton = self.programa_salvo[0][29]
        self.npn_canal4_toff = self.programa_salvo[0][30]
        self.npn_canal4_qtd = self.programa_salvo[0][31]

        self.npn_base_tempo = self.programa_salvo[0][32]
        self.npn_habilita_desabilita = self.programa_salvo[0][33]

    @QtCore.pyqtSlot()
    def atualizar_interface(self):
        if not self.programa_salvo:
            return

        if self.npn_habilita_desabilita == 1 and self.iniciado:
            self.ui.lbNomeProg.setText(f"{self.nome_programa}: Executando")
            incremento_canal1 = 0.1 if self.npn_base_tempo == 0 else 0.1 / 60  # Incrementa em 0.1 segundos ou 0.1 minutos
            incremento_canal2 = 0.1 if self.npn_base_tempo == 0 else 0.1 / 60
            incremento_canal3 = 0.1 if self.npn_base_tempo == 0 else 0.1 / 60
            incremento_canal4 = 0.1 if self.npn_base_tempo == 0 else 0.1 / 60

            ton_pwm = self.npn_pwm_periodo_canal4 * (self.npn_pwm_canal4 / 100)
            toff_pwm = self.npn_pwm_periodo_canal4 - ton_pwm

            # Canal 1
            if self.estado_cor_npn_1 == self.VERDE:
                self.tempo_npn_decorrido_canal1 += incremento_canal1
                self.io.npn_output(0, 1)
                if self.tempo_npn_decorrido_canal1 >= self.npn_canal1_ton:
                    self.tempo_npn_decorrido_canal1 = 0
                    self.mudar_cor_label("lbNpn_canal_1", self.CINZA)
                    self.estado_cor_npn_1 = self.CINZA
            else:
                self.tempo_npn_decorrido_canal1 += incremento_canal1
                self.io.npn_output(0, 0)
                if self.tempo_npn_decorrido_canal1 >= self.npn_canal1_toff:
                    self.tempo_npn_decorrido_canal1 = 0
                    self.mudar_cor_label("lbNpn_canal_1", self.VERDE)
                    self.estado_cor_npn_1 = self.VERDE

                    self.npn_canal1_contador += 1  # Incrementa o contador ao finalizar npn_canal1_toff

                    if self.npn_canal1_contador >= self.npn_canal1_qtd+1:
                        self.npn_canal1_contador = self.npn_canal1_qtd
                        self.mudar_cor_label("lbNpn_canal_1", self.CINZA)
        
                    self.mudar_texto_label("lbNpn_qdt_1", f"{self.npn_canal1_contador} de {self.npn_canal1_qtd}")

            # Canal 2
            if self.estado_cor_npn_2 == self.VERDE:
                self.tempo_npn_decorrido_canal2 += incremento_canal2
                self.io.npn_output(1, 1)
                if self.tempo_npn_decorrido_canal2 >= self.npn_canal2_ton:
                    self.tempo_npn_decorrido_canal2 = 0
                    self.mudar_cor_label("lbNpn_canal_2", self.CINZA)
                    self.estado_cor_npn_2 = self.CINZA
            else:
                self.tempo_npn_decorrido_canal2 += incremento_canal2
                self.io.npn_output(1, 0)
                if self.tempo_npn_decorrido_canal2 >= self.npn_canal2_toff:
                    self.tempo_npn_decorrido_canal2 = 0
                    self.mudar_cor_label("lbNpn_canal_2", self.VERDE)
                    self.estado_cor_npn_2 = self.VERDE

                    self.npn_canal2_contador += 1  # Incrementa o contador ao finalizar npn_canal2_toff

                    if self.npn_canal2_contador >= self.npn_canal2_qtd+1:
                        self.npn_canal2_contador = self.npn_canal2_qtd
                        self.mudar_cor_label("lbNpn_canal_2", self.CINZA)
        
                    self.mudar_texto_label("lbNpn_qdt_2", f"{self.npn_canal2_contador} de {self.npn_canal2_qtd}")

            # Canal 3
            if self.estado_cor_npn_3 == self.VERDE:
                self.tempo_npn_decorrido_canal3 += incremento_canal3
                self.io.npn_output(2, 1)
                if self.tempo_npn_decorrido_canal3 >= self.npn_canal3_ton:
                    self.tempo_npn_decorrido_canal3 = 0
                    self.mudar_cor_label("lbNpn_canal_3", self.CINZA)
                    self.estado_cor_npn_3 = self.CINZA
            else:
                self.tempo_npn_decorrido_canal3 += incremento_canal3
                self.io.npn_output(2, 0)
                if self.tempo_npn_decorrido_canal3 >= self.npn_canal3_toff:
                    self.tempo_npn_decorrido_canal3 = 0
                    self.mudar_cor_label("lbNpn_canal_3", self.VERDE)
                    self.estado_cor_npn_3 = self.VERDE

                    self.npn_canal3_contador += 1  # Incrementa o contador ao finalizar npn_canal3_toff

                    if self.npn_canal3_contador >= self.npn_canal3_qtd+1:
                        self.npn_canal3_contador = self.npn_canal3_qtd
                        self.mudar_cor_label("lbNpn_canal_3", self.CINZA)
        
                    self.mudar_texto_label("lbNpn_qdt_3", f"{self.npn_canal3_contador} de {self.npn_canal3_qtd}")

            # Canal 4
            if self.estado_ligado_canal4:
                if self.estado_cor_npn_4 == self.VERDE:
                    self.tempo_npn_decorrido_canal4 += incremento_canal4
                    self.io.npn_output(3, 1)
                    if self.tempo_npn_decorrido_canal4 >= ton_pwm:
                        self.tempo_npn_decorrido_canal4 = 0
                        self.mudar_cor_label("lbNpn_canal_4", self.CINZA)
                        self.estado_cor_npn_4 = self.CINZA
                else:
                    self.tempo_npn_decorrido_canal4 += incremento_canal4
                    self.io.npn_output(3, 0)
                    if self.tempo_npn_decorrido_canal4 >= toff_pwm:
                        self.tempo_npn_decorrido_canal4 = 0
                        self.mudar_cor_label("lbNpn_canal_4", self.VERDE)
                        self.estado_cor_npn_4 = self.VERDE

                self.tempo_ligado_canal4 += incremento_canal4
                if self.tempo_ligado_canal4 >= self.npn_canal4_ton * 60:  # Convertendo minutos para segundos
                    self.tempo_ligado_canal4 = 0
                    self.estado_ligado_canal4 = False
                    
                    if self.npn_canal4_contador >= self.npn_canal4_qtd+1:
                        self.npn_canal4_contador = self.npn_canal4_qtd
                        self.mudar_cor_label("lbNpn_canal_4", self.CINZA)

                self.mudar_texto_label("lbNpn_qdt_4", f"{self.npn_canal4_contador} de {self.npn_canal4_qtd}")
            else:
                self.tempo_desligado_canal4 += incremento_canal4
                if self.tempo_desligado_canal4 >= self.npn_canal4_toff * 60:  # Convertendo minutos para segundos
                    self.tempo_desligado_canal4 = 0
                    self.estado_ligado_canal4 = True
                    self.npn_canal4_contador += 1  # Incrementa o contador ao finalizar o tempo ligado

                self.mudar_cor_label("lbNpn_canal_4", self.CINZA)
                self.io.npn_output(3, 0)


        else:
            self.io.npn_output(0, 0)
            self.io.npn_output(1, 0)
            self.io.npn_output(2, 0)
            self.io.npn_output(3, 0)

            self.ui.lbNomeProg.setText(f"{self.nome_programa}: Parado")

        if self.npn_canal1_contador >= self.npn_canal1_qtd and self.npn_canal2_contador >= self.npn_canal2_qtd and self.npn_canal3_contador >= self.npn_canal3_qtd and self.npn_canal4_contador >= self.npn_canal4_qtd+1:
            self.iniciado = False
            self.ui.btIniciarPausar.setText("Iniciar")

            self.mudar_texto_label("lbNpn_qdt_1", f"{self.npn_canal1_contador} de {self.npn_canal1_qtd}")
            self.mudar_texto_label("lbNpn_qdt_2", f"{self.npn_canal2_contador} de {self.npn_canal2_qtd}")
            self.mudar_texto_label("lbNpn_qdt_3", f"{self.npn_canal3_contador} de {self.npn_canal3_qtd}")
            self.mudar_texto_label("lbNpn_qdt_4", f"{self.npn_canal4_contador-1} de {self.npn_canal4_qtd}")   

            self.tempo_npn_decorrido_canal1 = 0
            self.tempo_npn_decorrido_canal2 = 0
            self.tempo_npn_decorrido_canal3 = 0
            self.tempo_npn_decorrido_canal4 = 0

            self.npn_canal1_contador = 1
            self.npn_canal2_contador = 1
            self.npn_canal3_contador = 1
            self.npn_canal4_contador = 1

            self.estado_cor_npn_1 = self.CINZA
            self.estado_cor_npn_2 = self.CINZA
            self.estado_cor_npn_3 = self.CINZA
            self.estado_cor_npn_4 = self.CINZA
            self.estado_cor_pnp_1 = self.CINZA
            self.estado_cor_pnp_2 = self.CINZA
            self.estado_cor_pnp_3 = self.CINZA
            self.estado_cor_pnp_4 = self.CINZA
            self.estado_cor_rele_1 = self.CINZA
            self.estado_cor_rele_2 = self.CINZA
            self.estado_cor_rele_3 = self.CINZA
            self.estado_cor_rele_4 = self.CINZA

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

            QMessageBox.information(self, "Fim do programa", "Programa finalizado com sucesso.")

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

    def voltar(self):
        self.close()

    def iniciar_pausar(self):
        self.iniciado = not self.iniciado
        if self.iniciado:

            self.mudar_texto_label("lbNpn_qdt_1", f"{self.npn_canal1_contador} de {self.npn_canal1_qtd}")
            self.mudar_texto_label("lbNpn_qdt_2", f"{self.npn_canal2_contador} de {self.npn_canal2_qtd}")
            self.mudar_texto_label("lbNpn_qdt_3", f"{self.npn_canal3_contador} de {self.npn_canal3_qtd}")
            self.mudar_texto_label("lbNpn_qdt_4", f"{self.npn_canal4_contador} de {self.npn_canal4_qtd}")

            self.ui.btIniciarPausar.setText("Pausar")
            self.estado_cor_npn_1 = self.VERDE
            self.estado_cor_npn_2 = self.VERDE
            self.estado_cor_npn_3 = self.VERDE
            self.estado_cor_npn_4 = self.VERDE
            self.estado_cor_pnp_1 = self.VERDE
            self.estado_cor_pnp_2 = self.VERDE
            self.estado_cor_pnp_3 = self.VERDE
            self.estado_cor_pnp_4 = self.VERDE
            self.estado_cor_rele_1 = self.VERDE
            self.estado_cor_rele_2 = self.VERDE
            self.estado_cor_rele_3 = self.VERDE
            self.estado_cor_rele_4 = self.VERDE

            self.mudar_cor_label("lbNpn_canal_1", self.VERDE)
            self.mudar_cor_label("lbNpn_canal_2", self.VERDE)
            self.mudar_cor_label("lbNpn_canal_3", self.VERDE)
            self.mudar_cor_label("lbNpn_canal_4", self.VERDE)
            self.mudar_cor_label("lbPnp_canal_1", self.VERDE)
            self.mudar_cor_label("lbPnp_canal_2", self.VERDE)
            self.mudar_cor_label("lbPnp_canal_3", self.VERDE)
            self.mudar_cor_label("lbPnp_canal_4", self.VERDE)
            self.mudar_cor_label("lbRele_canal_1", self.VERDE)
            self.mudar_cor_label("lbRele_canal_2", self.VERDE)
            self.mudar_cor_label("lbRele_canal_3", self.VERDE)
            self.mudar_cor_label("lbRele_canal_4", self.VERDE)
        else:
            self.ui.btIniciarPausar.setText("Iniciar")
    
    def closeEvent(self, event):
        self.atualizador.stop()
        self.atualizador.wait()
        event.accept()