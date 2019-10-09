# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import pymsgbox
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import os

from Final_UI.LoginPage import Ui_LoginPage


class Ui_Initial(object):
    role = ""
    def jump_login(self,r):
        if r == self.Teacher:
            self.role = 0
            os.startfile('LoginPage_teacher.pyw')
        elif r == self.Student:
            self.role = 1
            os.startfile('LoginPage.pyw')
        elif r == self.Library:
            self.role = 2
            os.startfile('LoginPage_library.pyw')




        Initial.close()


    def setupUi(self, Initial):
        Initial.setObjectName("Initial")
        Initial.resize(637, 479)
        Initial.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.label = QtWidgets.QLabel(Initial)
        self.label.setGeometry(QtCore.QRect(110, 30, 399, 119))
        self.label.setStyleSheet("background-color: rgb(65, 205, 82);\n"
"font: 24pt \"Comic Sans MS\";")
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(Initial)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 170, 261, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.Teacher = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Teacher.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/teacher.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Teacher.setIcon(icon)
        self.Teacher.setIconSize(QtCore.QSize(90, 90))
        self.Teacher.setObjectName("Teacher")
        self.gridLayout.addWidget(self.Teacher, 1, 0, 1, 1)
        self.Student = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Student.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/student.JPG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Student.setIcon(icon1)
        self.Student.setIconSize(QtCore.QSize(90, 90))
        self.Student.setObjectName("Student")
        self.gridLayout.addWidget(self.Student, 1, 2, 1, 1)
        self.Library = QtWidgets.QPushButton(Initial)
        self.Library.setGeometry(QtCore.QRect(260, 300, 119, 99))
        self.Library.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Library.setIcon(icon2)
        self.Library.setIconSize(QtCore.QSize(90, 90))
        self.Library.setObjectName("Library")

        self.retranslateUi(Initial)
        QtCore.QMetaObject.connectSlotsByName(Initial)

        self.Teacher.clicked.connect(partial(self.jump_login,self.Teacher))
        self.Student.clicked.connect(partial(self.jump_login,self.Student))
        self.Library.clicked.connect(partial(self.jump_login,self.Library))

    def retranslateUi(self, Initial):
        _translate = QtCore.QCoreApplication.translate
        Initial.setWindowTitle(_translate("Initial", "Welcome"))
        self.label.setText(_translate("Initial", "<html><head/><body><p align=\"center\">        WHO ARE YOU?</p></body></html>"))
        self.Teacher.setToolTip(_translate("Initial", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Teacher</span></p></body></html>"))
        self.Student.setToolTip(_translate("Initial", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Student</span></p></body></html>"))
        self.Library.setToolTip(_translate("Initial", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Library</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Initial = QtWidgets.QDialog()
    ui = Ui_Initial()
    ui.setupUi(Initial)
    Initial.show()
    sys.exit(app.exec_())

