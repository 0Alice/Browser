# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\__studia2\2\EZI\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Browser import Browser
from PyQt5.QtWidgets import QMessageBox
from Query import Query

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.keywordsName=''
        self.docName=''
        self.itemsDict={}
        self.keywords=''
        self.idf={}
        self.docList=[]
        self.browser=None
        self.flag=0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 849)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 701, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 20, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.search)

        '''self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(15, 71, 951, 731))
        self.listView.setObjectName("listView")
        self.listView.clicked.connect(self.onItemSelect)
'''
        self.listWidget=QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(15, 71, 951, 731))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.clicked.connect(self.onItemSelect)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(840, 19, 121, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.clicked.connect(self.onCheckBoxChange)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 985, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)


        self.actionOpen_documents = QtWidgets.QAction(MainWindow)
        self.actionOpen_documents.setObjectName("actionOpen_documents")
        self.actionOpen_documents.triggered.connect(self.docOpen)

        self.actionOpen_terms = QtWidgets.QAction(MainWindow)
        self.actionOpen_terms.setObjectName("actionOpen_terms")
        self.actionOpen_terms.triggered.connect(self.termOpen)

        self.menuFile.addAction(self.actionOpen_documents)
        self.menuFile.addAction(self.actionOpen_terms)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Browser"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.checkBox.setText(_translate("MainWindow", "Query extension"))
        self.actionOpen_documents.setText(_translate("MainWindow", "Open documents"))
        self.actionOpen_terms.setText(_translate("MainWindow", "Open keywords"))

    def search(self):
        self.listWidget.clear()
        if(self.flag==1):
            self.browser.documentsSimilarityList(self.textEdit.toPlainText())
            for i in self.browser.similarityList:
                item = QtWidgets.QListWidgetItem()
                item.setData(1,i[0])
                item.setText(i[2])
                self.listWidget.addItem(item)
        queryObject = Query(self.textEdit.toPlainText())


    def docOpen(self):
        options = QFileDialog.Options()
        self.docName, _ = QFileDialog.getOpenFileName(None, "Choose file with documents", "",
                                                  "All Files (*)", options=options)
        self.createBrowser()

    def termOpen(self):
       options = QFileDialog.Options()
       self.keywordsName, _ = QFileDialog.getOpenFileName(None, "Choose file with keywords", "",
                                                          "All Files (*)", options=options)
       self.createBrowser()



    def createBrowser(self):
        self.listWidget.clear()
        if ((self.keywordsName != '') & (self.docName != '')):
            self.flag = 1
            print(self.checkBox.isChecked())
            self.browser = Browser(self.keywordsName, self.docName,self.checkBox.isChecked())



    def onCheckBoxChange(self):
        self.createBrowser()

    def onItemSelect(self):
        item=self.listWidget.currentItem()
        msg = QMessageBox()
        msg.setGeometry(QtCore.QRect(15, 71, 951, 731))
        msg.setWindowTitle(item.data(1).title)
        msg.setText("Original: \n\n"+item.data(1).originalDoc+"\n\n\n\nAfter stemming:\n\n"+item.data(1).finalDoc)
        msg.exec()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

