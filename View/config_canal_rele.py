# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/config_canal_rele.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmConfigCanalRele(object):
    def setupUi(self, frmConfigCanalRele):
        frmConfigCanalRele.setObjectName("frmConfigCanalRele")
        frmConfigCanalRele.resize(480, 320)
        self.lbTipoCanal = QtWidgets.QLabel(frmConfigCanalRele)
        self.lbTipoCanal.setGeometry(QtCore.QRect(200, 3, 60, 19))
        self.lbTipoCanal.setObjectName("lbTipoCanal")
        self.groupBox = QtWidgets.QGroupBox(frmConfigCanalRele)
        self.groupBox.setGeometry(QtCore.QRect(30, 33, 90, 190))
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
        self.groupBox_3 = QtWidgets.QGroupBox(frmConfigCanalRele)
        self.groupBox_3.setGeometry(QtCore.QRect(250, 33, 90, 190))
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
        self.groupBox_4 = QtWidgets.QGroupBox(frmConfigCanalRele)
        self.groupBox_4.setGeometry(QtCore.QRect(360, 33, 90, 190))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 60, 16))
        self.label_7.setObjectName("label_7")
        self.txTonCanal_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.txTonCanal_4.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.txTonCanal_4.setObjectName("txTonCanal_4")
        self.txToffCanal_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.txToffCanal_4.setGeometry(QtCore.QRect(10, 100, 71, 21))
        self.txToffCanal_4.setObjectName("txToffCanal_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 50, 16))
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(10, 130, 60, 16))
        self.label_12.setObjectName("label_12")
        self.txQtdCiclosCanal_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.txQtdCiclosCanal_4.setGeometry(QtCore.QRect(10, 150, 70, 21))
        self.txQtdCiclosCanal_4.setObjectName("txQtdCiclosCanal_4")
        self.btVoltar = QtWidgets.QPushButton(frmConfigCanalRele)
        self.btVoltar.setGeometry(QtCore.QRect(390, 260, 80, 40))
        self.btVoltar.setObjectName("btVoltar")
        self.ckbHabilitaModulo = QtWidgets.QCheckBox(frmConfigCanalRele)
        self.ckbHabilitaModulo.setGeometry(QtCore.QRect(150, 270, 160, 20))
        self.ckbHabilitaModulo.setObjectName("ckbHabilitaModulo")
        self.rbtBaseMinutos = QtWidgets.QRadioButton(frmConfigCanalRele)
        self.rbtBaseMinutos.setGeometry(QtCore.QRect(260, 240, 120, 20))
        self.rbtBaseMinutos.setObjectName("rbtBaseMinutos")
        self.groupBox_2 = QtWidgets.QGroupBox(frmConfigCanalRele)
        self.groupBox_2.setGeometry(QtCore.QRect(140, 33, 90, 190))
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
        self.rbtBaseSegundos = QtWidgets.QRadioButton(frmConfigCanalRele)
        self.rbtBaseSegundos.setGeometry(QtCore.QRect(130, 240, 120, 20))
        self.rbtBaseSegundos.setChecked(True)
        self.rbtBaseSegundos.setObjectName("rbtBaseSegundos")
        self.btSalvar = QtWidgets.QPushButton(frmConfigCanalRele)
        self.btSalvar.setGeometry(QtCore.QRect(30, 260, 80, 40))
        self.btSalvar.setObjectName("btSalvar")

        self.retranslateUi(frmConfigCanalRele)
        QtCore.QMetaObject.connectSlotsByName(frmConfigCanalRele)

    def retranslateUi(self, frmConfigCanalRele):
        _translate = QtCore.QCoreApplication.translate
        frmConfigCanalRele.setWindowTitle(_translate("frmConfigCanalRele", "Form"))
        self.lbTipoCanal.setText(_translate("frmConfigCanalRele", "<html><head/><body><p align=\"center\">RELÉ</p></body></html>"))
        self.groupBox.setTitle(_translate("frmConfigCanalRele", "CANAL 1"))
        self.label.setText(_translate("frmConfigCanalRele", "TON"))
        self.label_2.setText(_translate("frmConfigCanalRele", "TOFF"))
        self.label_9.setText(_translate("frmConfigCanalRele", "CICLOS"))
        self.groupBox_3.setTitle(_translate("frmConfigCanalRele", "CANAL 3"))
        self.label_5.setText(_translate("frmConfigCanalRele", "TON"))
        self.label_6.setText(_translate("frmConfigCanalRele", "TOFF"))
        self.label_11.setText(_translate("frmConfigCanalRele", "CICLOS"))
        self.groupBox_4.setTitle(_translate("frmConfigCanalRele", "CANAL 4"))
        self.label_7.setText(_translate("frmConfigCanalRele", "TON"))
        self.label_8.setText(_translate("frmConfigCanalRele", "TOFF"))
        self.label_12.setText(_translate("frmConfigCanalRele", "CICLOS"))
        self.btVoltar.setText(_translate("frmConfigCanalRele", "Voltar"))
        self.ckbHabilitaModulo.setText(_translate("frmConfigCanalRele", "Habilita Módulo"))
        self.rbtBaseMinutos.setText(_translate("frmConfigCanalRele", "Base min."))
        self.groupBox_2.setTitle(_translate("frmConfigCanalRele", "CANAL 2"))
        self.label_3.setText(_translate("frmConfigCanalRele", "TON"))
        self.label_4.setText(_translate("frmConfigCanalRele", "TOFF"))
        self.label_10.setText(_translate("frmConfigCanalRele", "CICLOS"))
        self.rbtBaseSegundos.setText(_translate("frmConfigCanalRele", "Base seg."))
        self.btSalvar.setText(_translate("frmConfigCanalRele", "Salvar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmConfigCanalRele = QtWidgets.QWidget()
    ui = Ui_frmConfigCanalRele()
    ui.setupUi(frmConfigCanalRele)
    frmConfigCanalRele.show()
    sys.exit(app.exec_())
