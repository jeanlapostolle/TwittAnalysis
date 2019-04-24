import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from ui_mainwindow import Ui_MainWindow
from get import *
from wcloud import *
from frequentation import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOuvrir_HTML.triggered.connect(self.loadHTML)
        self.ui.actionOuvrir_CSV.triggered.connect(self.loadCSV)
        self.ui.actionEnregistrer_CSV.triggered.connect(self.saveCSV)
        self.ui.actionEnregistrer_Worcloud.triggered.connect(
            self.saveWorkCloud)
        self.ui.actionEnregistrer_Fr_quences.triggered.connect(
            self.saveFrequences)
        self.ui.actionQuitter.triggered.connect(self.close)
        self.ui.actionCr_ateur.triggered.connect(self.crea)
        self.ui.actionAide.triggered.connect(self.help)

        self.ui.wcupdate.clicked.connect(self.setWordCloud)

        self.resize(820, 540)
        self.setWindowTitle("TwittAnalysis")
        self.setWindowIcon(QIcon("./ressource/logo2.svg"))

    def updateGraph(self):
        self.setWordCloud()
        self.setFrequence()

    def loadHTML(self, e):
        fdialog = QFileDialog()
        fname = fdialog.getOpenFileName(
            self, 'Open file', '.', "HTML file (*.html)")
        fdialog.setVisible(False)
        if fname[0]:
            # print("load")
            HTMLtoCSV(fname[0])
            # print("load end")
            self.updateGraph()

    def loadCSV(self, e):
        fdialog = QFileDialog()
        fname = fdialog.getOpenFileName(
            self, 'Open file', '.', "CSV file (*.csv)")
        fdialog.setVisible(False)
        if fname[0]:
            fin = open(fname[0], 'r')
            fout = open("res.csv", 'w')
            for line in fin.readlines():
                # print(line)
                fout.write(line)
            fout.close()
            self.updateGraph()

    def saveCSV(self, e):
        name = QFileDialog.getSaveFileName(
            self, 'Save File')
        fin = open("res.csv", 'r')
        fout = open(name[0], 'w')
        for line in fin.readlines():
            # print(line)
            fout.write(line)
        fout.close()
        fin.close()

    def saveWorkCloud(self, e):
        name = QFileDialog.getSaveFileName(
            self, 'Save File')
        nam = name[0]
        if nam:
            if not name[0].endswith(".png"):
                nam += ".png"
            stopword = set()
            for word in self.ui.textEdit.toPlainText().split(";"):
                stopword.add(word)
            width = self.ui.wcwidth.value()
            height = self.ui.wcheight.value()
            WCLOUD(stopword, nam, w=width, h=height)

    def saveFrequences(self, e):
        name = QFileDialog.getSaveFileName(
            self, 'Save File')
        nam = name[0]
        if nam:
            if not name[0].endswith(".png"):
                nam += ".png"
            FREQ(nam)

    def crea(self):
        QDesktopServices.openUrl(QUrl("https://github.com/jeanlapostolle/"))

    def help(self):
        QDesktopServices.openUrl(
            QUrl("https://github.com/jeanlapostolle/TwittAnalysis"))

    def setWordCloud(self):
        stopword = set()
        for word in self.ui.textEdit.toPlainText().split(";"):
            stopword.add(word)
        width = self.ui.wcwidth.value()
        height = self.ui.wcheight.value()
        WCLOUD(stopword, w=width, h=height)

        pixmap = QPixmap("wordcloud.png", )
        self.ui.wcloud.setPixmap(pixmap)
        self.ui.wcloud.show()
        self.ui.wcloud.setScaledContents(True)

    def setFrequence(self):
        FREQ()
        pixmap = QPixmap("freq.png")
        self.ui.freq.setPixmap(pixmap)
        self.ui.freq.show()
        self.ui.freq.setScaledContents(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()
