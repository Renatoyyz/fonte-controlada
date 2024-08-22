import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("PyQt5 Form Example")

        layout = QVBoxLayout()

        button = QPushButton("Clique aqui")
        layout.addWidget(button)

        self.setLayout(layout)

        button.clicked.connect(self.close)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    app.exec()