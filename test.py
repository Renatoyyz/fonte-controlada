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

        # nome_programa, pnp_canal1_ton, pnp_canal1_toff, pnp_canal2_ton, pnp_canal2_toff, pnp_canal3_ton, pnp_canal3_toff, pnp_canal4_pwm, pnp_canal4_periodo_pwm, pnp_base_tempo, pnp_habilita_desabilita, npn_canal1_ton, npn_canal1_toff, npn_canal2_ton, npn_canal2_toff, npn_canal3_ton, npn_canal3_toff, npn_canal4_pwm, npn_canal4_periodo_pwm, npn_base_tempo, npn_habilita_desabilita, rele_canal1_ton, rele_canal1_toff, rele_canal2_ton, rele_canal2_toff, rele_canal3_ton, rele_canal3_toff, rele_canal4_ton, rele_canal4_toff, rele_base_tempo, rele_habilita_desabilita
                         

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    app.exec()