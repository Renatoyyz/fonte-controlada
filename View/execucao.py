# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/execucao.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmExecucao(object):
    def setupUi(self, frmExecucao):
        frmExecucao.setObjectName("frmExecucao")
        frmExecucao.resize(480, 320)
        self.btVoltar = QtWidgets.QPushButton(frmExecucao)
        self.btVoltar.setGeometry(QtCore.QRect(20, 270, 113, 32))
        self.btVoltar.setObjectName("btVoltar")
        self.btIniciarPausar = QtWidgets.QPushButton(frmExecucao)
        self.btIniciarPausar.setGeometry(QtCore.QRect(350, 270, 113, 32))
        self.btIniciarPausar.setObjectName("btIniciarPausar")
        self.lbNpn_canal_1 = QtWidgets.QLabel(frmExecucao)
        self.lbNpn_canal_1.setGeometry(QtCore.QRect(110, 47, 20, 20))
        self.lbNpn_canal_1.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbNpn_canal_1.setText("")
        self.lbNpn_canal_1.setObjectName("lbNpn_canal_1")
        self.lbNpn_canal_2 = QtWidgets.QLabel(frmExecucao)
        self.lbNpn_canal_2.setGeometry(QtCore.QRect(210, 47, 20, 20))
        self.lbNpn_canal_2.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbNpn_canal_2.setText("")
        self.lbNpn_canal_2.setObjectName("lbNpn_canal_2")
        self.lbNpn_canal_3 = QtWidgets.QLabel(frmExecucao)
        self.lbNpn_canal_3.setGeometry(QtCore.QRect(310, 47, 20, 20))
        self.lbNpn_canal_3.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbNpn_canal_3.setText("")
        self.lbNpn_canal_3.setObjectName("lbNpn_canal_3")
        self.lbNpn_canal_4 = QtWidgets.QLabel(frmExecucao)
        self.lbNpn_canal_4.setGeometry(QtCore.QRect(410, 47, 20, 20))
        self.lbNpn_canal_4.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbNpn_canal_4.setText("")
        self.lbNpn_canal_4.setObjectName("lbNpn_canal_4")
        self.lbPnp_canal_1 = QtWidgets.QLabel(frmExecucao)
        self.lbPnp_canal_1.setGeometry(QtCore.QRect(110, 127, 20, 20))
        self.lbPnp_canal_1.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbPnp_canal_1.setText("")
        self.lbPnp_canal_1.setObjectName("lbPnp_canal_1")
        self.lbPnp_canal_2 = QtWidgets.QLabel(frmExecucao)
        self.lbPnp_canal_2.setGeometry(QtCore.QRect(210, 127, 20, 20))
        self.lbPnp_canal_2.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbPnp_canal_2.setText("")
        self.lbPnp_canal_2.setObjectName("lbPnp_canal_2")
        self.lbPnp_canal_3 = QtWidgets.QLabel(frmExecucao)
        self.lbPnp_canal_3.setGeometry(QtCore.QRect(310, 127, 20, 20))
        self.lbPnp_canal_3.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbPnp_canal_3.setText("")
        self.lbPnp_canal_3.setObjectName("lbPnp_canal_3")
        self.lbPnp_canal_4 = QtWidgets.QLabel(frmExecucao)
        self.lbPnp_canal_4.setGeometry(QtCore.QRect(410, 127, 20, 20))
        self.lbPnp_canal_4.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbPnp_canal_4.setText("")
        self.lbPnp_canal_4.setObjectName("lbPnp_canal_4")
        self.lbRele_canal_1 = QtWidgets.QLabel(frmExecucao)
        self.lbRele_canal_1.setGeometry(QtCore.QRect(110, 207, 20, 20))
        self.lbRele_canal_1.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbRele_canal_1.setText("")
        self.lbRele_canal_1.setObjectName("lbRele_canal_1")
        self.lbRele_canal_2 = QtWidgets.QLabel(frmExecucao)
        self.lbRele_canal_2.setGeometry(QtCore.QRect(210, 207, 20, 20))
        self.lbRele_canal_2.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbRele_canal_2.setText("")
        self.lbRele_canal_2.setObjectName("lbRele_canal_2")
        self.lbRele_canal_3 = QtWidgets.QLabel(frmExecucao)
        self.lbRele_canal_3.setGeometry(QtCore.QRect(310, 207, 20, 20))
        self.lbRele_canal_3.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbRele_canal_3.setText("")
        self.lbRele_canal_3.setObjectName("lbRele_canal_3")
        self.lbRele_canal_4 = QtWidgets.QLabel(frmExecucao)
        self.lbRele_canal_4.setGeometry(QtCore.QRect(410, 207, 20, 20))
        self.lbRele_canal_4.setStyleSheet("background-color: rgb(33, 255, 6);")
        self.lbRele_canal_4.setText("")
        self.lbRele_canal_4.setObjectName("lbRele_canal_4")
        self.label = QtWidgets.QLabel(frmExecucao)
        self.label.setGeometry(QtCore.QRect(20, 60, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(frmExecucao)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(frmExecucao)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 60, 16))
        self.label_3.setObjectName("label_3")
        self.lbNomeProg = QtWidgets.QLabel(frmExecucao)
        self.lbNomeProg.setGeometry(QtCore.QRect(60, 8, 340, 20))
        self.lbNomeProg.setObjectName("lbNomeProg")
        self.lbNpn_qdt_1 = QtWidgets.QLabel(frmExecucao)
        self.lbNpn_qdt_1.setGeometry(QtCore.QRect(80, 70, 80, 16))
        self.lbNpn_qdt_1.setObjectName("lbNpn_qdt_1")
        self.lbNpn_qdt_2 = QtWidgets.QLabel(frmExecucao)
        self.lbNpn_qdt_2.setGeometry(QtCore.QRect(180, 70, 80, 16))
        self.lbNpn_qdt_2.setObjectName("lbNpn_qdt_2")
        self.lbNpn_qdt_3 = QtWidgets.QLabel(frmExecucao)
        self.lbNpn_qdt_3.setGeometry(QtCore.QRect(280, 70, 80, 16))
        self.lbNpn_qdt_3.setObjectName("lbNpn_qdt_3")
        self.lbNpn_qdt_4 = QtWidgets.QLabel(frmExecucao)
        self.lbNpn_qdt_4.setGeometry(QtCore.QRect(380, 70, 80, 16))
        self.lbNpn_qdt_4.setObjectName("lbNpn_qdt_4")
        self.lbPnp_qdt_1 = QtWidgets.QLabel(frmExecucao)
        self.lbPnp_qdt_1.setGeometry(QtCore.QRect(80, 150, 80, 16))
        self.lbPnp_qdt_1.setObjectName("lbPnp_qdt_1")
        self.lbPnp_qdt_2 = QtWidgets.QLabel(frmExecucao)
        self.lbPnp_qdt_2.setGeometry(QtCore.QRect(180, 150, 80, 16))
        self.lbPnp_qdt_2.setObjectName("lbPnp_qdt_2")
        self.lbPnp_qdt_4 = QtWidgets.QLabel(frmExecucao)
        self.lbPnp_qdt_4.setGeometry(QtCore.QRect(380, 150, 80, 16))
        self.lbPnp_qdt_4.setObjectName("lbPnp_qdt_4")
        self.lbPnp_qdt_3 = QtWidgets.QLabel(frmExecucao)
        self.lbPnp_qdt_3.setGeometry(QtCore.QRect(280, 150, 80, 16))
        self.lbPnp_qdt_3.setObjectName("lbPnp_qdt_3")
        self.lbRele_qdt_1 = QtWidgets.QLabel(frmExecucao)
        self.lbRele_qdt_1.setGeometry(QtCore.QRect(80, 230, 80, 16))
        self.lbRele_qdt_1.setObjectName("lbRele_qdt_1")
        self.lbRele_qdt_2 = QtWidgets.QLabel(frmExecucao)
        self.lbRele_qdt_2.setGeometry(QtCore.QRect(180, 230, 80, 16))
        self.lbRele_qdt_2.setObjectName("lbRele_qdt_2")
        self.lbRele_qdt_3 = QtWidgets.QLabel(frmExecucao)
        self.lbRele_qdt_3.setGeometry(QtCore.QRect(280, 230, 80, 16))
        self.lbRele_qdt_3.setObjectName("lbRele_qdt_3")
        self.lbRele_qdt_4 = QtWidgets.QLabel(frmExecucao)
        self.lbRele_qdt_4.setGeometry(QtCore.QRect(380, 230, 80, 16))
        self.lbRele_qdt_4.setObjectName("lbRele_qdt_4")
        self.line = QtWidgets.QFrame(frmExecucao)
        self.line.setGeometry(QtCore.QRect(10, 100, 460, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(frmExecucao)
        self.line_2.setGeometry(QtCore.QRect(10, 180, 460, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(frmExecucao)
        self.line_3.setGeometry(QtCore.QRect(10, 260, 460, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(frmExecucao)
        QtCore.QMetaObject.connectSlotsByName(frmExecucao)

    def retranslateUi(self, frmExecucao):
        _translate = QtCore.QCoreApplication.translate
        frmExecucao.setWindowTitle(_translate("frmExecucao", "Form"))
        self.btVoltar.setText(_translate("frmExecucao", "Voltar"))
        self.btIniciarPausar.setText(_translate("frmExecucao", "Iniciar"))
        self.label.setText(_translate("frmExecucao", "NPN"))
        self.label_2.setText(_translate("frmExecucao", "PNP"))
        self.label_3.setText(_translate("frmExecucao", "RELE"))
        self.lbNomeProg.setText(_translate("frmExecucao", "NOME_PROG"))
        self.lbNpn_qdt_1.setText(_translate("frmExecucao", "xx de xx"))
        self.lbNpn_qdt_2.setText(_translate("frmExecucao", "xx de xx"))
        self.lbNpn_qdt_3.setText(_translate("frmExecucao", "xx de xx"))
        self.lbNpn_qdt_4.setText(_translate("frmExecucao", "xx de xx"))
        self.lbPnp_qdt_1.setText(_translate("frmExecucao", "xx de xx"))
        self.lbPnp_qdt_2.setText(_translate("frmExecucao", "xx de xx"))
        self.lbPnp_qdt_4.setText(_translate("frmExecucao", "xx de xx"))
        self.lbPnp_qdt_3.setText(_translate("frmExecucao", "xx de xx"))
        self.lbRele_qdt_1.setText(_translate("frmExecucao", "xx de xx"))
        self.lbRele_qdt_2.setText(_translate("frmExecucao", "xx de xx"))
        self.lbRele_qdt_3.setText(_translate("frmExecucao", "xx de xx"))
        self.lbRele_qdt_4.setText(_translate("frmExecucao", "xx de xx"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmExecucao = QtWidgets.QWidget()
    ui = Ui_frmExecucao()
    ui.setupUi(frmExecucao)
    frmExecucao.show()
    sys.exit(app.exec_())
