# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(750, 487)
        Dialog.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Dialog.setMouseTracking(False)
        Dialog.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.lcd = QtWidgets.QLCDNumber(Dialog)
        self.lcd.setGeometry(QtCore.QRect(20, 140, 371, 71))
        self.lcd.setStyleSheet("")
        self.lcd.setObjectName("lcd")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 240, 371, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid.setContentsMargins(1, 1, 1, 1)
        self.grid.setSpacing(6)
        self.grid.setObjectName("grid")
        self.b5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b5.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.b5.setObjectName("b5")
        self.grid.addWidget(self.b5, 1, 1, 1, 1)
        self.b7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b7.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.b7.setObjectName("b7")
        self.grid.addWidget(self.b7, 0, 0, 1, 1)
        self.b4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b4.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"\n"
"text-decoration: none;\n"
"\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.b4.setObjectName("b4")
        self.grid.addWidget(self.b4, 1, 0, 1, 1)
        self.b1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b1.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"\n"
"text-decoration: none;\n"
"\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.b1.setObjectName("b1")
        self.grid.addWidget(self.b1, 2, 0, 1, 1)
        self.b6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b6.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.b6.setObjectName("b6")
        self.grid.addWidget(self.b6, 1, 2, 1, 1)
        self.b8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b8.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.b8.setObjectName("b8")
        self.grid.addWidget(self.b8, 0, 1, 1, 1)
        self.b9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b9.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.b9.setObjectName("b9")
        self.grid.addWidget(self.b9, 0, 2, 1, 1)
        self.b2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b2.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.b2.setObjectName("b2")
        self.grid.addWidget(self.b2, 2, 1, 1, 1)
        self.b3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b3.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.b3.setObjectName("b3")
        self.grid.addWidget(self.b3, 2, 2, 1, 1)
        self.bApagar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bApagar.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"text-decoration: none;\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.bApagar.setObjectName("bApagar")
        self.grid.addWidget(self.bApagar, 3, 0, 1, 1)
        self.b0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.b0.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.b0.setObjectName("b0")
        self.grid.addWidget(self.b0, 3, 1, 1, 1)
        self.bEnter = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.bEnter.setStyleSheet("background-color: #008CBA; /* blue */\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"display: inline-block;\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.bEnter.setObjectName("bEnter")
        self.grid.addWidget(self.bEnter, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(470, 60, 191, 81))
        self.label.setStyleSheet("font: 75 28pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(410, 140, 321, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_nome = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_nome.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label_nome.setObjectName("label_nome")
        self.verticalLayout.addWidget(self.label_nome)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.verticalLayout.addWidget(self.lineEdit_nome)
        self.label_senha = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_senha.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label_senha.setObjectName("label_senha")
        self.verticalLayout.addWidget(self.label_senha)
        self.lineEdit_senha = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.verticalLayout.addWidget(self.lineEdit_senha)
        self.label_funcao = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_funcao.setStyleSheet("font: 63 11pt \"Yu Gothic UI Semibold\";\n"
"")
        self.label_funcao.setObjectName("label_funcao")
        self.verticalLayout.addWidget(self.label_funcao)
        self.lineEdit_funcao = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_funcao.setText("")
        self.lineEdit_funcao.setObjectName("lineEdit_funcao")
        self.verticalLayout.addWidget(self.lineEdit_funcao)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bLimpar = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.bLimpar.setStyleSheet("\n"
"\n"
"\n"
"background-color: rgb(108, 108, 108);\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"text-align: center;\n"
"text-decoration: none;\n"
"\n"
"font-size: 16px;\n"
"border-radius: 8px;")
        self.bLimpar.setObjectName("bLimpar")
        self.horizontalLayout.addWidget(self.bLimpar)
        self.bCadastrar = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.bCadastrar.setStyleSheet("background-color: rgb(108, 108, 108);\n"
"border: none;\n"
" color: white;\n"
"padding: 15px 32px;\n"
"\n"
"text-decoration: none;\n"
"\n"
"font-size: 16px;\n"
"border-radius: 8px;font: 11pt \"MS Shell Dlg 2\";")
        self.bCadastrar.setObjectName("bCadastrar")
        self.horizontalLayout.addWidget(self.bCadastrar)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.b5.setText(_translate("Dialog", "5"))
        self.b7.setText(_translate("Dialog", "7"))
        self.b4.setText(_translate("Dialog", "4"))
        self.b1.setText(_translate("Dialog", "1"))
        self.b6.setText(_translate("Dialog", "6"))
        self.b8.setText(_translate("Dialog", "8"))
        self.b9.setText(_translate("Dialog", "9"))
        self.b2.setText(_translate("Dialog", "2"))
        self.b3.setText(_translate("Dialog", "3"))
        self.bApagar.setText(_translate("Dialog", "Apagar"))
        self.b0.setText(_translate("Dialog", "0"))
        self.bEnter.setText(_translate("Dialog", "Enter"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.label_nome.setText(_translate("Dialog", "Nome completo:"))
        self.label_senha.setText(_translate("Dialog", "Senha:"))
        self.label_funcao.setText(_translate("Dialog", "Função:"))
        self.bLimpar.setText(_translate("Dialog", "limpar"))
        self.bCadastrar.setText(_translate("Dialog", "Cadastrar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())