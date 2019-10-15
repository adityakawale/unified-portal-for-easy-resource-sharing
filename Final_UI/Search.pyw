# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import pymsgbox
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as conn
mydb = conn.connect(host="127.0.0.1", username="root", passwd="", database="pccoe")

class Ui_Search(object):

    mycurr = ""

    def chat_room(self):
        s1 = self.Online.currentText()
        mydb.connect(host="127.0.0.1", username="root", passwd="", database="pccoe")
        self.mycurr = mydb.cursor()
        query = "select ip from students where name = %s"
        inputs = (s1,)
        self.mycurr.execute(query,inputs)
        HOST = self.mycurr.fetchone()


    def __init__(self):
        mydb.connect(host = "127.0.0.1",username = "root",passwd = "",database = "pccoe")
        self.mycurr = mydb.cursor()
        self.mycurr.execute("select name,ip from students where status = 'A'")


    def setupUi(self, Search):
        Search.setObjectName("Search")
        Search.resize(400, 300)
        Search.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.widget = QtWidgets.QWidget(Search)
        self.widget.setGeometry(QtCore.QRect(67, 30, 271, 241))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("background-color: rgb(65, 204, 82);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Online = QtWidgets.QComboBox(self.widget)
        self.Online.setObjectName("Online")
        self.verticalLayout.addWidget(self.Online)
        self.Start = QtWidgets.QPushButton(self.widget)
        self.Start.setObjectName("Start")
        self.verticalLayout.addWidget(self.Start)

        for i in self.mycurr:
            self.Online.addItem(i[0])

        self.Start.clicked.connect(self.chat_room)

        self.retranslateUi(Search)
        QtCore.QMetaObject.connectSlotsByName(Search)

    def retranslateUi(self, Search):
        _translate = QtCore.QCoreApplication.translate
        Search.setWindowTitle(_translate("Search", "Search"))
        self.label.setText(_translate("Search", "<html><head/><body><p><span style=\" font-size:12pt;\">See People who are online </span></p></body></html>"))
        self.Start.setText(_translate("Search", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Search = QtWidgets.QDialog()
    ui = Ui_Search()
    ui.setupUi(Search)
    Search.show()
    sys.exit(app.exec_())

