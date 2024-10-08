import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QLineEdit, QGridLayout, QDialog
from PyQt5 import QtWidgets, QtCore, QtGui

class AlphanumericKeyboard(QDialog):
    def __init__(self, dado=None):
        super().__init__()
        self.dado = dado
        self.setWindowTitle("Teclado Alfanumérico")
        self.setGeometry(0, 0, 480, 320)
        self.setMinimumSize(100, 50)  # Definir as dimensões mínimas da janela
        self.setMaximumSize(480, 320)  # Definir as dimensões máximas da janela
        self.layout = QVBoxLayout()
        self.line_edit = QLineEdit()
        self.layout.addWidget(self.line_edit)
        self.grid_layout = QGridLayout()

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        
        if self.dado and self.dado.full_scream:
            self.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)

        self.buttons = [
            '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', '-', '<-', 'OK'
        ]
        positions = [(i, j) for i in range(6) for j in range(8)]
        for position, button in zip(positions, self.buttons):
            row, col = position
            button_obj = QPushButton(button)
            if button == '<-':
                button_obj.clicked.connect(self.on_backspace_click)
            elif button == 'OK':
                button_obj.clicked.connect(self.on_ok_click)
            else:
                button_obj.clicked.connect(lambda state, button=button: self.on_button_click(button))
            self.grid_layout.addWidget(button_obj, row, col)
        self.layout.addLayout(self.grid_layout)
        self.setLayout(self.layout)

    def on_button_click(self, button):
        if button == ' ':
            self.line_edit.setText(self.line_edit.text() + ' ')
        else:
            self.line_edit.setText(self.line_edit.text() + button)

    def on_backspace_click(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text[:-1])

    def on_ok_click(self):
        self.close()

    def closeEvent(self, event):
        event.accept()

    def enterEvent(self, event):
        if self.dado.mouse_pointer:
            QtGui.QCursor.setPos(self.mapToGlobal(self.rect().center()))
            self.setCursor(QtCore.Qt.BlankCursor)
            super().enterEvent(event)


class NumericKeyboard(QDialog):
    def __init__(self, dado=None, type="password"):
        super().__init__()
        self.dado = dado
        self.type = type
        self.setWindowTitle("Teclado Numérico")
        self.setGeometry(0, 0, 480, 320)
        self.setMinimumSize(100, 50)  # Definir as dimensões mínimas da janela
        self.setMaximumSize(480, 320)  # Definir as dimensões máximas da janela
        self.layout = QVBoxLayout()
        self.line_edit = QLineEdit()

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        
        if self.dado and self.dado.full_scream:
            self.setWindowState(QtCore.Qt.WindowState.WindowFullScreen)

        if self.type == "password":
            self.line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.layout.addWidget(self.line_edit)
        self.grid_layout = QGridLayout()
        self.buttons = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '.', '0', '<-'
        ]

        positions = [(i, j) for i in range(5) for j in range(3)]
        for position, button in zip(positions, self.buttons):
            row, col = position
            button_obj = QPushButton(button)
            if button == '<-':
                button_obj.clicked.connect(self.on_backspace_click)
            elif button == '.':
                button_obj.clicked.connect(self.on_decimal_click)
            else:
                button_obj.clicked.connect(lambda state, button=button: self.on_button_click(button))
            self.grid_layout.addWidget(button_obj, row, col)
        
        ok_button = QPushButton('OK')
        ok_button.clicked.connect(self.on_ok_click)
        self.grid_layout.addWidget(ok_button, 5, 1, 1, 1)

        self.layout.addLayout(self.grid_layout)
        self.setLayout(self.layout)

    def on_button_click(self, button):
        self.line_edit.setText(self.line_edit.text() + button)

    def on_decimal_click(self):
        current_text = self.line_edit.text()
        if '.' not in current_text:
            self.line_edit.setText(current_text + '.')

    def on_backspace_click(self):
        current_text = self.line_edit.text()
        self.line_edit.setText(current_text[:-1])

    def on_ok_click(self):
        if self.line_edit.text() != "":
            pass
        self.close()
    def closeEvent(self, event):
        event.accept()

    def enterEvent(self, event):
        if self.dado.mouse_pointer:
            QtGui.QCursor.setPos(self.mapToGlobal(self.rect().center()))
            self.setCursor(QtCore.Qt.BlankCursor)
            super().enterEvent(event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    numeric_keyboard = NumericKeyboard()
    alphanumeric_keyboard = AlphanumericKeyboard()
    numeric_keyboard.exec_()
    alphanumeric_keyboard.exec_()
    sys.exit(app.exec_())