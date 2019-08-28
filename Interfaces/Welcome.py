# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Welcome(object):
    def setupUi(self, Welcome):
        Welcome.setObjectName("Welcome")
        Welcome.resize(400, 251)
        self.gridLayoutWidget = QtWidgets.QWidget(Welcome)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 10, 341, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Password.setObjectName("Password")
        self.gridLayout.addWidget(self.Password, 4, 0, 1, 1)
        self.Name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Name.setObjectName("Name")
        self.gridLayout.addWidget(self.Name, 1, 0, 1, 1)
        self.Name_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Name_input.setObjectName("Name_input")
        self.gridLayout.addWidget(self.Name_input, 1, 1, 1, 1)
        self.Password_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_input.setObjectName("Password_input")
        self.gridLayout.addWidget(self.Password_input, 4, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Welcome)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 160, 351, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Login = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Login.setObjectName("Login")
        self.horizontalLayout.addWidget(self.Login)
        self.SignUp = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.SignUp.setObjectName("SignUp")
        self.horizontalLayout.addWidget(self.SignUp)
        self.Clear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Clear.setObjectName("Clear")
        self.horizontalLayout.addWidget(self.Clear)

        self.retranslateUi(Welcome)
        QtCore.QMetaObject.connectSlotsByName(Welcome)

    def retranslateUi(self, Welcome):
        _translate = QtCore.QCoreApplication.translate
        Welcome.setWindowTitle(_translate("Welcome", "Welcome"))
        self.Password.setText(_translate("Welcome", "Password"))
        self.Name.setText(_translate("Welcome", "Name"))
        self.Name_input.setPlaceholderText(_translate("Welcome", "Enter your username"))
        self.Password_input.setPlaceholderText(_translate("Welcome", "Enter your password"))
        self.Login.setText(_translate("Welcome", "Login"))
        self.SignUp.setText(_translate("Welcome", "SignUp"))
        self.Clear.setText(_translate("Welcome", "Clear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Welcome = QtWidgets.QDialog()
    ui = Ui_Welcome()
    ui.setupUi(Welcome)
    Welcome.show()
    sys.exit(app.exec_())
