from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import Qt

from View.config import Ui_frmConfig
from Controller.Teclados import NumericKeyboard, AlphanumericKeyboard
from Model.CanalTransistor import CanalTransistor
from Model.CanalRele import CanalRele
from Controller.ViewProgramas import ViewProgramas


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
        self.ui.btSalvar.clicked.connect(self.salvar)
        self.ui.btAbrir.clicked.connect(self.abrir)
        self.ui.btAtualizar.clicked.connect(self.atualizar)  # Conectar o botão atualizar
        self.ui.btExcluir.clicked.connect(self.deletar)  # Conectar o botão deletar


        self.config()

    def config(self):
        self.ui.txNomeProg.setText(self.dado.nome_programa)

    def eventoteclado(self, event):
        num_teclado = AlphanumericKeyboard(dado=self.dado)
        num_teclado.exec_()
        self.ui.txNomeProg.setText(num_teclado.line_edit.text())   

    def tela_canal_transistor_npn(self):
        self.dado.nome_programa = self.ui.txNomeProg.text()
        tela_npn = CanalTransistor(dado=self.dado, io=self.io, db=self.database, npn_pnp=self.dado.CANAL_NPN)
        tela_npn.exec_()

    def tela_canal_transistor_pnp(self):
        self.dado.nome_programa = self.ui.txNomeProg.text()
        tela_pnp = CanalTransistor(dado=self.dado, io=self.io, db=self.database, npn_pnp=self.dado.CANAL_PNP)
        tela_pnp.exec_() 

    def tela_canal_rele(self):
        tela_rele =  CanalRele(dado=self.dado, io=self.io, db=self.database)
        tela_rele.exec_() 

    def abrir(self):
        # Abrir a janela ViewProgramas
        view_programas = ViewProgramas(dado=self.dado, io=self.io, db=self.database)
        view_programas.exec_()

        # Obter o nome do programa selecionado
        nome_programa = view_programas.nome_programa
        if nome_programa:
            # Preencher o campo txNomeProg
            self.ui.txNomeProg.setText(nome_programa)

            # Carregar o programa salvo
            self.dado.salva_programa_tupla(self.dado.atualiza_programa_tupla(self.database, nome_programa))


    def salvar(self):
        self.dado.nome_programa = self.ui.txNomeProg.text().strip()
        
        # Verificar se o nome do programa está vazio
        if not self.dado.nome_programa:
            QMessageBox.warning(self, "Aviso", "O nome do programa não pode estar vazio!")
            return
        
        # Verificar se já existe um programa com o mesmo nome
        if self.database.read(self.dado.nome_programa):
            QMessageBox.warning(self, "Aviso", "Programa já existente!")
        else:
            # Dados a serem salvos
            data = self.dado.programa_salvo
            # Salvar no banco de dados
            self.database.create(data)
            QMessageBox.information(self, "Sucesso", "Programa salvo com sucesso!")
            # Limpar o campo txNomeProg
            self.ui.txNomeProg.clear()
            
            # Resetar a tupla em Dados.py
            self.dado.salva_programa_tupla(self.dado.reset_programa_tupla())

    def atualizar(self):
        nome_programa = self.ui.txNomeProg.text()
        
        # Verificar se o programa existe
        if self.database.read(nome_programa):
            # Dados a serem atualizados
            data = self.dado.programa_salvo[1:]  # Remover o índice 0 que contém o nome do programa
            # Atualizar no banco de dados
            self.database.update(nome_programa, data)
            QMessageBox.information(self, "Sucesso", "Programa atualizado com sucesso!")
        else:
            QMessageBox.warning(self, "Aviso", "Programa não encontrado!")

    def deletar(self):
        nome_programa = self.ui.txNomeProg.text()
        
        # Verificar se o programa existe
        if self.database.read(nome_programa):
            # Mostrar mensagem de confirmação
            reply = QMessageBox.question(self, 'Confirmação', 
                                         f"Você realmente deseja deletar o programa '{nome_programa}'?", 
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Deletar do banco de dados
                self.database.delete(nome_programa)
                QMessageBox.information(self, "Sucesso", "Programa deletado com sucesso!")
                # Limpar o campo txNomeProg
                self.ui.txNomeProg.clear()
        else:
            QMessageBox.warning(self, "Aviso", "Programa não encontrado!")

        

    def voltar(self):
        self.close()

    def closeEvent(self, event):
        event.accept()