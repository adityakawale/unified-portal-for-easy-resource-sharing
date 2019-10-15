# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Chat_action.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from Final_UI.Search import Ui_Search


class Ui_ChatRole(object):
    def searchfn(self):
        self.Search = QtWidgets.QDialog()
        self.ui = Ui_Search()
        self.ui.setupUi(self.Search)
        self.Search.show()

    def receivefn(self):
            pass

    def setupUi(self, ChatRole):
        ChatRole.setObjectName("ChatRole")
        ChatRole.resize(340, 233)
        ChatRole.setStyleSheet("background-color: rgb(160, 160, 160);                        ")
        self.gridLayout = QtWidgets.QGridLayout(ChatRole)
        self.gridLayout.setObjectName("gridLayout")
        self.server = QtWidgets.QPushButton(ChatRole)
        self.server.setObjectName("server")
        self.gridLayout.addWidget(self.server, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(ChatRole)
        self.label.setStyleSheet("background-color: rgb(65, 204, 82);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 3)
        self.client = QtWidgets.QPushButton(ChatRole)
        self.client.setObjectName("client")
        self.gridLayout.addWidget(self.client, 2, 1, 1, 1)

        self.client.clicked.connect(self.searchfn)
        self.server.clicked.connect(self.receivefn)

        self.retranslateUi(ChatRole)
        QtCore.QMetaObject.connectSlotsByName(ChatRole)

    def retranslateUi(self, ChatRole):
        _translate = QtCore.QCoreApplication.translate
        ChatRole.setWindowTitle(_translate("ChatRole", "ChatRole"))
        self.server.setText(_translate("ChatRole", "Recieve"))
        self.label.setText(_translate("ChatRole", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">What would you like to do?</span></p></body></html>"))
        self.client.setText(_translate("ChatRole", "Find people!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatRole = QtWidgets.QDialog()
    ui = Ui_ChatRole()
    ui.setupUi(ChatRole)
    ChatRole.show()
    sys.exit(app.exec_())

