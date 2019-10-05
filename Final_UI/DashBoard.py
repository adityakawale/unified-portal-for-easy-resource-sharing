# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\DashBoard.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import LoginPage as lp

class Ui_DashBoard(object):
    res = ""
    def refresh_clicked(self):
        self.who.setText(self.res)

    def setupUi(self, DashBoard,res):
        DashBoard.setObjectName("DashBoard")
        DashBoard.resize(640, 480)
        DashBoard.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.centralwidget = QtWidgets.QWidget(DashBoard)
        self.centralwidget.setObjectName("centralwidget")
        self.Welcome = QtWidgets.QLabel(self.centralwidget)
        self.Welcome.setGeometry(QtCore.QRect(150, 60, 351, 111))
        self.Welcome.setTextFormat(QtCore.Qt.AutoText)
        self.Welcome.setAlignment(QtCore.Qt.AlignCenter)
        self.Welcome.setObjectName("Welcome")
        self.FileSharing = QtWidgets.QPushButton(self.centralwidget)
        self.FileSharing.setGeometry(QtCore.QRect(110, 150, 201, 101))
        self.FileSharing.setStyleSheet("background-color: rgb(65, 205, 82);")
        self.FileSharing.setObjectName("FileSharing")
        self.Chat = QtWidgets.QPushButton(self.centralwidget)
        self.Chat.setGeometry(QtCore.QRect(330, 150, 201, 101))
        self.Chat.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Chat.setObjectName("Chat")
        self.Elibrary = QtWidgets.QPushButton(self.centralwidget)
        self.Elibrary.setGeometry(QtCore.QRect(110, 270, 201, 101))
        self.Elibrary.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Elibrary.setObjectName("Elibrary")
        self.Report = QtWidgets.QPushButton(self.centralwidget)
        self.Report.setGeometry(QtCore.QRect(330, 270, 201, 101))
        self.Report.setStyleSheet("background-color: rgb(65, 205, 82);")
        self.Report.setObjectName("Report")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(359, 0, 271, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.who = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.who.setText("")
        self.who.setObjectName("who")
        self.horizontalLayout.addWidget(self.who)
        self.refresh = QtWidgets.QPushButton(self.centralwidget)
        self.refresh.setGeometry(QtCore.QRect(260, 6, 93, 28))
        self.refresh.setObjectName("refresh")
        DashBoard.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DashBoard)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        DashBoard.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DashBoard)
        self.statusbar.setObjectName("statusbar")
        DashBoard.setStatusBar(self.statusbar)
        self.actionChange_password = QtWidgets.QAction(DashBoard)
        self.actionChange_password.setObjectName("actionChange_password")
        self.actionLogout = QtWidgets.QAction(DashBoard)
        self.actionLogout.setObjectName("actionLogout")
        self.actionAccount_Details = QtWidgets.QAction(DashBoard)
        self.actionAccount_Details.setObjectName("actionAccount_Details")
        self.menuSettings.addAction(self.actionAccount_Details)
        self.menuSettings.addAction(self.actionChange_password)
        self.menuSettings.addAction(self.actionLogout)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.res = res;
        self.refresh.clicked.connect(self.refresh_clicked)

        self.retranslateUi(DashBoard)
        QtCore.QMetaObject.connectSlotsByName(DashBoard)

    def retranslateUi(self, DashBoard):
        _translate = QtCore.QCoreApplication.translate
        DashBoard.setWindowTitle(_translate("DashBoard", "DashBoard"))
        self.Welcome.setText(_translate("DashBoard", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">** DASHBOARD **</span></p></body></html>"))
        self.FileSharing.setText(_translate("DashBoard", "FileSharing"))
        self.Chat.setText(_translate("DashBoard", "Chat"))
        self.Elibrary.setText(_translate("DashBoard", "E-library"))
        self.Report.setText(_translate("DashBoard", "Report"))
        self.label_2.setText(_translate("DashBoard", "<html><head/><body><p><span style=\" font-size:11pt;\">Logged in :</span></p></body></html>"))
        self.refresh.setText(_translate("DashBoard", "Refresh"))
        self.menuSettings.setTitle(_translate("DashBoard", "Settings"))
        self.actionChange_password.setText(_translate("DashBoard", "Change password"))
        self.actionLogout.setText(_translate("DashBoard", "Logout"))
        self.actionAccount_Details.setText(_translate("DashBoard", "Account Details"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DashBoard = QtWidgets.QMainWindow()
    ui = Ui_DashBoard()
    ui.setupUi(DashBoard)
    DashBoard.show()
    sys.exit(app.exec_())

