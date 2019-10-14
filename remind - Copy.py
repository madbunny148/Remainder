# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def notify(self):
        #print("hello")
        date=""
        rtime=""
        topic=""
        tid=""
        connection=sqlite3.connect("reminder.db")
        query="SELECT * FROM record WHERE EXECUTED=0 LIMIT 1"
        result=connection.execute(query)
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        for row in records:
            print(row[0])
            date=row[2]
            rtime=row[3]
            topic=row[0]
            tid=(str(row[5]))
           # tid1=(str(tid))
        print(rtime,topic,tid)

        alarm_input =rtime
        while True:
            try:
                alarm_time = [int(n) for n in alarm_input.split(":")]
                if self.check_alarm_input(alarm_time):
                    break
                else:
                    raise ValueError
            except ValueError:
                print("ERROR: Enter time in HH:MM or HH:MM:SS format")


        # Convert the alarm time from [H:M] or [H:M:S] to second    s
        seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
        alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])
        # Get the current time of day in seconds
        now = datetime.datetime.now()
        current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])
        time_diff_seconds = alarm_seconds - current_time_seconds
        # If time difference is negative, set alarm for next day
        if time_diff_seconds < 0:
            time_diff_seconds += 86400 # number of seconds in a day

        # Display the amount of time until the alarm goes off
        print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

        # Sleep until the alarm goes off
        time.sleep(time_diff_seconds)

        # Time for the alarm to go off
        print("Wake Up!")
        print("Wake Up!")
        self.showDialog(topic)
        query="UPDATE record set EXECUTED =1 WHERE tid=?"
        cursor = connection.cursor()
        print(type(tid))
        cursor.execute(query,(tid))
        connection.commit()
        print(result)
          
    def showChildWindow(self):
        self.Dialog=QtWidgets.QDialog()
        self.ui=Ui_Dialog2()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        
    def updateWindow(self):
        self.Dialog=QtWidgets.QDialog()
        self.ui=Ui_Dialog3()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()

    def check_alarm_input(self,alarm_time):
        if len(alarm_time) == 1: # [Hour] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0:
                return True
            if len(alarm_time) == 2: # [Hour:Minute] Format
                if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                    alarm_time[1] < 60 and alarm_time[1] >= 0:
                    return True
        elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
            if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
                    alarm_time[1] < 60 and alarm_time[1] >= 0 and \
                    alarm_time[2] < 60 and alarm_time[2] >= 0:
                return True
        return False
            
    def showDialog(self,topic):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(topic)
        msgBox.setWindowTitle("QMessageBox Example")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
            msgBox.done(1)

        
    def regvalue(self):
        TOPIC=self.textbox1.toPlainText()
        DECSRIPTION="descr"
        DATE = self.dateEdit.date()
        DATE = DATE.toString("yyyy-MM-dd")
        TIME=self.timeEdit.time()
        TIME = TIME.toString("hh:mm:ss")
        EXECUTED=0
        print(TIME)


        connection = sqlite3.connect("reminder.db")
        connection.execute("INSERT INTO record VALUES(?,?,?,?,?,?)",(TOPIC,DECSRIPTION,DATE,TIME,EXECUTED,None))
        connection.commit()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(213, 286)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl1.setGeometry(QtCore.QRect(40, 40, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl1.setFont(font)
        self.lbl1.setObjectName("lbl1")
        self.lbl2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl2.setGeometry(QtCore.QRect(20, 100, 51, 16))
        self.lbl2.setObjectName("lbl2")
        self.lbl3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl3.setGeometry(QtCore.QRect(20, 140, 35, 10))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl3.setFont(font)
        self.lbl3.setObjectName("lbl3")
        self.lbl4 = QtWidgets.QLabel(self.centralwidget)
        self.lbl4.setGeometry(QtCore.QRect(20, 180, 35, 10))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl4.setFont(font)
        self.lbl4.setObjectName("lbl4")
        self.textbox1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textbox1.setGeometry(QtCore.QRect(90, 100, 104, 20))
        self.textbox1.setObjectName("textbox1")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(20, 220, 56, 17))
        self.button1.clicked.connect(self.regvalue)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(120, 220, 71, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(20, 250, 51, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button3.setFont(font)
        self.button3.setObjectName("button3")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(80, 250, 51, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button4.setFont(font)
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(140, 250, 51, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button5.setFont(font)
        self.button5.setObjectName("button5")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(90, 140, 101, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(90, 180, 101, 22))
        self.timeEdit.setObjectName("timeEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl1.setText(_translate("MainWindow", "REMAINDER"))
        self.lbl2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Subject</span></p></body></html>"))
        self.lbl3.setText(_translate("MainWindow", "Date"))
        self.lbl4.setText(_translate("MainWindow", "Time"))
        self.button1.setText(_translate("MainWindow", "SAVE"))
        self.button2.setText(_translate("MainWindow", "NOTIFY ME"))
        self.button3.setText(_translate("MainWindow", "VIEW"))
        self.button4.setText(_translate("MainWindow", "UPDATE"))
        self.button5.setText(_translate("MainWindow", "DELETE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
