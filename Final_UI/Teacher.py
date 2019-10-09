# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Teacher.ui'
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

class Ui_Teacher_Signup(object):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            username="root",
            passwd="",
            database="pccoe"
        )
        pymsgbox.alert('Connected to Teacher Database!')

    def __del__(self):
        self.mydb.close()

    def enroll_user(self):
        mycursor = self.mydb.cursor()
        erp = self.erp_ip.text()
        subid = self.subid_ip.text()
        name = self.name_ip.text()
        pa = self.password_ip.text()
        cpa = self.cpassword_ip.text()
        #ip = socket.gethostbyname(socket.gethostname())

        if (erp.isalnum()  and subid.isalnum() and  pa.isalnum() and cpa.isalnum()):
            if (len(pa) <= 8 and len(cpa)<=8):
                if pa == cpa:
                    inputs = (erp,name,"NA","NULL",pa,subid)
                    query = "insert into teachers values(%s,%s,%s,%s,%s,%s)"
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
        self.subid_ip.clear()
        self.name_ip.clear()
        self.password_ip.clear()
        self.cpassword_ip.clear()

    def setupUi(self, Teacher_Signup):
        Teacher_Signup.setObjectName("Teacher_Signup")
        Teacher_Signup.resize(640, 565)
        Teacher_Signup.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.label = QtWidgets.QLabel(Teacher_Signup)
        self.label.setGeometry(QtCore.QRect(180, 30, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(49, 200, 33);")
        self.label.setObjectName("label")
        self.formFrame = QtWidgets.QFrame(Teacher_Signup)
        self.formFrame.setGeometry(QtCore.QRect(120, 150, 401, 221))
        self.formFrame.setStyleSheet("")
        self.formFrame.setObjectName("formFrame")
        self.formLayout = QtWidgets.QFormLayout(self.formFrame)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formFrame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.erp_ip = QtWidgets.QLineEdit(self.formFrame)
        self.erp_ip.setObjectName("erp_ip")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.erp_ip)
        self.label_6 = QtWidgets.QLabel(self.formFrame)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.name_ip = QtWidgets.QLineEdit(self.formFrame)
        self.name_ip.setObjectName("name_ip")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.name_ip)
        self.label_16 = QtWidgets.QLabel(self.formFrame)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.subid_ip = QtWidgets.QLineEdit(self.formFrame)
        self.subid_ip.setObjectName("subid_ip")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.subid_ip)
        self.label_7 = QtWidgets.QLabel(self.formFrame)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.password_ip = QtWidgets.QLineEdit(self.formFrame)
        self.password_ip.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_ip.setObjectName("password_ip")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.password_ip)
        self.label_8 = QtWidgets.QLabel(self.formFrame)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.cpassword_ip = QtWidgets.QLineEdit(self.formFrame)
        self.cpassword_ip.setEchoMode(QtWidgets.QLineEdit.Password)
        self.cpassword_ip.setObjectName("cpassword_ip")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.cpassword_ip)
        self.logo = QtWidgets.QLabel(Teacher_Signup)
        self.logo.setGeometry(QtCore.QRect(20, 0, 101, 111))
        self.logo.setMinimumSize(QtCore.QSize(101, 111))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../Images/logog.JPG"))
        self.logo.setObjectName("logo")
        self.clear = QtWidgets.QPushButton(Teacher_Signup)
        self.clear.setGeometry(QtCore.QRect(440, 380, 93, 28))
        self.clear.setObjectName("clear")
        self.enroll = QtWidgets.QPushButton(Teacher_Signup)
        self.enroll.setGeometry(QtCore.QRect(130, 450, 401, 71))
        self.enroll.setStyleSheet("background-color: rgb(49, 200, 33);\n"
"font: 28pt \"Nirmala UI\";")
        self.enroll.setObjectName("enroll")
        ###
        self.enroll.clicked.connect(self.enroll_user)
        self.clear.clicked.connect(self.clear_cliked)
        ###
        self.retranslateUi(Teacher_Signup)
        QtCore.QMetaObject.connectSlotsByName(Teacher_Signup)

    def retranslateUi(self, Teacher_Signup):
        _translate = QtCore.QCoreApplication.translate
        Teacher_Signup.setWindowTitle(_translate("Teacher_Signup", "Teacher"))
        self.label.setText(_translate("Teacher_Signup", " Hey ! New User....."))
        self.label_2.setText(_translate("Teacher_Signup", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">ERP no.</span></p></body></html>"))
        self.label_6.setText(_translate("Teacher_Signup", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Full Name</span></p></body></html>"))
        self.label_16.setText(_translate("Teacher_Signup", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Subject Id\n"
"</span></p></body></html>"))
        self.label_7.setText(_translate("Teacher_Signup", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\"> password</span></p></body></html>"))
        self.label_8.setText(_translate("Teacher_Signup", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Confirm password</span></p></body></html>"))
        self.clear.setText(_translate("Teacher_Signup", "Clear"))
        self.enroll.setText(_translate("Teacher_Signup", "Enroll yourself !!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Teacher_Signup = QtWidgets.QDialog()
    ui = Ui_Teacher_Signup()
    ui.setupUi(Teacher_Signup)
    Teacher_Signup.show()
    sys.exit(app.exec_())

