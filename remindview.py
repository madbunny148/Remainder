# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewrecords.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):
    def delete(self):
        connection=sqlite3.connect("reminder.db")
        row=self.tableWidget.currentRow()
        data=self.tableWidget.item(row,5).text()
        print(row)
        query="DELETE FROM record WHERE ID=?"
        cursor = connection.cursor()
        
        cursor.execute(query,(data,))
        connection.commit()
        self.tableWidget.setRowCount(0)
        self.loadData()
        
        
    def loadData(self):
        connection=sqlite3.connect("reminder.db")
        query="SELECT * from record"
        result=connection.execute(query)
        self.tableWidget.setRowCount(0)
        

        for row_number,row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 650)
        Dialog.setStyleSheet("background-color: rgb(255, 85, 0);\n"
"background-color: rgb(235, 249, 255);")
        Dialog.setModal(False)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(170, 120, 650, 400))
        self.tableWidget.setStyleSheet("background-color: rgb(85, 255, 127);\n"
"background-color: rgb(85, 255, 255);")
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(6)
        self.tableWidget.hideColumn(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 50, 131, 41))
        self.pushButton.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"color: rgb(85, 0, 0);\n"
"background-color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loadData)

        self.pushButton2 = QtWidgets.QPushButton(Dialog)
        self.pushButton2.setGeometry(QtCore.QRect(140, 50, 131, 41))
        self.pushButton2.setStyleSheet("background-color: rgb(85, 255, 0);\n"
"color: rgb(85, 0, 0);\n"
"background-color: rgb(85, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 18pt \"MS Shell Dlg 2\";")
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.clicked.connect(self.delete)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Dialog", "SHOW"))
        self.pushButton2.setText(_translate("Dialog", "DELETE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
