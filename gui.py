# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\__studia2\2\EZI\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from Browser import Browser
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
        self.textEdit.setGeometry(QtCore.QRect(15, 70, 701, 31))
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(730, 70, 75, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.search)
        # self.textEdit.textChanged.connect(self.onTextChanged)
        '''self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(15, 71, 951, 731))
        self.listView.setObjectName("listView")
        self.listView.clicked.connect(self.onItemSelect)
'''
        self.listWidget=QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(15, 121, 701, 731))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.clicked.connect(self.onItemSelect)

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(840, 70, 121, 31))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.clicked.connect(self.onCheckBoxChange)

        self.smallListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.smallListWidget.setGeometry(QtCore.QRect(730, 120, 231, 731))
        self.smallListWidget.setObjectName("smallListWidget")
        self.smallListWidget.clicked.connect(self.onSmallItemSelect)

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 20, 131, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(490, 20, 131, 31))
        self.textEdit_3.setObjectName("textEdit_3")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 20, 20, 20))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 20, 91, 20))
        self.label_2.setObjectName("label_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 20, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.runKnn)


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
        self.label.setText(_translate("MainWindow", "K"))
        self.label_2.setText(_translate("MainWindow", "Max iterations"))
        self.pushButton_2.setText(_translate("MainWindow", "Run k-NN"))

    def search(self):
        self.listWidget.clear()
        self.smallListWidget.clear()
        if(self.flag==1):
            self.queryObject = Query(self.textEdit.toPlainText(),self.browser.keywords.terms,self.checkBox.isChecked())
            if(self.checkBox.isChecked()):
                self.queryObject.getExtesion(self.browser.coincidenceMatrix)
                for i in self.queryObject.extension:
                    item = QtWidgets.QListWidgetItem()
                    item.setData(1, i[0])
                    item.setText(i[2])
                    self.smallListWidget.addItem(item)
            self.browser.documentsSimilarityList(self.queryObject)
            for i in self.browser.similarityList:
                item = QtWidgets.QListWidgetItem()
                item.setData(1,i[0])
                item.setText(i[2])
                self.listWidget.addItem(item)

    def runKnn(self):
        if(self.textEdit_2.toPlainText()!="" and self.textEdit_3.toPlainText()!=""):
            self.listWidget.clear()
            self.smallListWidget.clear()
            if(self.flag==1):
                self.browser.runKNN(int(self.textEdit_2.toPlainText()),int(self.textEdit_3.toPlainText()))
                counter=0
                for i in self.browser.groups:
                    item = QtWidgets.QListWidgetItem()
                    item.setText("Group "+str(counter))
                    self.listWidget.addItem(item)
                    for d in i:
                        item = QtWidgets.QListWidgetItem()
                        item.setData(1,d)
                        item.setText(d.title)
                        self.listWidget.addItem(item)
                    counter+=1


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
        self.smallListWidget.clear()
        self.createBrowser()

    def onItemSelect(self):
        item=self.listWidget.currentItem()
        if(item.data(1)!=None):
            msg = QMessageBox()
            msg.setGeometry(QtCore.QRect(15, 71, 951, 731))
            msg.setWindowTitle(item.data(1).title)
            msg.setText("Original: \n\n"+item.data(1).originalDoc+"\n\n\n\nAfter stemming:\n\n"+item.data(1).finalDoc)
            msg.exec()

    def onSmallItemSelect(self):
        item = self.smallListWidget.currentItem()
        newQuery = self.textEdit.toPlainText() + " " + item.data(1)
        self.textEdit.clear()
        self.textEdit.setText(newQuery)
        self.search()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

