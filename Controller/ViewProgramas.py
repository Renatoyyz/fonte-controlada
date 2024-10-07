import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QMessageBox, QPushButton
from PyQt5 import QtGui, QtCore

class ViewProgramas(QDialog):
    def __init__(self, dado=None, io=None, db=None):
        super().__init__()
        self.dado = dado
        self.io = io
        self.database = db
        self.nome_programa = None

        self.setWindowTitle("Programas")
        self.setGeometry(0, 0, 480, 320)
        # self.resize(480, 320)
        
        self.layout = QVBoxLayout()
        self.table = QTableWidget()
        self.layout.addWidget(self.table)
        
        self.back_button = QPushButton("Voltar")
        self.back_button.clicked.connect(self.close)
        self.layout.addWidget(self.back_button)
        
        self.setLayout(self.layout)

        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

        # Maximizar a janela
        # self.showMaximized()
        if self.dado.full_scream == True:
            self.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)
        
        self.load_data()
        
        self.table.cellClicked.connect(self.cell_was_clicked)
    
    def load_data(self):
        programs = self.database.read_all()
        if not programs:
            QMessageBox.warning(self, "Aviso", "Nenhum programa encontrado.")
            return

        self.table.setRowCount(len(programs))
        self.table.setColumnCount(1)  # Apenas uma coluna para o nome do programa
        self.table.setHorizontalHeaderLabels(["Nome Programa"])

        for row_idx, program in enumerate(programs):
            self.table.setItem(row_idx, 0, QTableWidgetItem(program[1]))  # Assumindo que o nome do programa está na segunda coluna

        self.table.resizeColumnsToContents()  # Ajusta a largura da coluna para caber no conteúdoself.table.setItem(row_idx, 0, QTableWidgetItem(program[1]))  # Assumindo que o nome do programa está na segunda coluna
        
    def cell_was_clicked(self, row, column):
        self.nome_programa = self.table.item(row, 0).text()
        # QMessageBox.information(self, "Programa Selecionado", f"Nome do Programa: {program_name}")
        self.close()

    def closeEvent(self, event):
        event.accept()

    def enterEvent(self, event):
        if self.dado.mouse_pointer:
            QtGui.QCursor.setPos(self.mapToGlobal(self.rect().center()))
            self.setCursor(QtCore.Qt.BlankCursor)
        super().enterEvent(event)

if __name__ == "__main__":
    from Dados import Dado
    from Ios import InOut
    from DataBase import DataBase

    app = QApplication(sys.argv)
    dialog = ViewProgramas(dado=Dado(), io=InOut(), db=DataBase())
    dialog.exec_()