# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InputPassword.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Final_UI.LoginPage import *
import pymsgbox

class Ui_InputPassword(object):
    res = ""
    def changepasswordfn(self):
        mycursor = mydb.cursor()
        cp = self.newpass.text()
        query = "update students set pass = %s where name = %s"
        inputs = (cp, self.res)
        mycursor.execute(query,inputs)
        mydb.commit()
        mycursor.close()
        pymsgbox.alert("Successfully changed the password!","Success")

    def setupUi(self, InputPassword,res):
        InputPassword.setObjectName("InputPassword")
        InputPassword.resize(304, 149)
        InputPassword.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.formLayout = QtWidgets.QFormLayout(InputPassword)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(InputPassword)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.newpass = QtWidgets.QLineEdit(InputPassword)
        self.newpass.setObjectName("newpass")
        self.verticalLayout.addWidget(self.newpass)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.Change = QtWidgets.QPushButton(InputPassword)
        self.Change.setObjectName("Change")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Change)

        self.res = res
        self.Change.clicked.connect(self.changepasswordfn)

        self.retranslateUi(InputPassword)
        QtCore.QMetaObject.connectSlotsByName(InputPassword)

    def retranslateUi(self, InputPassword):
        _translate = QtCore.QCoreApplication.translate
        InputPassword.setWindowTitle(_translate("InputPassword", "Change_Password"))
        self.label.setText(_translate("InputPassword", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Enter Your new password:</span></p></body></html>"))
        self.Change.setText(_translate("InputPassword", "Change"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InputPassword = QtWidgets.QDialog()
    ui = Ui_InputPassword()
    ui.setupUi(InputPassword)
    InputPassword.show()
    sys.exit(app.exec_())

