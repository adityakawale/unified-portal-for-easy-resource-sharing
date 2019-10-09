# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Signuppage.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import pymsgbox
import socket
import pymsgbox



def error_function(obj):
    pymsgbox.alert("Passwords don't match","Error")
    obj.password_ip.clear()
    obj.cpassword_ip.clear()

def successfull_function(obj):
    pymsgbox.alert("Welcome to the System!","Success")
    obj.clear_cliked()

class Signuppage(object):

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            passwd="",
            database="pccoe"
        )
        pymsgbox.alert('Connected to Student Database!')
    def __del__(self):
        self.mydb.close()

    def enroll_user(self):
        mycursor = self.mydb.cursor()
        erp = self.erp_ip.text()
        roll = self.roll_ip.text()
        year = self.year_ip.text()
        dv = self.div_ip.text()
        name = self.name_ip.text()
        pa = self.password_ip.text()
        cpa = self.cpassword_ip.text()
        #ip = socket.gethostbyname(socket.gethostname())

        if (erp.isalnum() and roll.isalnum() and year.isalnum() and dv.isalnum() and name.isalnum() and pa.isalnum() and cpa.isalnum()):
            if (len(pa) <= 6 and len(cpa)<=6 ):
                if pa == cpa:
                    inputs = (erp,roll,year,dv,name,pa,"NA","NULL")
                    query = "insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    mycursor.execute(query,inputs)
                    self.mydb.commit()
                    successfull_function(self)
                    mycursor.close()
                    self.mydb.close()
                else:
                    error_function(self)
            else:
                pymsgbox.alert('Enter 8 alphanumeric characters only!')
                self.password_ip.clear()
                self.cpassword_ip.clear()
        else:
            pymsgbox.alert('Provide Alphanumeric Inputs Only!')
            return

    def clear_cliked(self):
        self.erp_ip.clear()
        self.roll_ip.clear()
        self.year_ip.clear()
        self.div_ip.clear()
        self.name_ip.clear()
        self.password_ip.clear()
        self.cpassword_ip.clear()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 566)
        Dialog.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 30, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(49, 200, 33);")
        self.label.setObjectName("label")
        self.formFrame = QtWidgets.QFrame(Dialog)
        self.formFrame.setGeometry(QtCore.QRect(120, 140, 401, 221))
        self.formFrame.setStyleSheet("")
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formFrame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formFrame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formFrame)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formFrame)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formFrame)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formFrame)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_2 = QtWidgets.QLabel(self.formFrame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.erp_ip = QtWidgets.QLineEdit(self.formFrame)
        self.erp_ip.setObjectName("erp_ip")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.erp_ip)
        self.roll_ip = QtWidgets.QLineEdit(self.formFrame)
        self.roll_ip.setObjectName("roll_ip")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.roll_ip)
        self.year_ip = QtWidgets.QLineEdit(self.formFrame)
        self.year_ip.setObjectName("year_ip")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.year_ip)
        self.div_ip = QtWidgets.QLineEdit(self.formFrame)
        self.div_ip.setObjectName("div_ip")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.div_ip)
        self.name_ip = QtWidgets.QLineEdit(self.formFrame)
        self.name_ip.setObjectName("name_ip")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.name_ip)
        self.password_ip = QtWidgets.QLineEdit(self.formFrame)
        self.password_ip.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_ip.setObjectName("password_ip")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.password_ip)
        self.cpassword_ip = QtWidgets.QLineEdit(self.formFrame)
        self.cpassword_ip.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpassword_ip.setObjectName("cpassword_ip")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.cpassword_ip)
        self.clear = QtWidgets.QPushButton(Dialog)
        self.clear.setGeometry(QtCore.QRect(430, 380, 93, 28))
        self.clear.setObjectName("clear")
        self.enroll = QtWidgets.QPushButton(Dialog)
        self.enroll.setGeometry(QtCore.QRect(120, 450, 401, 71))
        self.enroll.setStyleSheet("background-color: rgb(49, 200, 33);\n"
"font: 28pt \"Nirmala UI\";")
        self.enroll.setObjectName("enroll")
        self.logo = QtWidgets.QLabel(Dialog)
        self.logo.setGeometry(QtCore.QRect(10, 0, 101, 111))
        self.logo.setMinimumSize(QtCore.QSize(101, 111))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Images/logog.JPG"))
        self.logo.setObjectName("logo")

        ###
        self.enroll.clicked.connect(self.enroll_user)
        self.clear.clicked.connect(self.clear_cliked)
        ###

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "SignUp"))
        self.label.setText(_translate("Dialog", " Hey ! New User....."))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Roll no.</span></p></body></html>"))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Year</span></p></body></html>"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Division</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Full Name</span></p></body></html>"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Password</span></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Confirm password</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">ERP no.</span></p></body></html>"))
        self.clear.setText(_translate("Dialog", "Clear"))
        self.enroll.setText(_translate("Dialog", "Enroll yourself !!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Signuppage()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

