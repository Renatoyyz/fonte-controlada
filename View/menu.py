# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'View/menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmMainMenu(object):
    def setupUi(self, frmMainMenu):
        frmMainMenu.setObjectName("frmMainMenu")
        frmMainMenu.resize(480, 320)
        self.btConfigProg = QtWidgets.QPushButton(frmMainMenu)
        self.btConfigProg.setGeometry(QtCore.QRect(20, 50, 140, 80))
        self.btConfigProg.setStyleSheet("")
        self.btConfigProg.setObjectName("btConfigProg")
        self.btInitProg = QtWidgets.QPushButton(frmMainMenu)
        self.btInitProg.setGeometry(QtCore.QRect(320, 50, 140, 80))
        self.btInitProg.setObjectName("btInitProg")
        self.btTestOutNPN = QtWidgets.QPushButton(frmMainMenu)
        self.btTestOutNPN.setGeometry(QtCore.QRect(20, 190, 140, 80))
        self.btTestOutNPN.setStyleSheet("")
        self.btTestOutNPN.setObjectName("btTestOutNPN")
        self.btTestOutPNP = QtWidgets.QPushButton(frmMainMenu)
        self.btTestOutPNP.setGeometry(QtCore.QRect(170, 190, 140, 80))
        self.btTestOutPNP.setStyleSheet("")
        self.btTestOutPNP.setObjectName("btTestOutPNP")
        self.btTestOutRelay = QtWidgets.QPushButton(frmMainMenu)
        self.btTestOutRelay.setGeometry(QtCore.QRect(320, 190, 140, 80))
        self.btTestOutRelay.setStyleSheet("")
        self.btTestOutRelay.setObjectName("btTestOutRelay")
        self.txHidden = QtWidgets.QLineEdit(frmMainMenu)
        self.txHidden.setGeometry(QtCore.QRect(10, 10, 31, 22))
        self.txHidden.setObjectName("txHidden")

        self.retranslateUi(frmMainMenu)
        QtCore.QMetaObject.connectSlotsByName(frmMainMenu)

    def retranslateUi(self, frmMainMenu):
        _translate = QtCore.QCoreApplication.translate
        frmMainMenu.setWindowTitle(_translate("frmMainMenu", "Form"))
        self.btConfigProg.setToolTip(_translate("frmMainMenu", "<html><head/><body><p><br/></p></body></html>"))
        self.btConfigProg.setText(_translate("frmMainMenu", "Configurar\n"
"Programas"))
        self.btInitProg.setText(_translate("frmMainMenu", "Iniciar\n"
"Programas"))
        self.btTestOutNPN.setToolTip(_translate("frmMainMenu", "<html><head/><body><p><br/></p></body></html>"))
        self.btTestOutNPN.setText(_translate("frmMainMenu", "Testar\n"
"Saida NPN"))
        self.btTestOutPNP.setToolTip(_translate("frmMainMenu", "<html><head/><body><p><br/></p></body></html>"))
        self.btTestOutPNP.setText(_translate("frmMainMenu", "Testar\n"
"Saida PNP"))
        self.btTestOutRelay.setToolTip(_translate("frmMainMenu", "<html><head/><body><p><br/></p></body></html>"))
        self.btTestOutRelay.setText(_translate("frmMainMenu", "Testar\n"
"Saida Rele"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmMainMenu = QtWidgets.QWidget()
    ui = Ui_frmMainMenu()
    ui.setupUi(frmMainMenu)
    frmMainMenu.show()
    sys.exit(app.exec_())
