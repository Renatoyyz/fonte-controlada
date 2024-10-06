from PyQt5 import QtCore, QtGui
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
        self.iniciado_npn = False
        self.iniciado_pnp = False
        self.iniciado_rele = False

        self.oscila_msg = False
        self.cnt_osciala = 0

        self.fim_npn = False
        self.fim_pnp = False
        self.fim_rele = False

        self.npn_canal1_contador = 1
        self.npn_canal2_contador = 1
        self.npn_canal3_contador = 1
        self.npn_canal4_contador = 1

        self.pnp_canal1_contador = 1
        self.pnp_canal2_contador = 1
        self.pnp_canal3_contador = 1
        self.pnp_canal4_contador = 1

        self.rele_canal1_contador = 1
        self.rele_canal2_contador = 1
        self.rele_canal3_contador = 1
        self.rele_canal4_contador = 1

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

        self.tempo_ligado_canal4_npn = 0
        self.tempo_ligado_canal4_pnp = 0
        self.tempo_desligado_canal4_npn = 0
        self.tempo_desligado_canal4_pnp = 0

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

        self.estado_ligado_canal4_npn = True
        self.estado_ligado_canal4_pnp = True

        # Variáveis carregadas do programa salvo
        self.npn_habilita_desabilita = None
        self.pnp_habilita_desabilita = None
        self.rele_habilita_desabilita = None

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
        self.mudar_texto_label("lbNpn_qdt_1", f"{self.npn_canal1_contador} de {self.programa_salvo[0][20]}")
        self.mudar_texto_label("lbNpn_qdt_2", f"{self.npn_canal2_contador} de {self.programa_salvo[0][23]}")
        self.mudar_texto_label("lbNpn_qdt_3", f"{self.npn_canal3_contador} de {self.programa_salvo[0][26]}")
        self.mudar_texto_label("lbNpn_qdt_4", f"{self.npn_canal4_contador} de {self.programa_salvo[0][31]}")
        self.mudar_texto_label("lbPnp_qdt_1", f"{self.pnp_canal1_contador} de {self.programa_salvo[0][4]}")
        self.mudar_texto_label("lbPnp_qdt_2", f"{self.pnp_canal2_contador} de {self.programa_salvo[0][7]}")
        self.mudar_texto_label("lbPnp_qdt_3", f"{self.pnp_canal3_contador} de {self.programa_salvo[0][10]}")
        self.mudar_texto_label("lbPnp_qdt_4", f"{self.pnp_canal4_contador} de {self.programa_salvo[0][15]}")
        self.mudar_texto_label("lbRele_qdt_1", f"{self.rele_canal1_contador} de {self.programa_salvo[0][36]}")
        self.mudar_texto_label("lbRele_qdt_2", f"{self.rele_canal2_contador} de {self.programa_salvo[0][39]}")
        self.mudar_texto_label("lbRele_qdt_3", f"{self.rele_canal3_contador} de {self.programa_salvo[0][42]}")
        self.mudar_texto_label("lbRele_qdt_4", f"{self.rele_canal4_contador} de {self.programa_salvo[0][45]}")
    
        
        self.mudar_cor_label("lbNpn_canal_1", self.CINZA)
        self.estado_cor_npn_1 = self.CINZA
        self.mudar_cor_label("lbNpn_canal_2", self.CINZA)
        self.estado_cor_npn_2 = self.CINZA
        self.mudar_cor_label("lbNpn_canal_3", self.CINZA)
        self.estado_cor_npn_3 = self.CINZA
        self.mudar_cor_label("lbNpn_canal_4", self.CINZA)
        self.estado_cor_npn_4 = self.CINZA
        self.mudar_cor_label("lbPnp_canal_1", self.CINZA)
        self.estado_cor_pnp_1 = self.CINZA
        self.mudar_cor_label("lbPnp_canal_2", self.CINZA)
        self.estado_cor_pnp_2 = self.CINZA
        self.mudar_cor_label("lbPnp_canal_3", self.CINZA)
        self.estado_cor_pnp_3 = self.CINZA
        self.mudar_cor_label("lbPnp_canal_4", self.CINZA)
        self.estado_cor_pnp_4 = self.CINZA
        self.mudar_cor_label("lbRele_canal_1", self.CINZA)
        self.estado_cor_rele_1 = self.CINZA
        self.mudar_cor_label("lbRele_canal_2", self.CINZA)
        self.estado_cor_rele_2 = self.CINZA
        self.mudar_cor_label("lbRele_canal_3", self.CINZA)
        self.estado_cor_rele_3 = self.CINZA
        self.mudar_cor_label("lbRele_canal_4", self.CINZA)
        self.estado_cor_rele_4 = self.CINZA

        # Carregar variáveis do programa salvo
        self.pnp_canal1_ton = self.programa_salvo[0][2]
        self.pnp_canal1_toff = self.programa_salvo[0][3]
        self.pnp_canal1_qtd = self.programa_salvo[0][4]
        self.pnp_canal2_ton = self.programa_salvo[0][5]
        self.pnp_canal2_toff = self.programa_salvo[0][6]
        self.pnp_canal2_qtd = self.programa_salvo[0][7]
        self.pnp_canal3_ton = self.programa_salvo[0][8]
        self.pnp_canal3_toff = self.programa_salvo[0][9]
        self.pnp_canal3_qtd = self.programa_salvo[0][10]
        self.pnp_pwm_canal4 = self.programa_salvo[0][11]
        self.pnp_pwm_periodo_canal4 = self.programa_salvo[0][12]
        self.pnp_canal4_ton = self.programa_salvo[0][13]
        self.pnp_canal4_toff = self.programa_salvo[0][14]
        self.pnp_canal4_qtd = self.programa_salvo[0][15]
        self.pnp_base_tempo = self.programa_salvo[0][16]
        self.pnp_habilita_desabilita = self.programa_salvo[0][17]

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

        self.rele_canal1_ton = self.programa_salvo[0][34]
        self.rele_canal1_toff = self.programa_salvo[0][35]
        self.rele_canal1_qtd = self.programa_salvo[0][36]
        self.rele_canal2_ton = self.programa_salvo[0][37]
        self.rele_canal2_toff = self.programa_salvo[0][38]
        self.rele_canal2_qtd = self.programa_salvo[0][39]
        self.rele_canal3_ton = self.programa_salvo[0][40]
        self.rele_canal3_toff = self.programa_salvo[0][41]
        self.rele_canal3_qtd = self.programa_salvo[0][42]
        self.rele_canal4_ton = self.programa_salvo[0][43]
        self.rele_canal4_toff = self.programa_salvo[0][44]
        self.rele_canal4_qtd = self.programa_salvo[0][45]
        self.rele_base_tempo = self.programa_salvo[0][46]
        self.rele_habilita_desabilita = self.programa_salvo[0][47]


    @QtCore.pyqtSlot()
    def atualizar_interface(self):
        if self.npn_habilita_desabilita == 1 and self.iniciado_npn and self.fim_npn==False:
            self.executa_canal_npn()
        else:
            if self.npn_habilita_desabilita == 0:
                self.fim_npn = True
            self.mudar_cor_label("lbNpn_canal_1", self.CINZA)
            self.estado_cor_npn_1 = self.CINZA
            self.io.npn_output(0, 0)
            self.mudar_cor_label("lbNpn_canal_2", self.CINZA)
            self.estado_cor_npn_2 = self.CINZA
            self.io.npn_output(1, 0)
            self.mudar_cor_label("lbNpn_canal_3", self.CINZA)
            self.estado_cor_npn_3 = self.CINZA
            self.io.npn_output(2, 0)
            self.mudar_cor_label("lbNpn_canal_4", self.CINZA)
            self.estado_cor_npn_4 = self.CINZA
            self.io.npn_output(3, 0)
        if self.pnp_habilita_desabilita == 1 and self.iniciado_pnp and self.fim_pnp==False:
            self.executa_canal_pnp()
        else:
            if self.pnp_habilita_desabilita == 0:
                self.fim_pnp = True
            self.mudar_cor_label("lbPnp_canal_1", self.CINZA)
            self.estado_cor_pnp_1 = self.CINZA
            self.io.pnp_output(0, 0)
            self.mudar_cor_label("lbPnp_canal_2", self.CINZA)
            self.estado_cor_pnp_2 = self.CINZA
            self.io.pnp_output(1, 0)
            self.mudar_cor_label("lbPnp_canal_3", self.CINZA)
            self.estado_cor_pnp_3 = self.CINZA
            self.io.pnp_output(2, 0)
            self.mudar_cor_label("lbPnp_canal_4", self.CINZA)
            self.estado_cor_pnp_4 = self.CINZA
            self.io.pnp_output(3, 0)
        if self.rele_habilita_desabilita == 1 and self.iniciado_rele and self.fim_rele==False:
            self.executa_canal_rele()
        else:
            if self.rele_habilita_desabilita == 0:
                self.fim_rele = True
            self.mudar_cor_label("lbRele_canal_1", self.CINZA)
            self.estado_cor_rele_1 = self.CINZA
            self.io.relay_output(0, 0)
            self.mudar_cor_label("lbRele_canal_2", self.CINZA)
            self.estado_cor_rele_2 = self.CINZA
            self.io.relay_output(1, 0)
            self.mudar_cor_label("lbRele_canal_3", self.CINZA)
            self.estado_cor_rele_3 = self.CINZA
            self.io.relay_output(2, 0)
            self.mudar_cor_label("lbRele_canal_4", self.CINZA)
            self.estado_cor_rele_4 = self.CINZA
            self.io.relay_output(3, 0)

        if self.fim_npn and self.fim_pnp and self.fim_rele:
            self.fim_npn = False
            self.fim_pnp = False
            self.fim_rele = False
            self.ui.lbNomeProg.setText(f"{self.nome_programa}: Parado")
            self.ui.btIniciarPausar.setText("Iniciar")
            QMessageBox.information(self, "Fim do Programa", "Programa finalizado com sucesso!")

    def executa_canal_npn(self):
        if not self.programa_salvo:
            return

        if self.npn_habilita_desabilita == 1 and self.iniciado_npn and self.fim_npn==False:
            self.oscila_executando()
            incremento_canal1 = 0.1 if self.npn_base_tempo == 0 else 0.1 / 60  # Incrementa em 0.1 segundos ou 0.1 minutos
            incremento_canal2 = 0.1 if self.npn_base_tempo == 0 else 0.1 / 60
            incremento_canal3 = 0.1 if self.npn_base_tempo == 0 else 0.1 / 60
            incremento_canal4 = 0.1  # Incrementa em 0.1 segundos

            ton_pwm = self.npn_pwm_periodo_canal4 * (self.npn_pwm_canal4 / 100)
            toff_pwm = self.npn_pwm_periodo_canal4 - ton_pwm

            # Canal 1
            if self.npn_canal1_contador < self.npn_canal1_qtd:
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
                            self.estado_cor_npn_1 = self.CINZA
            
                        self.mudar_texto_label("lbNpn_qdt_1", f"{self.npn_canal1_contador} de {self.npn_canal1_qtd}")
            else:
                self.mudar_cor_label("lbNpn_canal_1", self.CINZA)
                self.estado_cor_npn_1 = self.CINZA
                self.io.npn_output(0, 0)

            # Canal 2
            if self.npn_canal2_contador < self.npn_canal2_qtd:
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
                            self.estado_cor_npn_2 = self.CINZA
            
                        self.mudar_texto_label("lbNpn_qdt_2", f"{self.npn_canal2_contador} de {self.npn_canal2_qtd}")
            else:
                self.mudar_cor_label("lbNpn_canal_2", self.CINZA)
                self.estado_cor_npn_2 = self.CINZA
                self.io.npn_output(1, 0)

            # Canal 3
            if self.npn_canal3_contador < self.npn_canal3_qtd:
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
                            self.estado_cor_npn_3 = self.CINZA
            
                        self.mudar_texto_label("lbNpn_qdt_3", f"{self.npn_canal3_contador} de {self.npn_canal3_qtd}")
            else:
                self.mudar_cor_label("lbNpn_canal_3", self.CINZA)
                self.estado_cor_npn_3 = self.CINZA
                self.io.npn_output(2, 0)    

            # Canal 4
            if self.npn_canal4_contador < self.npn_canal4_qtd + 1:
                if self.estado_ligado_canal4_npn:
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

                    self.tempo_ligado_canal4_npn += incremento_canal4
                    if self.tempo_ligado_canal4_npn >= self.npn_canal4_ton * 60:  # Convertendo minutos para segundos
                        self.tempo_ligado_canal4_npn = 0
                        self.estado_ligado_canal4_npn = False
                        
                        if self.npn_canal4_contador >= self.npn_canal4_qtd+1:
                            self.npn_canal4_contador = self.npn_canal4_qtd
                            self.mudar_cor_label("lbNpn_canal_4", self.CINZA)
                            self.estado_cor_npn_4 = self.CINZA

                    self.mudar_texto_label("lbNpn_qdt_4", f"{self.npn_canal4_contador} de {self.npn_canal4_qtd}")
                else:
                    self.tempo_desligado_canal4_npn += incremento_canal4
                    if self.tempo_desligado_canal4_npn >= self.npn_canal4_toff * 60:  # Convertendo minutos para segundos
                        self.tempo_desligado_canal4_npn = 0
                        self.estado_ligado_canal4_npn = True
                        self.npn_canal4_contador += 1  # Incrementa o contador ao finalizar o tempo ligado

                    self.mudar_cor_label("lbNpn_canal_4", self.CINZA)
                    self.estado_cor_npn_4 = self.CINZA
                    self.io.npn_output(3, 0)
            else:
                self.mudar_cor_label("lbNpn_canal_4", self.CINZA)
                self.estado_cor_npn_4 = self.CINZA
                self.io.npn_output(3, 0)


        else:
            self.io.npn_output(0, 0)
            self.io.npn_output(1, 0)
            self.io.npn_output(2, 0)
            self.io.npn_output(3, 0)

            self.ui.lbNomeProg.setText(f"{self.nome_programa}: Parado")

        if self.npn_canal1_contador >= self.npn_canal1_qtd and self.npn_canal2_contador >= self.npn_canal2_qtd and self.npn_canal3_contador >= self.npn_canal3_qtd and self.npn_canal4_contador >= self.npn_canal4_qtd+1:
            self.iniciado_npn = False

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

            self.mudar_cor_label("lbNpn_canal_1", self.CINZA)
            self.estado_cor_npn_1 = self.CINZA
            self.mudar_cor_label("lbNpn_canal_2", self.CINZA)
            self.estado_cor_npn_2 = self.CINZA
            self.mudar_cor_label("lbNpn_canal_3", self.CINZA)
            self.estado_cor_npn_3 = self.CINZA
            self.mudar_cor_label("lbNpn_canal_4", self.CINZA)
            self.estado_cor_npn_4 = self.CINZA

            self.fim_npn = True # Indica que o programa NPN terminou

    def executa_canal_pnp(self):
        if not self.programa_salvo:
            return

        if self.pnp_habilita_desabilita == 1 and self.iniciado_pnp and self.fim_pnp==False:
            self.oscila_executando()
            incremento_canal1 = 0.1 if self.pnp_base_tempo == 0 else 0.1 / 60  # Incrementa em 0.1 segundos ou 0.1 minutos
            incremento_canal2 = 0.1 if self.pnp_base_tempo == 0 else 0.1 / 60
            incremento_canal3 = 0.1 if self.pnp_base_tempo == 0 else 0.1 / 60
            incremento_canal4 = 0.1 # Incrementa em 0.1 segundos

            ton_pwm = self.pnp_pwm_periodo_canal4 * (self.npn_pwm_canal4 / 100)
            toff_pwm = self.pnp_pwm_periodo_canal4 - ton_pwm

            # Canal 1
            if self.pnp_canal1_contador < self.pnp_canal1_qtd:
                if self.estado_cor_pnp_1 == self.VERDE:
                    self.tempo_pnp_decorrido_canal1 += incremento_canal1
                    self.io.pnp_output(0, 1)
                    if self.tempo_pnp_decorrido_canal1 >= self.pnp_canal1_ton:
                        self.tempo_pnp_decorrido_canal1 = 0
                        self.mudar_cor_label("lbPnp_canal_1", self.CINZA)
                        self.estado_cor_pnp_1 = self.CINZA
                else:
                    self.tempo_pnp_decorrido_canal1 += incremento_canal1
                    self.io.pnp_output(0, 0)
                    if self.tempo_pnp_decorrido_canal1 >= self.pnp_canal1_toff:
                        self.tempo_pnp_decorrido_canal1 = 0
                        self.mudar_cor_label("lbPnp_canal_1", self.VERDE)
                        self.estado_cor_pnp_1 = self.VERDE

                        self.pnp_canal1_contador += 1  # Incrementa o contador ao finalizar pnp_canal1_toff

                        if self.pnp_canal1_contador >= self.pnp_canal1_qtd + 1:
                            self.pnp_canal1_contador = self.pnp_canal1_qtd
                            self.mudar_cor_label("lbPnp_canal_1", self.CINZA)
                            self.estado_cor_pnp_1 = self.CINZA

                        self.mudar_texto_label("lbPnp_qdt_1", f"{self.pnp_canal1_contador} de {self.pnp_canal1_qtd}")
            else:
                self.mudar_cor_label("lbPnp_canal_1", self.CINZA)
                self.estado_cor_pnp_1 = self.CINZA
                self.io.pnp_output(0, 0)


            # Canal 2
            if self.pnp_canal2_contador < self.pnp_canal2_qtd:
                if self.estado_cor_pnp_2 == self.VERDE:
                    self.tempo_pnp_decorrido_canal2 += incremento_canal2
                    self.io.pnp_output(1, 1)
                    if self.tempo_pnp_decorrido_canal2 >= self.pnp_canal2_ton:
                        self.tempo_pnp_decorrido_canal2 = 0
                        self.mudar_cor_label("lbPnp_canal_2", self.CINZA)
                        self.estado_cor_pnp_2 = self.CINZA
                else:
                    self.tempo_pnp_decorrido_canal2 += incremento_canal2
                    self.io.pnp_output(1, 0)
                    if self.tempo_pnp_decorrido_canal2 >= self.pnp_canal2_toff:
                        self.tempo_pnp_decorrido_canal2 = 0
                        self.mudar_cor_label("lbPnp_canal_2", self.VERDE)
                        self.estado_cor_pnp_2 = self.VERDE

                        self.pnp_canal2_contador += 1  # Incrementa o contador ao finalizar pnp_canal2_toff

                        if self.pnp_canal2_contador >= self.pnp_canal2_qtd + 1:
                            self.pnp_canal2_contador = self.pnp_canal2_qtd
                            self.mudar_cor_label("lbPnp_canal_2", self.CINZA)
                            self.estado_cor_pnp_2 = self.CINZA

                        self.mudar_texto_label("lbPnp_qdt_2", f"{self.pnp_canal2_contador} de {self.pnp_canal2_qtd}")
            else:
                self.mudar_cor_label("lbPnp_canal_2", self.CINZA)
                self.estado_cor_pnp_2 = self.CINZA
                self.io.pnp_output(1, 0)

            # Canal 3
            if self.pnp_canal3_contador < self.pnp_canal3_qtd:
                if self.estado_cor_pnp_3 == self.VERDE:
                    self.tempo_pnp_decorrido_canal3 += incremento_canal3
                    self.io.pnp_output(2, 1)
                    if self.tempo_pnp_decorrido_canal3 >= self.pnp_canal3_ton:
                        self.tempo_pnp_decorrido_canal3 = 0
                        self.mudar_cor_label("lbPnp_canal_3", self.CINZA)
                        self.estado_cor_pnp_3 = self.CINZA
                else:
                    self.tempo_pnp_decorrido_canal3 += incremento_canal3
                    self.io.pnp_output(2, 0)
                    if self.tempo_pnp_decorrido_canal3 >= self.pnp_canal3_toff:
                        self.tempo_pnp_decorrido_canal3 = 0
                        self.mudar_cor_label("lbPnp_canal_3", self.VERDE)
                        self.estado_cor_pnp_3 = self.VERDE

                        self.pnp_canal3_contador += 1  # Incrementa o contador ao finalizar pnp_canal3_toff

                        if self.pnp_canal3_contador >= self.pnp_canal3_qtd + 1:
                            self.pnp_canal3_contador = self.pnp_canal3_qtd
                            self.mudar_cor_label("lbPnp_canal_3", self.CINZA)
                            self.estado_cor_pnp_3 = self.CINZA

                        self.mudar_texto_label("lbPnp_qdt_3", f"{self.pnp_canal3_contador} de {self.pnp_canal3_qtd}")
            else:
                self.mudar_cor_label("lbPnp_canal_3", self.CINZA)
                self.estado_cor_pnp_3 = self.CINZA
                self.io.pnp_output(2, 0)

            # Canal 4
            if self.pnp_canal4_contador < self.pnp_canal4_qtd + 1:
                if self.estado_ligado_canal4_pnp:
                    if self.estado_cor_pnp_4 == self.VERDE:
                        self.tempo_pnp_decorrido_canal4 += incremento_canal4
                        self.io.pnp_output(3, 1)
                        if self.tempo_pnp_decorrido_canal4 >= ton_pwm:
                            self.tempo_pnp_decorrido_canal4 = 0
                            self.mudar_cor_label("lbPnp_canal_4", self.CINZA)
                            self.estado_cor_pnp_4 = self.CINZA
                    else:
                        self.tempo_pnp_decorrido_canal4 += incremento_canal4
                        self.io.pnp_output(3, 0)
                        if self.tempo_pnp_decorrido_canal4 >= toff_pwm:
                            self.tempo_pnp_decorrido_canal4 = 0
                            self.mudar_cor_label("lbPnp_canal_4", self.VERDE)
                            self.estado_cor_pnp_4 = self.VERDE

                    self.tempo_ligado_canal4_pnp += incremento_canal4
                    if self.tempo_ligado_canal4_pnp >= self.pnp_canal4_ton * 60:  # Convertendo minutos para segundos
                        self.tempo_ligado_canal4_pnp = 0
                        self.estado_ligado_canal4_pnp = False
                        
                        if self.pnp_canal4_contador >= self.pnp_canal4_qtd + 1:
                            self.pnp_canal4_contador = self.pnp_canal4_qtd
                            self.mudar_cor_label("lbPnp_canal_4", self.CINZA)
                            self.estado_cor_pnp_4 = self.CINZA

                    self.mudar_texto_label("lbPnp_qdt_4", f"{self.pnp_canal4_contador} de {self.pnp_canal4_qtd}")
                else:
                    self.tempo_desligado_canal4_pnp += incremento_canal4
                    if self.tempo_desligado_canal4_pnp >= self.pnp_canal4_toff * 60:  # Convertendo minutos para segundos
                        self.tempo_desligado_canal4_pnp = 0
                        self.estado_ligado_canal4_pnp = True
                        self.pnp_canal4_contador += 1  # Incrementa o contador ao finalizar o tempo ligado

                    self.mudar_cor_label("lbPnp_canal_4", self.CINZA)
                    self.estado_cor_pnp_4 = self.CINZA
                    self.io.pnp_output(3, 0)
            else:
                self.mudar_cor_label("lbPnp_canal_4", self.CINZA)
                self.estado_cor_pnp_4 = self.CINZA
                self.io.pnp_output(3, 0)

        else:
            self.io.pnp_output(0, 0)
            self.io.pnp_output(1, 0)
            self.io.pnp_output(2, 0)
            self.io.pnp_output(3, 0)

            self.ui.lbNomeProg.setText(f"{self.nome_programa}: Parado")

        if self.pnp_canal1_contador >= self.pnp_canal1_qtd and self.pnp_canal2_contador >= self.pnp_canal2_qtd and self.pnp_canal3_contador >= self.pnp_canal3_qtd and self.pnp_canal4_contador >= self.pnp_canal4_qtd + 1:
            self.iniciado_pnp = False

            self.mudar_texto_label("lbPnp_qdt_1", f"{self.pnp_canal1_contador} de {self.pnp_canal1_qtd}")
            self.mudar_texto_label("lbPnp_qdt_2", f"{self.pnp_canal2_contador} de {self.pnp_canal2_qtd}")
            self.mudar_texto_label("lbPnp_qdt_3", f"{self.pnp_canal3_contador} de {self.pnp_canal3_qtd}")
            self.mudar_texto_label("lbPnp_qdt_4", f"{self.pnp_canal4_contador - 1} de {self.pnp_canal4_qtd}")

            self.tempo_pnp_decorrido_canal1 = 0
            self.tempo_pnp_decorrido_canal2 = 0
            self.tempo_pnp_decorrido_canal3 = 0
            self.tempo_pnp_decorrido_canal4 = 0

            self.pnp_canal1_contador = 1
            self.pnp_canal2_contador = 1
            self.pnp_canal3_contador = 1
            self.pnp_canal4_contador = 1

            self.estado_cor_pnp_1 = self.CINZA
            self.estado_cor_pnp_2 = self.CINZA
            self.estado_cor_pnp_3 = self.CINZA
            self.estado_cor_pnp_4 = self.CINZA

            self.mudar_cor_label("lbPnp_canal_1", self.CINZA)
            self.estado_cor_pnp_1 = self.CINZA
            self.mudar_cor_label("lbPnp_canal_2", self.CINZA)
            self.estado_cor_pnp_2 = self.CINZA
            self.mudar_cor_label("lbPnp_canal_3", self.CINZA)
            self.estado_cor_pnp_3 = self.CINZA
            self.mudar_cor_label("lbPnp_canal_4", self.CINZA)
            self.estado_cor_pnp_4 = self.CINZA

            self.fim_pnp = True  # Indica que o programa PNP terminou

    def executa_canal_rele(self):
        if not self.programa_salvo:
            return
    
        if self.rele_habilita_desabilita == 1 and self.iniciado_rele and self.fim_rele==False:
            self.oscila_executando()
            incremento_canal1 = 0.1 if self.rele_base_tempo == 0 else 0.1 / 60  # Incrementa em 0.1 segundos ou 0.1 minutos
            incremento_canal2 = 0.1 if self.rele_base_tempo == 0 else 0.1 / 60
            incremento_canal3 = 0.1 if self.rele_base_tempo == 0 else 0.1 / 60
            incremento_canal4 = 0.1 if self.rele_base_tempo == 0 else 0.1 / 60
    
            # Canal 1
            if self.estado_cor_rele_1 == self.VERDE:
                self.tempo_rele_decorrido_canal1 += incremento_canal1
                self.io.relay_output(0, 1)
                if self.tempo_rele_decorrido_canal1 >= self.rele_canal1_ton:
                    self.tempo_rele_decorrido_canal1 = 0
                    self.mudar_cor_label("lbRele_canal_1", self.CINZA)
                    self.estado_cor_rele_1 = self.CINZA
            else:
                self.tempo_rele_decorrido_canal1 += incremento_canal1
                self.io.relay_output(0, 0)
                if self.tempo_rele_decorrido_canal1 >= self.rele_canal1_toff:
                    self.tempo_rele_decorrido_canal1 = 0
                    self.mudar_cor_label("lbRele_canal_1", self.VERDE)
                    self.estado_cor_rele_1 = self.VERDE
    
                    self.rele_canal1_contador += 1  # Incrementa o contador ao finalizar rele_canal1_toff
    
                    if self.rele_canal1_contador >= self.rele_canal1_qtd+1:
                        self.rele_canal1_contador = self.rele_canal1_qtd
                        self.mudar_cor_label("lbRele_canal_1", self.CINZA)
                        self.estado_cor_rele_1 = self.CINZA
        
                    self.mudar_texto_label("lbRele_qdt_1", f"{self.rele_canal1_contador} de {self.rele_canal1_qtd}")
    
            # Canal 2
            if self.estado_cor_rele_2 == self.VERDE:
                self.tempo_rele_decorrido_canal2 += incremento_canal2
                self.io.relay_output(1, 1)
                if self.tempo_rele_decorrido_canal2 >= self.rele_canal2_ton:
                    self.tempo_rele_decorrido_canal2 = 0
                    self.mudar_cor_label("lbRele_canal_2", self.CINZA)
                    self.estado_cor_rele_2 = self.CINZA
            else:
                self.tempo_rele_decorrido_canal2 += incremento_canal2
                self.io.relay_output(1, 0)
                if self.tempo_rele_decorrido_canal2 >= self.rele_canal2_toff:
                    self.tempo_rele_decorrido_canal2 = 0
                    self.mudar_cor_label("lbRele_canal_2", self.VERDE)
                    self.estado_cor_rele_2 = self.VERDE
    
                    self.rele_canal2_contador += 1  # Incrementa o contador ao finalizar rele_canal2_toff
    
                    if self.rele_canal2_contador >= self.rele_canal2_qtd+1:
                        self.rele_canal2_contador = self.rele_canal2_qtd
                        self.mudar_cor_label("lbRele_canal_2", self.CINZA)
                        self.estado_cor_rele_2 = self.CINZA
        
                    self.mudar_texto_label("lbRele_qdt_2", f"{self.rele_canal2_contador} de {self.rele_canal2_qtd}")
    
            # Canal 3
            if self.estado_cor_rele_3 == self.VERDE:
                self.tempo_rele_decorrido_canal3 += incremento_canal3
                self.io.relay_output(2, 1)
                if self.tempo_rele_decorrido_canal3 >= self.rele_canal3_ton:
                    self.tempo_rele_decorrido_canal3 = 0
                    self.mudar_cor_label("lbRele_canal_3", self.CINZA)
                    self.estado_cor_rele_3 = self.CINZA
            else:
                self.tempo_rele_decorrido_canal3 += incremento_canal3
                self.io.relay_output(2, 0)
                if self.tempo_rele_decorrido_canal3 >= self.rele_canal3_toff:
                    self.tempo_rele_decorrido_canal3 = 0
                    self.mudar_cor_label("lbRele_canal_3", self.VERDE)
                    self.estado_cor_rele_3 = self.VERDE
    
                    self.rele_canal3_contador += 1  # Incrementa o contador ao finalizar rele_canal3_toff
    
                    if self.rele_canal3_contador >= self.rele_canal3_qtd+1:
                        self.rele_canal3_contador = self.rele_canal3_qtd
                        self.mudar_cor_label("lbRele_canal_3", self.CINZA)
                        self.estado_cor_rele_3 = self.CINZA
        
                    self.mudar_texto_label("lbRele_qdt_3", f"{self.rele_canal3_contador} de {self.rele_canal3_qtd}")
    
            # Canal 4
            if self.estado_cor_rele_4 == self.VERDE:
                self.tempo_rele_decorrido_canal4 += incremento_canal4
                self.io.relay_output(3, 1)
                if self.tempo_rele_decorrido_canal4 >= self.rele_canal4_ton:
                    self.tempo_rele_decorrido_canal4 = 0
                    self.mudar_cor_label("lbRele_canal_4", self.CINZA)
                    self.estado_cor_rele_4 = self.CINZA
            else:
                self.tempo_rele_decorrido_canal4 += incremento_canal4
                self.io.relay_output(3, 0)
                if self.tempo_rele_decorrido_canal4 >= self.rele_canal4_toff:
                    self.tempo_rele_decorrido_canal4 = 0
                    self.mudar_cor_label("lbRele_canal_4", self.VERDE)
                    self.estado_cor_rele_4 = self.VERDE
    
                    self.rele_canal4_contador += 1  # Incrementa o contador ao finalizar rele_canal4_toff
    
                    if self.rele_canal4_contador >= self.rele_canal4_qtd+1:
                        self.rele_canal4_contador = self.rele_canal4_qtd
                        self.mudar_cor_label("lbRele_canal_4", self.CINZA)
                        self.estado_cor_rele_4 = self.CINZA
        
                    self.mudar_texto_label("lbRele_qdt_4", f"{self.rele_canal4_contador} de {self.rele_canal4_qtd}")
    
        else:
            self.io.relay_output(0, 0)
            self.io.relay_output(1, 0)
            self.io.relay_output(2, 0)
            self.io.relay_output(3, 0)
    
            self.ui.lbNomeProg.setText(f"{self.nome_programa}: Parado")
    
        if self.rele_canal1_contador >= self.rele_canal1_qtd and self.rele_canal2_contador >= self.rele_canal2_qtd and self.rele_canal3_contador >= self.rele_canal3_qtd and self.rele_canal4_contador >= self.rele_canal4_qtd:
            self.iniciado_rele = False
    
            self.mudar_texto_label("lbRele_qdt_1", f"{self.rele_canal1_contador} de {self.rele_canal1_qtd}")
            self.mudar_texto_label("lbRele_qdt_2", f"{self.rele_canal2_contador} de {self.rele_canal2_qtd}")
            self.mudar_texto_label("lbRele_qdt_3", f"{self.rele_canal3_contador} de {self.rele_canal3_qtd}")
            self.mudar_texto_label("lbRele_qdt_4", f"{self.rele_canal4_contador} de {self.rele_canal4_qtd}")   
    
            self.tempo_rele_decorrido_canal1 = 0
            self.tempo_rele_decorrido_canal2 = 0
            self.tempo_rele_decorrido_canal3 = 0
            self.tempo_rele_decorrido_canal4 = 0
    
            self.rele_canal1_contador = 1
            self.rele_canal2_contador = 1
            self.rele_canal3_contador = 1
            self.rele_canal4_contador = 1
    
            self.estado_cor_rele_1 = self.CINZA
            self.estado_cor_rele_2 = self.CINZA
            self.estado_cor_rele_3 = self.CINZA
            self.estado_cor_rele_4 = self.CINZA
    
            self.mudar_cor_label("lbRele_canal_1", self.CINZA)
            self.estado_cor_rele_1 = self.CINZA
            self.mudar_cor_label("lbRele_canal_2", self.CINZA)
            self.estado_cor_rele_2 = self.CINZA
            self.mudar_cor_label("lbRele_canal_3", self.CINZA)
            self.estado_cor_rele_3 = self.CINZA
            self.mudar_cor_label("lbRele_canal_4", self.CINZA)
            self.estado_cor_rele_4 = self.CINZA
    
            self.fim_rele = True  # Indica que o programa RELE terminou

    def oscila_executando(self):
        self.oscila_msg = not self.oscila_msg
        if self.cnt_osciala < 20:
            self.cnt_osciala += 1
            self.ui.lbNomeProg.setText(f"{self.nome_programa}: Executando")
        elif self.cnt_osciala < 20+10:
            self.cnt_osciala += 1
            self.ui.lbNomeProg.setText(f"{self.nome_programa}: ")
        else:
            self.cnt_osciala = 0

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
        self.iniciado_npn = not self.iniciado_npn
        self.iniciado_pnp = not self.iniciado_pnp
        self.iniciado_rele = not self.iniciado_rele
        if self.iniciado_npn and self.iniciado_pnp and self.iniciado_rele:

            self.mudar_texto_label("lbNpn_qdt_1", f"{self.npn_canal1_contador} de {self.npn_canal1_qtd}")
            self.mudar_texto_label("lbNpn_qdt_2", f"{self.npn_canal2_contador} de {self.npn_canal2_qtd}")
            self.mudar_texto_label("lbNpn_qdt_3", f"{self.npn_canal3_contador} de {self.npn_canal3_qtd}")
            self.mudar_texto_label("lbNpn_qdt_4", f"{self.npn_canal4_contador} de {self.npn_canal4_qtd}")
            self.mudar_texto_label("lbPnp_qdt_1", f"{self.pnp_canal1_contador} de {self.pnp_canal1_qtd}")
            self.mudar_texto_label("lbPnp_qdt_2", f"{self.pnp_canal2_contador} de {self.pnp_canal2_qtd}")
            self.mudar_texto_label("lbPnp_qdt_3", f"{self.pnp_canal3_contador} de {self.pnp_canal3_qtd}")
            self.mudar_texto_label("lbPnp_qdt_4", f"{self.pnp_canal4_contador} de {self.pnp_canal4_qtd}")
            self.mudar_texto_label("lbRele_qdt_1", f"{self.rele_canal1_contador} de {self.rele_canal1_qtd}")
            self.mudar_texto_label("lbRele_qdt_2", f"{self.rele_canal2_contador} de {self.rele_canal2_qtd}")
            self.mudar_texto_label("lbRele_qdt_3", f"{self.rele_canal3_contador} de {self.rele_canal3_qtd}")
            self.mudar_texto_label("lbRele_qdt_4", f"{self.rele_canal4_contador} de {self.rele_canal4_qtd}")

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
            self.estado_cor_npn_1 = self.VERDE
            self.mudar_cor_label("lbNpn_canal_2", self.VERDE)
            self.estado_cor_npn_2 = self.VERDE
            self.mudar_cor_label("lbNpn_canal_3", self.VERDE)
            self.estado_cor_npn_3 = self.VERDE
            self.mudar_cor_label("lbNpn_canal_4", self.VERDE)
            self.estado_cor_npn_4 = self.VERDE
            self.mudar_cor_label("lbPnp_canal_1", self.VERDE)
            self.estado_cor_pnp_1 = self.VERDE
            self.mudar_cor_label("lbPnp_canal_2", self.VERDE)
            self.estado_cor_pnp_2 = self.VERDE
            self.mudar_cor_label("lbPnp_canal_3", self.VERDE)
            self.estado_cor_pnp_3 = self.VERDE
            self.mudar_cor_label("lbPnp_canal_4", self.VERDE)
            self.estado_cor_pnp_4 = self.VERDE
            self.mudar_cor_label("lbRele_canal_1", self.VERDE)
            self.estado_cor_rele_1 = self.VERDE
            self.mudar_cor_label("lbRele_canal_2", self.VERDE)
            self.estado_cor_rele_2 = self.VERDE
            self.mudar_cor_label("lbRele_canal_3", self.VERDE)
            self.estado_cor_rele_3 = self.VERDE
            self.mudar_cor_label("lbRele_canal_4", self.VERDE)
            self.estado_cor_rele_4 = self.VERDE
        else:
            self.ui.btIniciarPausar.setText("Iniciar")
            self.ui.lbNomeProg.setText(f"{self.nome_programa}: Parado")
    
    def closeEvent(self, event):
        self.atualizador.stop()
        self.atualizador.wait()
        event.accept()

    def enterEvent(self, event):
        if self.dado.mouse_pointer:
            QtGui.QCursor.setPos(self.mapToGlobal(self.rect().center()))
            self.setCursor(QtCore.Qt.BlankCursor)
            super().enterEvent(event)