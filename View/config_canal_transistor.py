# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/config_canal_transistor.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmConfigCanalTransistor(object):
    def setupUi(self, frmConfigCanalTransistor):
        frmConfigCanalTransistor.setObjectName("frmConfigCanalTransistor")
        frmConfigCanalTransistor.resize(480, 320)
        self.lbTipoCanal = QtWidgets.QLabel(frmConfigCanalTransistor)
        self.lbTipoCanal.setGeometry(QtCore.QRect(160, 10, 140, 16))
        self.lbTipoCanal.setObjectName("lbTipoCanal")
        self.groupBox = QtWidgets.QGroupBox(frmConfigCanalTransistor)
        self.groupBox.setGeometry(QtCore.QRect(20, 40, 90, 151))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label.setObjectName("label")
        self.txTonCanal_1 = QtWidgets.QLineEdit(self.groupBox)
        self.txTonCanal_1.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.txTonCanal_1.setObjectName("txTonCanal_1")
        self.txToffCanal_1 = QtWidgets.QLineEdit(self.groupBox)
        self.txToffCanal_1.setGeometry(QtCore.QRect(10, 110, 71, 21))
        self.txToffCanal_1.setObjectName("txToffCanal_1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 60, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(frmConfigCanalTransistor)
        self.groupBox_2.setGeometry(QtCore.QRect(130, 40, 90, 151))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label_3.setObjectName("label_3")
        self.txTonCanal_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txTonCanal_2.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.txTonCanal_2.setObjectName("txTonCanal_2")
        self.txToffCanal_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txToffCanal_2.setGeometry(QtCore.QRect(10, 110, 71, 21))
        self.txToffCanal_2.setObjectName("txToffCanal_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 60, 16))
        self.label_4.setObjectName("label_4")
        self.groupBox_3 = QtWidgets.QGroupBox(frmConfigCanalTransistor)
        self.groupBox_3.setGeometry(QtCore.QRect(240, 40, 90, 151))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label_5.setObjectName("label_5")
        self.txTonCanal_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txTonCanal_3.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.txTonCanal_3.setObjectName("txTonCanal_3")
        self.txToffCanal_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txToffCanal_3.setGeometry(QtCore.QRect(10, 110, 71, 21))
        self.txToffCanal_3.setObjectName("txToffCanal_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 60, 16))
        self.label_6.setObjectName("label_6")
        self.groupBox_4 = QtWidgets.QGroupBox(frmConfigCanalTransistor)
        self.groupBox_4.setGeometry(QtCore.QRect(350, 40, 90, 151))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label_7.setObjectName("label_7")
        self.txPwmCanal_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.txPwmCanal_4.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.txPwmCanal_4.setObjectName("txPwmCanal_4")
        self.txPeriodoCanal_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.txPeriodoCanal_4.setGeometry(QtCore.QRect(10, 110, 71, 21))
        self.txPeriodoCanal_4.setObjectName("txPeriodoCanal_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 90, 80, 16))
        self.label_8.setObjectName("label_8")
        self.ckbHabilitaModulo = QtWidgets.QCheckBox(frmConfigCanalTransistor)
        self.ckbHabilitaModulo.setGeometry(QtCore.QRect(300, 210, 141, 20))
        self.ckbHabilitaModulo.setObjectName("ckbHabilitaModulo")
        self.btSalvar = QtWidgets.QPushButton(frmConfigCanalTransistor)
        self.btSalvar.setGeometry(QtCore.QRect(20, 260, 80, 40))
        self.btSalvar.setObjectName("btSalvar")
        self.btVoltar = QtWidgets.QPushButton(frmConfigCanalTransistor)
        self.btVoltar.setGeometry(QtCore.QRect(380, 260, 80, 40))
        self.btVoltar.setObjectName("btVoltar")
        self.rbtBaseSegundos = QtWidgets.QRadioButton(frmConfigCanalTransistor)
        self.rbtBaseSegundos.setGeometry(QtCore.QRect(20, 210, 120, 20))
        self.rbtBaseSegundos.setChecked(True)
        self.rbtBaseSegundos.setObjectName("rbtBaseSegundos")
        self.rbtBaseMinutos = QtWidgets.QRadioButton(frmConfigCanalTransistor)
        self.rbtBaseMinutos.setGeometry(QtCore.QRect(150, 210, 120, 20))
        self.rbtBaseMinutos.setObjectName("rbtBaseMinutos")
        self.label_9 = QtWidgets.QLabel(frmConfigCanalTransistor)
        self.label_9.setGeometry(QtCore.QRect(150, 250, 120, 16))
        self.label_9.setObjectName("label_9")
        self.txQtdCiclos = QtWidgets.QLineEdit(frmConfigCanalTransistor)
        self.txQtdCiclos.setGeometry(QtCore.QRect(170, 270, 80, 21))
        self.txQtdCiclos.setObjectName("txQtdCiclos")

        self.retranslateUi(frmConfigCanalTransistor)
        QtCore.QMetaObject.connectSlotsByName(frmConfigCanalTransistor)

    def retranslateUi(self, frmConfigCanalTransistor):
        _translate = QtCore.QCoreApplication.translate
        frmConfigCanalTransistor.setWindowTitle(_translate("frmConfigCanalTransistor", "Form"))
        self.lbTipoCanal.setText(_translate("frmConfigCanalTransistor", "Canal Transistor XXX"))
        self.groupBox.setTitle(_translate("frmConfigCanalTransistor", "CANAL 1"))
        self.label.setText(_translate("frmConfigCanalTransistor", "TON"))
        self.label_2.setText(_translate("frmConfigCanalTransistor", "TOFF"))
        self.groupBox_2.setTitle(_translate("frmConfigCanalTransistor", "CANAL 2"))
        self.label_3.setText(_translate("frmConfigCanalTransistor", "TON"))
        self.label_4.setText(_translate("frmConfigCanalTransistor", "TOFF"))
        self.groupBox_3.setTitle(_translate("frmConfigCanalTransistor", "CANAL 3"))
        self.label_5.setText(_translate("frmConfigCanalTransistor", "TON"))
        self.label_6.setText(_translate("frmConfigCanalTransistor", "TOFF"))
        self.groupBox_4.setTitle(_translate("frmConfigCanalTransistor", "CANAL 4"))
        self.label_7.setText(_translate("frmConfigCanalTransistor", "PWM(%)"))
        self.label_8.setText(_translate("frmConfigCanalTransistor", "Periodo(seg)"))
        self.ckbHabilitaModulo.setText(_translate("frmConfigCanalTransistor", "Habilita Módulo"))
        self.btSalvar.setText(_translate("frmConfigCanalTransistor", "Salvar"))
        self.btVoltar.setText(_translate("frmConfigCanalTransistor", "Voltar"))
        self.rbtBaseSegundos.setText(_translate("frmConfigCanalTransistor", "Base Segundos"))
        self.rbtBaseMinutos.setText(_translate("frmConfigCanalTransistor", "Base Minutos"))
        self.label_9.setText(_translate("frmConfigCanalTransistor", "Quantidade Cilclos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmConfigCanalTransistor = QtWidgets.QWidget()
    ui = Ui_frmConfigCanalTransistor()
    ui.setupUi(frmConfigCanalTransistor)
    frmConfigCanalTransistor.show()
    sys.exit(app.exec_())