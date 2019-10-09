# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginPage_library.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import socket

from PyQt5 import QtCore, QtGui, QtWidgets

from Final_UI.Library import Ui_LibrarySignup
from Final_UI.Signuppage import *
from Final_UI.DashBoard import *
import mysql.connector
import pymsgbox

try:
    mydb = mysql.connector.connect(
        host="localhost",
        username="root",
        passwd="",
        database="pccoe"
    )
except:
    pymsgbox.alert("Xampp Server not ON!")

class Ui_LoginPage(object):
    result = ""

    def __init__(self):
        global mydb
        self.mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            passwd="",
            database="pccoe"
        )

    def jump_signuppage(self):
        self.LibrarySignup = QtWidgets.QDialog()
        self.ui = Ui_LibrarySignup()
        self.ui.setupUi(self.LibrarySignup)
        self.LibrarySignup.show()

    def jump_dashboard(self):
        self.DashBoard = QtWidgets.QMainWindow()
        self.ui = Ui_DashBoard()
        self.ui.setupUi(self.DashBoard,self.result[0])
        self.DashBoard.show()


    def login_clicked(self,role):
        self.mydb.close()
        self.__init__()
        mycursor = self.mydb.cursor()
        us = self.username_ip.text()
        pa = self.password_ip.text()
        if (us.isalnum() and pa.isalnum()):
            query = "select name from library where erp = %s and pass = %s"
            inputs = (us,pa)

            mycursor.execute(query,inputs)
            self.result = list(sum(mycursor,()))
        else:
            pymsgbox.alert('Credentials not in alphanumeric manner!')
            return

        if not self.result:
            pymsgbox.alert('Wrong Credentials', 'Error')
        else:
            pymsgbox.alert("Logged in as : %s" %self.result[0], "Success")
            query = "update library set status = 'A' where name = %s"
            mycursor.execute(query,(self.result))
            self.mydb.commit()

            ip = socket.gethostbyname(socket.gethostname())
            query = "update library set ip = %s where name = %s"
            mycursor.execute(query,(ip,self.result[0]))
            self.mydb.commit()

            self.jump_dashboard()


    def clear_clicked(self):
        self.username_ip.clear()
        self.password_ip.clear()


    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(626, 480)
        LoginPage.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.gridLayoutWidget = QtWidgets.QWidget(LoginPage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(110, 201, 391, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.usernamelabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.usernamelabel.setObjectName("usernamelabel")
        self.gridLayout.addWidget(self.usernamelabel, 0, 0, 1, 1)
        self.password_ip = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.password_ip.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_ip.setObjectName("password_ip")
        self.gridLayout.addWidget(self.password_ip, 2, 1, 1, 1)
        self.username_ip = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.username_ip.setObjectName("username_ip")
        self.gridLayout.addWidget(self.username_ip, 0, 1, 1, 1)
        self.passwordlabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.passwordlabel.setObjectName("passwordlabel")
        self.gridLayout.addWidget(self.passwordlabel, 2, 0, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(LoginPage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 330, 391, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Login = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Login.setStyleSheet("\n"
"    background-color:rgb(49, 200, 33);\n"
"")
        self.Login.setObjectName("Login")
        self.horizontalLayout.addWidget(self.Login)
        self.Signup = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Signup.setStyleSheet("background-color:rgb(49, 200, 33);")
        self.Signup.setObjectName("Signup")
        self.horizontalLayout.addWidget(self.Signup)
        self.Clear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Clear.setStyleSheet("background-color:rgb(49, 200, 33);")
        self.Clear.setObjectName("Clear")
        self.horizontalLayout.addWidget(self.Clear)
        self.label = QtWidgets.QLabel(LoginPage)
        self.label.setGeometry(QtCore.QRect(220, 21, 191, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(49, 200, 33);")
        self.label.setObjectName("label")
        self.logo = QtWidgets.QLabel(LoginPage)
        self.logo.setGeometry(QtCore.QRect(10, 0, 101, 111))
        self.logo.setMinimumSize(QtCore.QSize(101, 111))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Images/logog.JPG"))
        self.logo.setObjectName("logo")

        self.Signup.clicked.connect(self.jump_signuppage)
        self.Login.clicked.connect(self.login_clicked)
        self.Clear.clicked.connect(self.clear_clicked)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "LoginPage"))
        self.usernamelabel.setText(_translate("LoginPage", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Username</span></p></body></html>"))
        self.passwordlabel.setText(_translate("LoginPage", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Password</span></p></body></html>"))
        self.Login.setText(_translate("LoginPage", "Login"))
        self.Signup.setText(_translate("LoginPage", "Signup"))
        self.Clear.setText(_translate("LoginPage", "Clear"))
        self.label.setText(_translate("LoginPage", " WELCOME"))
    def __del__(self):
        mycursor = self.mydb.cursor()
        print("Destructed")
        if self.result != "":
            query = "update library set status = 'NA',ip = NULL where name = %s"
            inputs = self.result
            mycursor.execute(query,inputs)
            self.mydb.commit()
            self.mydb.close()
        else:
            self.mydb.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QDialog()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())

