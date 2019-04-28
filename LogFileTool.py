# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogFileTool.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtGui import , QString
from PyQt5.QtWidgets import (QFileDialog, QMessageBox, QTableWidget, QComboBox, QPushButton, QLabel, QCheckBox, QTableWidgetItem, QSlider)
from PyQt5.QtCore import QStringListModel
from PyQt5.QtCore import (Qt, pyqtSignal)
from os.path import expanduser
import os
from datetime import datetime

# http://pyqt.sourceforge.net/Docs/PyQt4/new_style_signals_slots.html
# https://stackoverflow.com/questions/3891465/how-to-connect-pyqtsignal-between-classes-in-pyqt

LogFileList = []


class MatchRecord:
    def __init__(self, MatchString):
        self.MatchString = MatchString
        self.Count = 0


class LogFileListClass:
    def __init__(self, PathFilename, name, timestamp):
        self.LogFilename = name
        self.LogPathFilename = PathFilename
        self.LogTimeStamp = timestamp


class CustomLabel(QLabel):
    global LogFileList

    DragAndDropSignal = QtCore.pyqtSignal()

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def CustomLabelOutput(self):
        print("CustomLabel Here")

    def dragEnterEvent(self, event):
        print( "dragEnterEvent" + str( event ) )
        if event.mimeData().hasText():
            print( "dragEnterEvent hasText" )
            event.accept()
        else:
            print( "dragEnterEvent NOT hasText" )
            event.ignore()

        if event.mimeData().hasUrls():
            print( "dragEnterEvent hasUrls" )
            for url in event.mimeData().urls():
                print(url)

        else:
            print( "dragEnterEvent NOT hasHrls" )

    def dropEvent(self, e):
        print( "dropEvent:-" + str( e.mimeData().text() ))
        for url in e.mimeData().urls():
            fileDir = str(url.toLocalFile())
            print("fileDir " +fileDir)
            fileName = fileDir[fileDir.rfind('/') + 1:]
            print( fileName )
            name, ext = fileName.split(".")
            print(name + "-" + ext)
            intTime = int(name, 16)
            print(fileName  + "," + str(intTime))
            xyz = LogFileListClass(fileDir, fileName, intTime)
            print(xyz)
            LogFileList.append(xyz)

        print("dropEvent END len "  + str(len(LogFileList)))
        LogFileList.sort(key=lambda x: x.LogTimeStamp, reverse=False)

        self.DragAndDropSignal.emit()
        print("dropEvent END2")


class Ui_LogFileTool(QFileDialog):
    global LogFileList

    def logFileToolHere(self):
        print( "logFileToolHere" )

    def dragEnterEvent(self, event):
        print("dragEnterEvent" + str(event))

    def setupUi(self, LogFileTool):

        LogFileTool.setObjectName("LogFileTool")
        LogFileTool.resize(735, 600)

        self.centralwidget = QtWidgets.QWidget(LogFileTool)
        self.centralwidget.setObjectName("centralwidget")
        self.sourceCb = QComboBox(self.centralwidget)
        self.sourceCb.setGeometry(QtCore.QRect(30, 30, 541, 22))
        self.sourceCb.setObjectName("comboBox")
        self.findSourceBtn = QPushButton(self.centralwidget)
        self.findSourceBtn.setGeometry(QtCore.QRect(600, 30, 75, 23))
        self.findSourceBtn.setObjectName("findSourceBtn")

        self.filesLv = QTableWidget(self.centralwidget)
        self.filesLv.setGeometry(QtCore.QRect(30, 70, 541, 431))
        self.columnCount = 0
        self.rowCount = 0
        self.filesLv.setColumnCount(self.columnCount)
        self.filesLv.setRowCount(self.rowCount)
        self.filesLv.setAlternatingRowColors(True)
        self.filesLv.setToolTip("")
        self.filesLv.setObjectName("filesLv")
        self.filesLv.show()

        self.clearListBtn = QPushButton(self.centralwidget)
        self.clearListBtn.setGeometry(QtCore.QRect(600, 70, 75, 23))
        self.clearListBtn.setObjectName("clearListBtn")
#        self.clearListBtn.setEnabled(True)  # Temp for debug

        self.scanSourceBtn = QPushButton(self.centralwidget)
        self.scanSourceBtn.setGeometry(QtCore.QRect(600, 110, 75, 23))
        self.scanSourceBtn.setObjectName("scanSourceBtn")
        #        self.scanSourceBtn.setEnabled(False)

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 47, 13))
        self.label.setObjectName("label")

        self.listCount = QLabel(self.centralwidget)
        self.listCount.setGeometry(QtCore.QRect(600, 170, 101, 17))
        self.listCount.setObjectName("listCount")

        self.destinationComboBox = QComboBox(self.centralwidget)
        self.destinationComboBox.setGeometry(QtCore.QRect(30, 530, 541, 22))
        self.destinationComboBox.setObjectName("destinationComboBox")

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 510, 61, 16))
        self.label_2.setObjectName("label_2")

        self.concatenateListBtn = QPushButton(self.centralwidget)
        self.concatenateListBtn.setGeometry(QtCore.QRect(600, 220, 101, 23))
        self.concatenateListBtn.setObjectName("concatenateListBtn")
        self.concatenateListBtn.setEnabled(False)

        self.recursiveCb = QCheckBox(self.centralwidget)
        self.recursiveCb.setEnabled(False)
        self.recursiveCb.setGeometry(QtCore.QRect(600, 140, 101, 17))
        self.recursiveCb.setObjectName("recursiveCb")

        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)

        self.dragDropLabel = CustomLabel('Drop here.', self.centralwidget)
#        print( "jcm " + str(self.dragDropLabel.jcm))
        self.dragDropLabel.DragAndDropSignal.connect(self.DragAndDropEvent)

        self.dragDropLabel.move(590, 330)
        self.dragDropLabel.setFont(font)
        self.dragDropLabel.setGeometry(QtCore.QRect(590, 300, 121, 91))
        self.dragDropLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.dragDropLabel.setMidLineWidth(9)
        self.dragDropLabel.setScaledContents(True)
        self.dragDropLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dragDropLabel.setWordWrap(True)

        LogFileTool.setCentralWidget(self.centralwidget)

        self.dragDropLabel.CustomLabelOutput()

#        self.menubar = QtWidgets.QMenuBar(LogFileTool)
#        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 21))
#        self.menubar.setObjectName("menubar")
#        LogFileTool.setMenuBar(self.menubar)
#        self.statusbar = QtWidgets.QStatusBar(LogFileTool)
#        self.statusbar.setObjectName("statusbar")
#        LogFileTool.setStatusBar(self.statusbar)

        self.retranslateUi(LogFileTool)
        QtCore.QMetaObject.connectSlotsByName(LogFileTool)

    def DragAndDropEvent(self):
        print("DragAndDropEvent")
        self.fillFilesTableView()

    def retranslateUi(self, LogFileTool):
        _translate = QtCore.QCoreApplication.translate
        LogFileTool.setWindowTitle(_translate("LogFileTool", "Log File Tool"))
        self.findSourceBtn.setText(_translate("LogFileTool", "..."))
        self.clearListBtn.setText(_translate("LogFileTool", "Clear List"))
        self.scanSourceBtn.setText(_translate("LogFileTool", "Scan Source"))
        self.label.setText(_translate("LogFileTool", "Source Directories:"))
        self.label_2.setText(_translate("LogFileTool", "Destination:"))
        self.listCount.setText(_translate("LogFileTool", "List Count:"))
        self.concatenateListBtn.setText(_translate("LogFileTool", "Concatenate Files"))
        self.recursiveCb.setText(_translate("LogFileTool", "Recursive Scan"))
        self.dragDropLabel.setText(_translate("LogFileTool", "Drag and drop here"))

        self.findSourceBtn.clicked.connect(self.findSourceBtnPressed)
        self.clearListBtn.clicked.connect(self.clearListBtnPressed)
        self.scanSourceBtn.clicked.connect(self.scanSourceBtnPressed)
        self.concatenateListBtn.clicked.connect(self.concatenateListBtnPressed)
        self.filesLv.cellDoubleClicked.connect(self.filesLvDoubleClicked)

        defaultDirectory = "C:/Users/John Mullarkey/PycharmProjects/LogFileSamples"
        self.sourceCb.addItem(defaultDirectory)

    def updateButtonEnables(self):

        if self.filesLv.rowCount() == 0:
            self.concatenateListBtn.setEnabled(False)
            self.clearListBtn.setEnabled(False)
        else:
            self.concatenateListBtn.setEnabled(True)
            self.clearListBtn.setEnabled(True)


    def findSourceBtnPressed(self):
        print("findSourceBtnPressed")
        home = os.getenv("HOME")
        print(home)
        print(expanduser("~"))

        try:
            myDir = QFileDialog.getExistingDirectory(self)
        except:
            pass

        if myDir:
            print(myDir)
            self.sourceCb.addItem(myDir)
            print(self.sourceCb.count())
            self.sourceCb.setCurrentIndex(self.sourceCb.count() - 1)

    def clearListBtnPressed(self):
        print("clearListBtnPressed " + str(len(LogFileList)))
        self.columnCount = 0
        self.rowCount = 0
        self.filesLv.setColumnCount(self.columnCount)
        self.filesLv.setRowCount(self.rowCount)
        self.filesLv.clear()
#        self.fillFilesTableView()
        self.LogFileList.clear()


    def scanSourceBtnPressed(self):
        srcCount = self.sourceCb.count()
        print("Source count " + str(srcCount))
        if srcCount == 0:
            print("No Source directory")
            QMessageBox.question(self, "Log File Tool", "No Source Directory", QMessageBox.Ok)
        else:
            #            listCount = self.filesLv.count()
            #            print("scanSourceBtnPressed " + str(listCount))
            #            if listCount == 0:
            #                print("List Empty")
            #                QMessageBox.question(self, "Log File Tool", "Source List Empty", QMessageBox.Ok)
            #            else:
            srcDir = self.sourceCb.currentText()
            print("List NOT Empty " + srcDir)
            os.chdir(srcDir)
            dirList = os.listdir()
            print(dirList)

#            intList = []
            for x in dirList:
                if "LOG" in x:
                    name, ext = x.split(".")
                    intTime = int(name, 16)
                    print(x + " -> " + name + "-" + ext + " -> " + str(intTime))
#                    intList.append(intTime)
                    LogFileList.append(LogFileListClass(x, intTime))
                else:
                    print(x + " not processed")

            print("Log files found: " + str(len(LogFileList)))

            LogFileList.sort(key=lambda x: x.LogTimeStamp, reverse=False)
            self.fillFilesTableView()

    def fillFilesTableView(self):
        print("fillFilesTableView - len " + str(len(LogFileList)))
        self.columnCount = 2
        nThTime = False
        for x in LogFileList:
            if nThTime:
                self.rowCount = self.rowCount + 1

            nThTime = True
            self.filesLv.setColumnCount(self.columnCount)
            self.filesLv.setRowCount(self.rowCount + 1)
            self.filesLv.setHorizontalHeaderLabels(["Timestamp", "Filename"])
            self.filesLv.setColumnWidth(0,150)

            tsStr = datetime.utcfromtimestamp(x.LogTimeStamp).strftime('%Y-%m-%d %H:%M:%S')
            self.filesLv.setItem(self.rowCount, 0, QTableWidgetItem(tsStr) )
            self.filesLv.setItem(self.rowCount, 1, QTableWidgetItem(x.LogFilename) )

        print( "Row count " + str(self.filesLv.rowCount()))
        self.updateButtonEnables()

    def concatenateListBtnPressed(self):
        matchfile = 'match.txt'
        MatchRecordList = []
        cwd = os.getcwd()
        print("concatenateListBtnPressed " + str(self.filesLv.rowCount()) + " " + cwd)
        xxx = cwd[cwd.rfind('\\') + 1:]
        ppp = LogFileList[0].LogTimeStamp
        zzz = xxx + "_" + datetime.utcfromtimestamp(ppp).strftime('%Y-%m-%d_%H-%M-%S' ) + ".txt"
        print(zzz )

        if os.path.isfile(matchfile):
            # Open match file
            matchfile = open(matchfile, "r", encoding="utf-8")
            try:
                line = matchfile.readline()
                while line:
                    print(line.strip())
                    # Read lines into match list
                    MatchRecordList.append(MatchRecord(line.strip()))
                    line = matchfile.readline()
            finally:
                matchfile.close()
        else:
            print("No 'match file' found")

        try:
            exists = os.path.isfile(zzz)
            if exists:
                os.remove(zzz)

            outputfile = open(zzz, "w", encoding="utf-8")
            for x in LogFileList:
                print(x.LogFilename + " " + str(x.LogTimeStamp) + " " + datetime.utcfromtimestamp(x.LogTimeStamp).strftime('%Y-%m-%d %H:%M:%S' ))

                inputfile = open(x.LogPathFilename, "r", encoding="utf-8")

                outputfile.write("=" * 60 + "\nLog file: " + x.LogFilename + " Start Time: '" + str(
                    datetime.utcfromtimestamp(x.LogTimeStamp).strftime('%Y-%m-%d %H:%M:%S')) + "' {{ \n" + "=" * 60 + "\n")
                try:
                    line = inputfile.readline()
                    while line:
                        try:
                            outputfile.writelines(line)
                        except:
                            errLine = "\n\nFile Output Error " + str(sys.exc_info()[0]) + " " + x.LogFilename + "\n"
                            print(errLine)
                            outputfile.write(errLine)

                        try:
                            line = inputfile.readline()

                            # For each in Match list
                            for ml in MatchRecordList:
                                if ml.MatchString in line:
                                    #print( "Matched Line : " + line)
                                    ml.Count = ml.Count + 1

                        except:
                            errLine = "\n\nFile Input Error 1: " + str(sys.exc_info()[0]) + " " + x.LogFilename + "\n"
                            print(errLine)
                            outputfile.write(errLine)

                    outputfile.write("}}\n")

                except:
                    errLine = "\n\nFile Input Error: " + str(sys.exc_info()[0]) + " " + x.LogFilename + "\n"
                    print(errLine)
                    outputfile.write(errLine)
                finally:
                    inputfile.close()

        finally:
            if (MatchRecordList.__len__() > 0):
                outputfile.write("\nMatch results:\n")
                Count = 0
                for ml in MatchRecordList:
                    outputfile.write(
                        '{:>3}'.format(Count) + '   {:50}'.format(ml.MatchString) + '{:4}'.format(ml.Count) + '\n')
                    Count += 1

            outputfile.close()

    def filesLvDoubleClicked(self,row,col):
        print("filesLvDoubleClicked " + str(row) + " "  + str(col) )
        if col == 1:
            print( str(self.filesLv.item(row,col).text()) )
            os.system('notepad.exe')

if __name__ == "__main__":
    import sys

    LogFileList = []

    app = QtWidgets.QApplication(sys.argv)
    LogFileTool = QtWidgets.QMainWindow()
    ui = Ui_LogFileTool()
    ui.setupUi(LogFileTool)
    LogFileTool.show()
    sys.exit(app.exec_())

