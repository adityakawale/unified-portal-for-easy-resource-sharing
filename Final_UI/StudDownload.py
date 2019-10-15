# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudDownload.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import pymsgbox
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as conn
import os

mydb = conn.connect(host="localhost",username="root",passwd="",database="pccoe")
mycurr = mydb.cursor()

class Ui_StudDownload(object):
    def downloadfn(self):
        try:
            id = self.id_inp.text()
            name = self.name_ip.text()
            query = "select file_data from material where id = %s and name = %s"
            inputs = (id,name)
            mycurr.execute(query,inputs)
            filerecv = list(sum(mycurr,()))
            pymsgbox.alert('Done fetching!')
            if id[0:3] == 'PDF':
                import base64
                with open(os.path.expanduser(r'C:\Users\Aditya\Desktop\MyDownloads\%s.pdf')%name, "wb") as f:
                    f.write(filerecv[0])
            elif id[0:3] == 'TXT':
                pymsgbox.alert('yes it is text')
                result = bytes(filerecv[0],'utf-8')
                with open(os.path.expanduser(r'C:\Users\Aditya\Desktop\MyDownloads\%s.txt') % name, "wb") as f:
                    f.write(result)

        except:
            pymsgbox.alert('Error in downloading file')

    def setupUi(self, StudDownload):
        StudDownload.setObjectName("StudDownload")
        StudDownload.resize(640, 480)
        StudDownload.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.formLayoutWidget = QtWidgets.QWidget(StudDownload)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 160, 491, 92))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.id_inp = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.id_inp.setObjectName("id_inp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.id_inp)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.name_ip = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_ip.setObjectName("name_ip")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_ip)
        self.label_5 = QtWidgets.QLabel(StudDownload)
        self.label_5.setGeometry(QtCore.QRect(70, 20, 501, 119))
        self.label_5.setStyleSheet("background-color: rgb(65, 205, 82);\n"
"font: 24pt \"Comic Sans MS\";")
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget = QtWidgets.QWidget(StudDownload)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 260, 171, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Download = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Download.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"background-color: rgb(84, 150, 200);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.Download.setObjectName("Push")
        self.gridLayout.addWidget(self.Download, 0, 0, 1, 1)

        self.Download.clicked.connect(self.downloadfn)

        self.retranslateUi(StudDownload)
        QtCore.QMetaObject.connectSlotsByName(StudDownload)

    def retranslateUi(self, StudDownload):
        _translate = QtCore.QCoreApplication.translate
        StudDownload.setWindowTitle(_translate("StudDownload", "Download"))
        self.label.setText(_translate("StudDownload", "Enter the id : "))
        self.label_2.setText(_translate("StudDownload", "Enter the Name : "))
        self.label_5.setText(_translate("StudDownload", "<html><head/><body><p align=\"center\">        LIBRARY MANAGEMENT\n"
"</p></body></html>"))
        self.Download.setText(_translate("StudDownload", "DOWNLOAD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudDownload = QtWidgets.QDialog()
    ui = Ui_StudDownload()
    ui.setupUi(StudDownload)
    StudDownload.show()
    sys.exit(app.exec_())

