# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'after.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_after(object):
    def setupUi(self, after):
        after.setObjectName("after")
        after.resize(640, 480)
        self.buttonBox = QtWidgets.QDialogButtonBox(after)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(after)
        self.label.setGeometry(QtCore.QRect(170, 100, 341, 211))
        self.label.setObjectName("label")

        self.retranslateUi(after)
        self.buttonBox.accepted.connect(after.accept)
        self.buttonBox.rejected.connect(after.reject)
        QtCore.QMetaObject.connectSlotsByName(after)

    def retranslateUi(self, after):
        _translate = QtCore.QCoreApplication.translate
        after.setWindowTitle(_translate("after", "after"))
        self.label.setText(_translate("after", "File Sharing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    after = QtWidgets.QDialog()
    ui = Ui_after()
    ui.setupUi(after)
    after.show()
    sys.exit(app.exec_())
