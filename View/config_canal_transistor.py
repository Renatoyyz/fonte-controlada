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
        self.lbTipoCanal.setGeometry(QtCore.QRect(130, 5, 190, 16))
        self.lbTipoCanal.setObjectName("lbTipoCanal")
        self.groupBox_4 = QtWidgets.QGroupBox(frmConfigCanalTransistor)
        self.groupBox_4.setGeometry(QtCore.QRect(350, 0, 120, 300))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 110, 16))
        self.label_7.setObjectName("label_7")
        self.txPwmCanal_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.txPwmCanal_4.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.txPwmCanal_4.setObjectName("txPwmCanal_4")
        self.txPeriodoCanal_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.txPeriodoCanal_4.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.txPeriodoCanal_4.setObjectName("txPeriodoCanal_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 110, 16))
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(10, 130, 110, 16))
        self.label_12.setObjectName("label_12")
        self.txTonCanal_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.txTonCanal_4.setGeometry(QtCore.QRect(10, 150, 70, 21))
        self.txTonCanal_4.setObjectName("txTonCanal_4")
        self.label_13 = QtWidgets.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(10, 180, 110, 16))
        self.label_13.setObjectName("label_13")
        self.txToffCanal_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.txToffCanal_4.setGeometry(QtCore.QRect(10, 200, 70, 21))
        self.txToffCanal_4.setText("")
        self.txToffCanal_4.setObjectName("txToffCanal_4")
        self.txQtdCiclosCanal_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.txQtdCiclosCanal_4.setGeometry(QtCore.QRect(10, 250, 70, 21))
        self.txQtdCiclosCanal_4.setText("")
        self.txQtdCiclosCanal_4.setObjectName("txQtdCiclosCanal_4")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(10, 230, 100, 16))
        self.label_14.setObjectName("label_14")
        self.ckbHabilitaModulo = QtWidgets.QCheckBox(frmConfigCanalTransistor)
        self.ckbHabilitaModulo.setGeometry(QtCore.QRect(100, 280, 121, 20))
        self.ckbHabilitaModulo.setObjectName("ckbHabilitaModulo")
        self.btSalvar = QtWidgets.QPushButton(frmConfigCanalTransistor)
        self.btSalvar.setGeometry(QtCore.QRect(10, 260, 80, 40))
        self.btSalvar.setObjectName("btSalvar")
        self.btVoltar = QtWidgets.QPushButton(frmConfigCanalTransistor)
        self.btVoltar.setGeometry(QtCore.QRect(260, 260, 80, 40))
        self.btVoltar.setObjectName("btVoltar")
        self.rbtBaseSegundos = QtWidgets.QRadioButton(frmConfigCanalTransistor)
        self.rbtBaseSegundos.setGeometry(QtCore.QRect(100, 240, 120, 20))
        self.rbtBaseSegundos.setChecked(True)
        self.rbtBaseSegundos.setObjectName("rbtBaseSegundos")
        self.rbtBaseMinutos = QtWidgets.QRadioButton(frmConfigCanalTransistor)
        self.rbtBaseMinutos.setGeometry(QtCore.QRect(100, 260, 120, 20))
        self.rbtBaseMinutos.setObjectName("rbtBaseMinutos")
        self.groupBox_3 = QtWidgets.QGroupBox(frmConfigCanalTransistor)
        self.groupBox_3.setGeometry(QtCore.QRect(240, 20, 90, 190))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label_5.setObjectName("label_5")
        self.txTonCanal_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txTonCanal_3.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.txTonCanal_3.setObjectName("txTonCanal_3")
        self.txToffCanal_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txToffCanal_3.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.txToffCanal_3.setObjectName("txToffCanal_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 80, 60, 16))
        self.label_6.setObjectName("label_6")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 130, 60, 16))
        self.label_11.setObjectName("label_11")
        self.txQtdCiclosCanal_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.txQtdCiclosCanal_3.setGeometry(QtCore.QRect(10, 150, 70, 21))
        self.txQtdCiclosCanal_3.setObjectName("txQtdCiclosCanal_3")
        self.groupBox_2 = QtWidgets.QGroupBox(frmConfigCanalTransistor)
        self.groupBox_2.setGeometry(QtCore.QRect(130, 20, 90, 190))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label_3.setObjectName("label_3")
        self.txTonCanal_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txTonCanal_2.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.txTonCanal_2.setObjectName("txTonCanal_2")
        self.txToffCanal_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txToffCanal_2.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.txToffCanal_2.setObjectName("txToffCanal_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 60, 16))
        self.label_4.setObjectName("label_4")
        self.txQtdCiclosCanal_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.txQtdCiclosCanal_2.setGeometry(QtCore.QRect(10, 150, 70, 21))
        self.txQtdCiclosCanal_2.setObjectName("txQtdCiclosCanal_2")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 130, 60, 16))
        self.label_10.setObjectName("label_10")
        self.groupBox = QtWidgets.QGroupBox(frmConfigCanalTransistor)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 90, 190))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label.setObjectName("label")
        self.txTonCanal_1 = QtWidgets.QLineEdit(self.groupBox)
        self.txTonCanal_1.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.txTonCanal_1.setObjectName("txTonCanal_1")
        self.txToffCanal_1 = QtWidgets.QLineEdit(self.groupBox)
        self.txToffCanal_1.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.txToffCanal_1.setObjectName("txToffCanal_1")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 60, 16))
        self.label_2.setObjectName("label_2")
        self.txQtdCiclosCanal_1 = QtWidgets.QLineEdit(self.groupBox)
        self.txQtdCiclosCanal_1.setGeometry(QtCore.QRect(10, 150, 70, 21))
        self.txQtdCiclosCanal_1.setObjectName("txQtdCiclosCanal_1")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 130, 60, 16))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(frmConfigCanalTransistor)
        QtCore.QMetaObject.connectSlotsByName(frmConfigCanalTransistor)

    def retranslateUi(self, frmConfigCanalTransistor):
        _translate = QtCore.QCoreApplication.translate
        frmConfigCanalTransistor.setWindowTitle(_translate("frmConfigCanalTransistor", "Form"))
        self.lbTipoCanal.setText(_translate("frmConfigCanalTransistor", "Transistor XXX"))
        self.groupBox_4.setTitle(_translate("frmConfigCanalTransistor", "CANAL 4"))
        self.label_7.setText(_translate("frmConfigCanalTransistor", "PWM(%)"))
        self.label_8.setText(_translate("frmConfigCanalTransistor", "Periodo(seg)"))
        self.label_12.setText(_translate("frmConfigCanalTransistor", "TON(min)"))
        self.label_13.setText(_translate("frmConfigCanalTransistor", "TOFF(min)"))
        self.label_14.setText(_translate("frmConfigCanalTransistor", "CICLOS"))
        self.ckbHabilitaModulo.setText(_translate("frmConfigCanalTransistor", "Habilita Módulo"))
        self.btSalvar.setText(_translate("frmConfigCanalTransistor", "Salvar"))
        self.btVoltar.setText(_translate("frmConfigCanalTransistor", "Voltar"))
        self.rbtBaseSegundos.setText(_translate("frmConfigCanalTransistor", "Base Segundos"))
        self.rbtBaseMinutos.setText(_translate("frmConfigCanalTransistor", "Base Minutos"))
        self.groupBox_3.setTitle(_translate("frmConfigCanalTransistor", "CANAL 3"))
        self.label_5.setText(_translate("frmConfigCanalTransistor", "TON"))
        self.label_6.setText(_translate("frmConfigCanalTransistor", "TOFF"))
        self.label_11.setText(_translate("frmConfigCanalTransistor", "CICLOS"))
        self.groupBox_2.setTitle(_translate("frmConfigCanalTransistor", "CANAL 2"))
        self.label_3.setText(_translate("frmConfigCanalTransistor", "TON"))
        self.label_4.setText(_translate("frmConfigCanalTransistor", "TOFF"))
        self.label_10.setText(_translate("frmConfigCanalTransistor", "CICLOS"))
        self.groupBox.setTitle(_translate("frmConfigCanalTransistor", "CANAL 1"))
        self.label.setText(_translate("frmConfigCanalTransistor", "TON"))
        self.label_2.setText(_translate("frmConfigCanalTransistor", "TOFF"))
        self.label_9.setText(_translate("frmConfigCanalTransistor", "CICLOS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmConfigCanalTransistor = QtWidgets.QWidget()
    ui = Ui_frmConfigCanalTransistor()
    ui.setupUi(frmConfigCanalTransistor)
    frmConfigCanalTransistor.show()
    sys.exit(app.exec_())
