# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUppage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

mydb = mysql.connector.connect(

host = "localhost",
user = "root",
passwd = "aditya",
database = "cn"

)

class Ui_SignUppage(object):
    def create_account(self):
        roll = self.Roll_input.text()
        name = self.Name_input.text()
        dept = self.Department_input.text()
        year = self.Year_input.text()
        divison = self.Division_input.text()
        passd = self.Password_input.text()
        cp = self.lineEdit.text()

        try:
            if mydb:
                print("Connected to Database")
        except:
            print("Problem in connecting the Database")
            exit;
        mycursor = mydb.cursor()
        query = """insert into registered_students(roll,name,dept,year,divison,passd) values(%s,%s,%s,%s,%s,%s)"""
        insert_data = (roll,name,dept,year,divison,passd)
        if passd == cp:

            mycursor.execute(query,insert_data)
            mydb.commit()
            print("Successfull Registration")
            mycursor.close()
        else:
            print("Error : Passwords dont match!")

    def setupUi(self, SignUppage):
        SignUppage.setObjectName("SignUppage")
        SignUppage.resize(400, 284)
        self.horizontalLayoutWidget = QtWidgets.QWidget(SignUppage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 220, 341, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.CreateAcc = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.CreateAcc.setObjectName("CreateAcc")
        self.horizontalLayout.addWidget(self.CreateAcc)
        self.Clear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Clear.setObjectName("Clear")
        self.horizontalLayout.addWidget(self.Clear)
        self.gridLayoutWidget = QtWidgets.QWidget(SignUppage)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 341, 198))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Name.setObjectName("Name")
        self.gridLayout.addWidget(self.Name, 2, 0, 1, 1)
        self.Password = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Password.setObjectName("Password")
        self.gridLayout.addWidget(self.Password, 7, 0, 1, 1)
        self.Roll_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Roll_input.setObjectName("Roll_input")
        self.gridLayout.addWidget(self.Roll_input, 1, 1, 1, 1)
        self.Password_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_input.setObjectName("Password_input")
        self.gridLayout.addWidget(self.Password_input, 7, 1, 1, 1)
        self.Name_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Name_input.setText("")
        self.Name_input.setObjectName("Name_input")
        self.gridLayout.addWidget(self.Name_input, 2, 1, 1, 1)
        self.Roll = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Roll.setObjectName("Roll")
        self.gridLayout.addWidget(self.Roll, 1, 0, 1, 1)
        self.Division = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Division.setObjectName("Division")
        self.gridLayout.addWidget(self.Division, 6, 0, 1, 1)
        self.ConfirmPassword = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ConfirmPassword.setObjectName("ConfirmPassword")
        self.gridLayout.addWidget(self.ConfirmPassword, 8, 0, 1, 1)
        self.Year = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Year.setObjectName("Year")
        self.gridLayout.addWidget(self.Year, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 8, 1, 1, 1)
        self.Department = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Department.setObjectName("Department")
        self.gridLayout.addWidget(self.Department, 3, 0, 1, 1)
        self.Department_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Department_input.setObjectName("Department_input")
        self.gridLayout.addWidget(self.Department_input, 3, 1, 1, 1)
        self.Year_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Year_input.setObjectName("Year_input")
        self.gridLayout.addWidget(self.Year_input, 4, 1, 1, 1)
        self.Division_input = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Division_input.setObjectName("Division_input")
        self.gridLayout.addWidget(self.Division_input, 6, 1, 1, 1)
        self.retranslateUi(SignUppage)
        QtCore.QMetaObject.connectSlotsByName(SignUppage)
        self.CreateAcc.clicked.connect(self.create_account)   #create account event

    def retranslateUi(self, SignUppage):
        _translate = QtCore.QCoreApplication.translate
        SignUppage.setWindowTitle(_translate("SignUppage", "Register"))
        self.CreateAcc.setText(_translate("SignUppage", "Create Account"))
        self.Clear.setText(_translate("SignUppage", "Clear"))
        self.Name.setText(_translate("SignUppage", "Name"))
        self.Password.setText(_translate("SignUppage", "Password"))
        self.Roll_input.setPlaceholderText(_translate("SignUppage", "Enter your username"))
        self.Password_input.setPlaceholderText(_translate("SignUppage", "Enter your password"))
        self.Name_input.setPlaceholderText(_translate("SignUppage", "Enter your name"))
        self.Roll.setText(_translate("SignUppage", "Roll"))
        self.Division.setText(_translate("SignUppage", "Division"))
        self.ConfirmPassword.setText(_translate("SignUppage", "Confirm Password"))
        self.Year.setText(_translate("SignUppage", "Year"))
        self.lineEdit.setPlaceholderText(_translate("SignUppage", "Enter Password Again"))
        self.Department.setText(_translate("SignUppage", "Department"))
        self.Department_input.setPlaceholderText(_translate("SignUppage", "Enter your Department"))
        self.Year_input.setPlaceholderText(_translate("SignUppage", "Enter your Year"))
        self.Division_input.setPlaceholderText(_translate("SignUppage", "Enter your Division"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUppage = QtWidgets.QDialog()
    ui = Ui_SignUppage()
    ui.setupUi(SignUppage)
    SignUppage.show()
    sys.exit(app.exec_())
