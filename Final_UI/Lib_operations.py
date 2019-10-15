# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Lib_operations.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymsgbox
import mysql.connector as conn
mydb = conn.connect(host="localhost",username="root",passwd="",database="pccoe")
mycurr = mydb.cursor()

class Ui_Lib_operations(object):

    fileloc = ""

    def convertToBinaryData(self, filename):
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData

    def insertBLOB(self, id, name, file_data):
        try:
            sql_insert_blob_query = """ INSERT INTO material
                              (id, name, file_data) VALUES (%s,%s,%s)"""

            file_to_insert = self.convertToBinaryData(file_data)

            # Convert data into tuple format
            insert_blob_tuple = (id, name, file_to_insert)
            result = mycurr.execute(sql_insert_blob_query, insert_blob_tuple)
            mydb.commit()
            pymsgbox.alert('File Inserted in Database Succesfully!')

        except conn.Error as error:
            pymsgbox.alert('Error while pushing the file to database!')

        finally:
            if (mydb.is_connected()):
                mydb.close()
                pymsgbox.alert('Connection to Database closed!')

    def pushfn(self):
        mydb.connect(host="localhost",username="root",passwd="",database="pccoe")
        id = self.id_inp.text()
        name = self.name_ip.text()
        self.insertBLOB(id, name, self.fileloc)

    def deletefn(self):
        mydb.connect(host="localhost",username="root",passwd="",database="pccoe")
        id = self.id_inp.text()
        name = self.name_ip.text()
        try:
            query = "delete from material where id = %s and name = %s;"
            inputs = (id,name)
            mycurr.execute(query,inputs)
            mydb.commit()
            pymsgbox.alert('Deleted the File : %s'%name)
            mydb.close()
        except:
            pymsgbox.alert('Error occured : Check the details')


    def statsfn(self):
        mydb.connect(host="localhost",username="root",passwd="",database="pccoe")
        try:
            query = "select count(id) from material where id like 'PDF%'"
            mycurr.execute(query)
            pdf_nos = mycurr.fetchone()
            query1 = "select count(id) from material where id like 'TXT%'"
            mycurr.execute(query1)
            txt_nos = mycurr.fetchone()
            pymsgbox.alert('\n---------------------------\n'
                           'No. of TXT files : %s \n No. of PDF files : %s '
                           '\n---------------------------\n'%(txt_nos,pdf_nos))
            mydb.close()
        except:
            pymsgbox.alert('Error occured : Check the details')
        pass

    def locationfn(self):
        import easygui
        self.fileloc = easygui.fileopenbox()


    def setupUi(self, Lib_operations):
        Lib_operations.setObjectName("Lib_operations")
        Lib_operations.resize(640, 480)
        Lib_operations.setStyleSheet("background-color: rgb(199, 199, 199);")
        self.formLayoutWidget = QtWidgets.QWidget(Lib_operations)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 160, 491, 92))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.id_inp = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.id_inp.setObjectName("id_inp")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.id_inp)
        self.name_ip = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name_ip.setObjectName("name_ip")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_ip)
        self.Choose = QtWidgets.QPushButton(self.formLayoutWidget)
        self.Choose.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Choose.setObjectName("Choose")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.Choose)
        self.label_5 = QtWidgets.QLabel(Lib_operations)
        self.label_5.setGeometry(QtCore.QRect(70, 20, 501, 119))
        self.label_5.setStyleSheet("background-color: rgb(65, 205, 82);\n"
"font: 24pt \"Comic Sans MS\";")
        self.label_5.setObjectName("label_5")
        self.gridLayoutWidget = QtWidgets.QWidget(Lib_operations)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 290, 171, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Stats = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Stats.setStyleSheet("background-color: rgb(190, 200, 0);\n"
"background-color: rgb(84, 150, 200);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.Stats.setObjectName("Stats")
        self.gridLayout.addWidget(self.Stats, 3, 0, 1, 1)
        self.Delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Delete.setStyleSheet("background-color: rgb(200, 14, 18);\n"
"background-color: rgb(84, 150, 200);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.Delete.setObjectName("Delete")
        self.gridLayout.addWidget(self.Delete, 1, 0, 1, 1)
        self.Push = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Push.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"background-color: rgb(84, 150, 200);\n"
"font: 16pt \"MS Shell Dlg 2\";")
        self.Push.setObjectName("Push")
        self.gridLayout.addWidget(self.Push, 0, 0, 1, 1)
#####
        self.Choose.clicked.connect(self.locationfn)
        self.Push.clicked.connect(self.pushfn)
        self.Delete.clicked.connect(self.deletefn)
        self.Stats.clicked.connect(self.statsfn)

#####

        self.retranslateUi(Lib_operations)
        QtCore.QMetaObject.connectSlotsByName(Lib_operations)

    def retranslateUi(self, Lib_operations):
        _translate = QtCore.QCoreApplication.translate
        Lib_operations.setWindowTitle(_translate("Lib_operations", "LibOperations"))
        self.label.setText(_translate("Lib_operations", "Enter the id : "))
        self.label_2.setText(_translate("Lib_operations", "Enter the Name : "))
        self.label_3.setText(_translate("Lib_operations", "Enter the location of file:"))
        self.Choose.setText(_translate("Lib_operations", "Choose a file"))
        self.label_5.setText(_translate("Lib_operations", "<html><head/><body><p align=\"center\">        LIBRARY MANAGEMENT\n"
"</p></body></html>"))
        self.Stats.setText(_translate("Lib_operations", "STATS"))
        self.Delete.setText(_translate("Lib_operations", "DELETE"))
        self.Push.setText(_translate("Lib_operations", "PUSH"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Lib_operations = QtWidgets.QDialog()
    ui = Ui_Lib_operations()
    ui.setupUi(Lib_operations)
    Lib_operations.show()
    sys.exit(app.exec_())

