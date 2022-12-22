import sys, re, urllib
import html2text
from urllib import request

from newsform import *


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.newsurl = []
        self.Parse()

        self.ui.pushButton.clicked.connect(self.AllNews)

    def Parse(self):
        s = 'https://seanews.ru/category/news/'
        doc = urllib.request.urlopen(s).read().decode('utf-8', errors='iqnore')
        doc = doc.replace('\n', '')
        zagolovki = re.findall('<a class="category_item_title" href="(.+?)</a>', doc)
        for x in zagolovki:
            self.newsurl.append(x.split('">')[0])
            self.ui.listWidget.addItem(x.split('">')[1])

    def AllNews(self):
        n = self.ui.listWidget.currentRow()
        u = self.newsurl[n]
        doc = urllib.request.urlopen(u).read().decode('utf-8', errors='iqnore')
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.body_width = False
        h.ignore_images = True
        doc = h.handle(doc)
        mas = doc.split('\n')
        stroka = ''
        for x in mas:
            if(len(x)>150):
                stroka = stroka+x+'\n\n'
        self.ui.textEdit.setText(stroka)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
